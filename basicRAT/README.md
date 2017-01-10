# basicRAT

Boilerplate python RAT.

## Features todo
* If I branch this off...
    * C2 Protocol selection? HTTP, HTTPS, DNS, NTP, etc
    * remote CMD.EXE
    * persistance
    * file upload/download
    * screenshots
    * keylogger
    * priv esc, mimikatz, etc
* curses server command line tool (allow additional client connection)
* additional / stronger crypto

## Notes
* key generated with `binascii.hexlify(os.urandom(16))`
* should data be base64 encoded after encryption?

## Other Python RATs to look at
* [ahhh/Reverse_DNS_Shell](https://github.com/ahhh/Reverse_DNS_Shell)
* [sweetsoftware/Ares](https://github.com/sweetsoftware/Ares)