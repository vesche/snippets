#include <stdio.h>

void
main()
{
    int n;
    scanf("%d", &n);
    
    while (n != 1) {
        int x = n % 3;
        
        if (x == 0) {
            printf("%d 0\n", n);
        }
        else if (x == 1) {
            printf("%d -1\n", n);
            n--;
        }
        else {
            printf("%d 1\n", n);
            n++;
        }
        
        n /= 3;
    }
    
    printf("1\n");
}