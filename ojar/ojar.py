#!/usr/bin/env python

if __name__ == "__main__":
    while True:
        command = raw_input("> ")

        letter, action, argument = command.split()

        module = __import__(letter)

        function = getattr(module, action)

        print function(argument)
