#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "net_login.h"
#include "mongoose/mongoose.h"

static int exit_flag = 0;
static const char *url = "http://127.0.0.1:8123";

char *key;
struct LoginData login_data;


static void
login_event_handler(struct mg_connection *conn, int event, void *event_data)
{
    struct http_message *msg = (struct http_message *) event_data;

    switch (event) {
        case MG_EV_CONNECT:
            if (*(int *) event_data != 0) {
                fprintf(stderr, "connect() failed: %s\n", strerror(*(int *) event_data));
                exit_flag = 1;
            }
            break;
        case MG_EV_HTTP_REPLY:
            conn->flags |= MG_F_CLOSE_IMMEDIATELY;
            /* https://stackoverflow.com/a/32823094 */
            key = strrchr(msg->body.p, ':') + 1;
            exit_flag = 2;
            break;
        case MG_EV_CLOSE:
            if (exit_flag == 0) {
                printf("Server closed connection\n");
                exit_flag = 1;
            }
            break;
    }
}


void
login(char *username, char *password)
{
    login_data.success = 0;
    login_data.username = username;

    // TODO: careful here, come back to this...
    // check input sizes and evaluate snprintf usage
    char full_url[128];
    snprintf(full_url, 128, "%s/login/%s/%s", url, username, password);

    struct mg_mgr mgr;

    mg_mgr_init(&mgr, NULL);
    mg_connect_http(&mgr, login_event_handler, full_url, NULL, NULL);

    while (exit_flag == 0) {
        mg_mgr_poll(&mgr, 1000);
    }
    mg_mgr_free(&mgr);

    if (exit_flag != 2) {
        // couldn't reach login server...
        exit(1);
    }

    //
    // NOTE:
    // copy key variable into login_data struct
    // or the key variable will be overwritten when mongoose is used again
    //
    // TODO: Revisit this for security/safety
    //
    login_data.key = malloc(sizeof(char) * 16);
    memcpy(login_data.key, key, 16);

    if (strlen(login_data.key) == 16) {
        login_data.success = 1;
    }
}
