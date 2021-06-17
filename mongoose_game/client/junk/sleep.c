// some C sleep code, might need this later.

#include <stdio.h>
#include <unistd.h>

unsigned int microseconds = 100000;

void main() {
    int i;
    for (i = 0; i < 10; i++) {
        printf("Sleeping %d\n", i);
        usleep(microseconds);
    }
}

// little startswith func

#include <string.h>

bool
startswith(const char *pre, const char *str)
{
    return strncmp(pre, str, strlen(pre)) == 0;
}
