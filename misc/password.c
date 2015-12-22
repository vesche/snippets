#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

int passwordLength(char password[]);
bool mixed(char password[]);
bool isOneDigit(char password[]);

int
main()
{
    char password[21];

    printf("Enter a password between 8-20 characters must contain one:\n");
    printf("lower-case letter, upper-case letter, numeric digit: \n");

    for (;;) {
        printf("Password: ");
        scanf("%s", password);

        if (passwordLength(password) < 8) {
            printf("Must be longer than 8 characters!\n");
            continue;
        }
        else if (mixed(password) == false) {
            printf( "Must contain at least one upper case "
                    "letter and one lower case letter!\n");
            continue;
        }
        else if (isOneDigit(password) == false) {
            printf("Must contain at least one number!\n");
            continue;
        }
        else {
            printf("valid!\n");
        }
    }
    return 0;
}

int
passwordLength(char password[])
{
    int count = 0;
    while (password[count] != '\0')
        ++count;
    return count;
}

bool
mixed(char password[])
{
    int i;
    char found_lower = false, found_upper = false;

    for (i = 0; password[i] != '\0'; i++) {
        found_lower = found_lower || (password[i] >= 'a' && password[i] <= 'z');
        found_upper = found_upper || (password[i] >= 'A' && password[i] <= 'Z');
        if (found_lower && found_upper) return true;
    }
    return false;
}

bool
isOneDigit(char password[])
{
    int i;

    for (i = 0; password[i] != '\0'; i++)
        if (isdigit(password[i]))
            return true;
    return false;
}