#include <stdio.h>

#include "rc4.h"
#include "game.h"
#include "net_login.h"
#include "mongoose/mongoose.h"

static int closed = 0;
static int connected = 0;

// enable or disable encryption for testing
// cause rc4 is hard is guess fucking rip...
int ENCRYPTION = 0;


static void
realtime_event_handler(struct mg_connection *conn, int event, void *event_data)
{
    (void) conn;

    switch (event) {
        case MG_EV_CONNECT: {
            int status = *((int *) event_data);
            if (status != 0) {
                printf("[-] Connection error: %d\n", status);
            }
            break;
        }
        case MG_EV_WEBSOCKET_HANDSHAKE_DONE: {
            struct http_message *hm = (struct http_message *) event_data;
            if (hm->resp_code == 101) {
                printf("[+] Connected\n");
                connected = 1;
            } else {
                printf("[-] Connection failed! HTTP code %d\n", hm->resp_code);
                /* Connection will be closed after this. */
            }
            break;
        }
        case MG_EV_POLL: {
            // char *plaintext = "testing123aaaaaaaaaaa1";
            char plaintext[128];
            snprintf(plaintext, 128, "%s", game_data.direction);

            if (ENCRYPTION == 1) {
                int length = strlen(plaintext);

                // rc4 encrypt plaintext into ciphertext bytes
                unsigned char *ciphertext = malloc(sizeof(int) * length);
                rc4(login_data.key, plaintext, ciphertext);

                // convert ciphertext bytes into hex string
                /* https://stackoverflow.com/a/41173236 */
                char hexstr[(length * 2) + 1];
                char *ptr = &hexstr[0];
                for (int i = 0; i < length; i++) {
                    ptr += sprintf(ptr, "%02X", ciphertext[i]);
                }
                mg_send_websocket_frame(conn, WEBSOCKET_OP_TEXT, hexstr, strlen(hexstr));
            } else {
                mg_send_websocket_frame(conn, WEBSOCKET_OP_TEXT, plaintext, strlen(plaintext));
            }

            break;
        }
        case MG_EV_WEBSOCKET_FRAME: {
            struct websocket_message *wm = (struct websocket_message *) event_data;

            if (ENCRYPTION == 1) {
                // TODO: come back to this...
                // incoming 1024 bytes?
                char ciphertext[1024];
                // snprintf(ciphertext, 1024, "%.*s", (int) wm->size, wm->data);
                snprintf(ciphertext, 1024, "%s", wm->data);

                printf("%s\n%s\n", ciphertext, login_data.key);

                //char *plaintext;
                //rc4(login_data.key, ciphertext, plaintext);

                //plaintext = strstrip(plaintext);
                //printf("%s - %s - %s\n", login_data.key, wm->data, plaintext);
            } else {
                printf("%.*s\n", (int) wm->size, wm->data);
            }

            break;
        }
        case MG_EV_CLOSE: {
            if (connected) printf("[-] Disconnected\n");
            closed = 1;
            break;
        }
    }
}


void
*realtime()
{
    struct mg_mgr mgr;
    struct mg_connection *conn;

    // TODO: careful here, come back to this...
    // check input sizes and evaluate snprintf usage
    char realtime_url[128];
    snprintf(realtime_url, 128, "ws://127.0.0.1:1337/test/%s", login_data.username);

    mg_mgr_init(&mgr, NULL);

    conn = mg_connect_ws(&mgr, realtime_event_handler, realtime_url, NULL, NULL);
    if (conn == NULL) {
        fprintf(stderr, "Invalid address\n");
        // TODO: fix this?
        return NULL;
    }

    while (!closed) {
        mg_mgr_poll(&mgr, 100);
    }
    mg_mgr_free(&mgr);

    return NULL;
}
