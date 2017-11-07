## Cryptosplurge

Usage: `./cryptosplurge.py <file>`  

Cryptosplurge attempts to decrypt a file by attempting many common decryption
methods, and displaying the decrypted text to the user. By manually skimming
the decrypted data, the encryption method could be easily found.  

This is intended for use in CTF events or cyber challenges. **Pushed for
backup purposes, currently only a basic idea.**

### Todo
* make command line utility
* write output to file
* `more` each file
* ncurses keyboard commands
    * SPACE, next page
    * RETURN, next line
    * RIGHT, next decryption
    * LEFT, previous decryption
    * S, save decryption
* add additional crypto
    * fuzzyhash
    * dvorak/qwerty
    * encoding
