#include <stdio.h>
#include <stdlib.h>

void menu();
void game();
void game_output(char map[], int coins, int pos);

int main() {
    menu();
    game();
}

void game() {
    /* init vars */
    char map[9] = {'_','_','_','_','_','_','_','_','_'};
    int pos = 4;
    int coins = 0;
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
        
        /* print game output */
        game_output(map, coins, pos);
        scanf(" %c", &move);
        system("clear");
        
        /* reset player location */
        map[pos] = '_';
        
        /* player moves */
        if (move == 'n' && pos > 2) {
            pos -= 3;
        }
        else if (move == 's' && pos < 6) {
            pos += 3;
        }
        else if (move == 'e' && pos != 2 && pos != 5 && pos != 8) {
                pos += 1;
        }
        else if (move == 'w' && pos != 0 && pos != 3 && pos != 6) {
            pos -= 1;
        }
        else if (move == 'h') {
            printf("%s", help_text);
        }
        else if (move == 'q') {
            exit(0);
        }
    }
}

void game_output(char map[], int coins, int pos) {
    printf("Coins: %d\n", coins);
    printf(" _____ \n|%c|%c|%c|\n|%c|%c|%c|\n|%c|%c|%c|\n", \
    map[0],map[1],map[2],map[3],map[4],map[5],map[6],map[7],map[8]);
    if (pos == 0) { printf("Room 0"); }
    if (pos == 1) { printf("Room 1"); }
    if (pos == 2) { printf("Room 2"); }
    if (pos == 3) { printf("Room 3"); }
    if (pos == 4) { printf("Room 4"); }
    if (pos == 5) { printf("Room 5"); }
    if (pos == 6) { printf("Room 6"); }
    if (pos == 7) { printf("Room 7"); }
    if (pos == 8) { printf("Room 8"); }
    printf("\n> ");
}

void menu() {
    int choice;
    char *about_text =  "You awake in a strange building with nine rooms,\n"
                        "connected together by many doors. Each room has one\n"
                        "coin hidden within. Find all the coins to escape!\n";
    char name[20];

    printf("9coins - By: Vesche\n");
    printf("1. Play\n2. About\n3. Quit\n");

    for (;;) {
        printf("> ");
        scanf("%d", &choice);
        if (choice == 1) {
            system("clear");
            break;
        }
        else if (choice == 2) {
            printf("%s", about_text);
        }
        else if (choice == 3) {
            exit(0);
        }
        else {
            printf("Wut?\n");
        }
    }
}