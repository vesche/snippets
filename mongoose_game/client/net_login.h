#ifndef NET_LOGIN_H_
#define NET_LOGIN_H_

extern struct LoginData {
    int success;
    char *key;
    char *username;
} login_data;

void login(char *username, char *password);

#endif