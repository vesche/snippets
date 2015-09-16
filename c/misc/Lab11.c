#include <stdio.h>

int main()
{
    char *days[] = {"Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"};
    int i, input, total;

    for (i = 0; i < 7; i++) {
        printf("Threat Level (%s): ", days[i]);
        scanf("%d", &input);
        if ( input <= 5 && input >= 1 ) {
            total += input;
        } else {
            i--;
        }
    }
    
    int average = (total/7.0f) + 0.5;
    printf("Average Threat Lvl: %d\n", average);
    
    return 0;
}