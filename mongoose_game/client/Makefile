CC := gcc
#CFLAGS := `sdl2-config --cflags --libs` -lSDL2_image -lSDL2_net -Wall
CFLAGS := -lraylib -Wall -pthread

HDRS := game.h mongoose/mongoose.h net_login.h net_realtime.h rc4.h

SRCS := main.c game.c mongoose/mongoose.c net_login.c net_realtime.c rc4.c
OBJS := $(SRCS:.c=.o)
EXEC := main.build

all: $(EXEC)

$(EXEC): $(OBJS) $(HDRS) Makefile
	$(CC) -o $@ $(OBJS) $(CFLAGS)

#clean:
#	rm -f $(OBJS)
#	# rm -f $(EXEC) $(OBJS)

#.PHONY: all clean
