#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

int
main()
{
    // init
    size_t len = strlen("foo");

    uint32_t a = len * 0x875CD;
    uint64_t b = a * 0x51EB851FULL;
    uint32_t c = b >> 32;
    int32_t  d = c >> 5;
    uint32_t e = d * 0x0FFFFFC90;
    double   f = (double)e;
    int32_t  g = *(int32_t *)&f;

    printf("%i\n", g);
    return 0;
}
