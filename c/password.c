/* Description: Write a program to validate a user-entered
** password against specific password requirements and provide feedback to the user
** describing what requirements don't match
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

/* Function prototypes */
int passwordLength(char password[]);
bool mixed(char password[]);
bool isOneDigit(char password[]);

int main()
{
    char password[21];

    for (;;) {
        /* Get password from the user*/
        printf("Please enter a password between 8-20 characters with one of the following:\n");
        printf("lower-case letter, upper-case letter, numeric digit: \n");
        printf("Password: ");
        scanf("%s", password);


        /* Validate password length is between 8-20 characters */
        if (passwordLength(password) < 8) {
            printf("Length is less than 8!");
            continue;
        }

        else if (mixed(password) == false) {
            printf("Must contain at least one upper case letter and one lower case letter!\n");
            continue;
        }

        /* proceed with confirming there is a digit */
        else if (isOneDigit(password) == false) {
            printf("Must contain at least one number!");
            continue;
        }
        else {
            printf("valid!\n");
        }
    }

    return 0;
}

/* function to count password character-length */
int passwordLength(char password[]) {
    int count = 0;
    while ( password[count] != '\0' )
        ++count;
    return count;
}

/* function to check for a digit */
bool isOneDigit(char password[]) {
    int i;

    for (i = 0; password[i] != '\0'; i++) {
        if (isdigit(password[i])) {
            return true;
        }
    }

    return false;
}

bool mixed(char password[]) {
    int i;
    char found_lower = false, found_upper = false;

    for (i = 0; password[i] != '\0'; i++) {
        found_lower = found_lower || (password[i] >= 'a' && password[i] <= 'z');
        found_upper = found_upper || (password[i] >= 'A' && password[i] <= 'Z');
        if (found_lower && found_upper) return true;
    }

    return false;
}
