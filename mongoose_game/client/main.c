#include <stdio.h>
#include <pthread.h>

#include "game.h"
#include "net_login.h"
#include "net_realtime.h"

int
main()
{
    // temp
    char *username = "jackson";
    char *password = "toortoor";

    login(username, password);

    if (login_data.success == 0) {
        printf("Login failed!\n");
        return 1;
    }

    /* create realtime background thread */
    pthread_t thread;
    if (pthread_create(&thread, NULL, realtime, NULL)) {
        perror("Error!");
    }

    testing();


    return 0;
}
