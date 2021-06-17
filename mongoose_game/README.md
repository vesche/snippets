## new_game

Experiments with a few new things:
* https://github.com/raysan5/raylib
* https://github.com/warmcat/libwebsockets/
* https://github.com/aaugustin/websockets

ports:
* 1337 - realtime
* 8123 - login
* 8888 - game
* 41337 - internal (rc4/redis)

notes:
* realtime will be mongoose websockets, sending and recving RC4 encrypted payloads
* login will be mongoose https
* game will be mongoose https
* rc4/database conn server will be all backend/isolated

more notes:
* realtime will have to split off into its own thread... movement + chat + player locations
* load all resources / wait until RC4 key has been recv by other end

hosting:
* Linode, arch linux
