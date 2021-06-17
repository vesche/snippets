
#include <stdio.h>
#include "rc4.h"

void
main()
{
    /*
        1 8B5B375F7AD7D73AC40588D8D15C0560515FF6EE610F255A16
        2 b'\x8b[7_z\xd7\xd7:\xc4\x05\x88\xd8\xd1\\\x05`Q_\xf6\xeea\x0f%Z\x16'
        3 362074657374696E672068656C6C6F20667269656E64203A29
        '6 testing hello friend :)'
    */

    char *key = "zivkjwykkrzmjiiz";
    char *ciphertext = "8B5B375F7AD7D73AC40588D8D15C0560515FF6EE610F255A16";

    // unsigned char plaintext[1024];
    char plaintext[1024];
    rc4(key, ciphertext, plaintext);

    printf("%s\n", plaintext);
    
}