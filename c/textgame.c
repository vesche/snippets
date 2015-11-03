#include <stdio.h>
#include <stdlib.h>

void game();
void game_output(char map[], char message[], int coins, int pos);
void menu();

void game() {
    /* init vars */
    int coins       =   0;
    int pos         =   4;
    char map[9]     =   {'_','_','_','_','_','_','_','_','_'};
    char *message   =   "";
    char move;
    char *help_text =   "Moves:\n"
                        "e - move east\n"
                        "h - show help text\n"
                        "l - look around the room\n"
                        "n - move north\n"
                        "q - quit game\n"
                        "s - move south\n"
                        "t - touch something\n"
                        "w - move west\n";

    /* main game loop */
    for (;;) {
        /* set player location */
        map[pos] = '*';
        
        /* print game output and prompt */
        game_output(map, message, coins, pos);
        scanf(" %c", &move);
        system("clear");
        
        /* reset player location and message */
        map[pos]    = '_';
        message     = "";
        
        /* player moves */
        if (move == 'n' && pos > 2)
            pos -= 3;
        else if (move == 's' && pos < 6)
            pos += 3;
        else if (move == 'e' && pos != 2 && pos != 5 && pos != 8)
                pos += 1;
        else if (move == 'w' && pos != 0 && pos != 3 && pos != 6)
            pos -= 1;
        else if (move == 'h')
            message = help_text;
        else if (move == 'q')
            exit(0);
    }
}

void game_output(char map[], char message[], int coins, int pos) {
    /* print values and map */
    printf("Coins: %d\n", coins);
    printf(" _____ \n|%c|%c|%c|\n|%c|%c|%c|\n|%c|%c|%c|\n", \
    map[0],map[1],map[2],map[3],map[4],map[5],map[6],map[7],map[8]);
    
    /* print message and room text */
    printf("%s", message);
    if (pos == 0)
        printf("Room 0");
    if (pos == 1)
        printf("Room 1");
    if (pos == 2)
        printf("Room 2");
    if (pos == 3)
        printf("Room 3");
    if (pos == 4)
        printf("Room 4");
    if (pos == 5)
        printf("Room 5");
    if (pos == 6)
        printf("Room 6");
    if (pos == 7)
        printf("Room 7");
    if (pos == 8)
        printf("Room 8");
    printf("\n> ");
}

void menu() {
    /* menu vars */
    int choice;
    char *about_text =  "You awake in a strange building with nine rooms,\n"
                        "connected together by many doors. Each room has one\n"
                        "coin hidden within. Find all the coins to escape!\n";

    /* menu text */
    printf("9coins - By: Vesche\n");
    printf("1. Play\n2. About\n3. Quit\n");

    /* menu loop */
    for (;;) {
        /* menu prompt */
        printf("> ");
        scanf("%d", &choice);
        
        /* menu choices */
        if (choice == 1)
            break;
        else if (choice == 2)
            printf("%s", about_text);
        else if (choice == 3)
            exit(0);
        else
            printf("Invalid option.\n");
    }
}

int main() {
    menu();
    system("clear");
    game();
}