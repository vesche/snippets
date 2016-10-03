# ojar Runecrafting

Let's make a rune! First clone the ojar repository and create a new rune file. There currently isn't a `p` rune, so lets make one and call it the [p]ersonal rune.

```bash
$ git clone https://github.com/vesche/ojar
$ cd ojar
$ vi runes/p.py
```

Every function you create inside your rune is an action that the rune will be capable of doing. At minimum a rune needs to include the `info` function which will display the name of the rune and everything action that rune has available.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ojar - [p]ersonal rune

def info(_):
    from common import list_functions
    return "[p]ersonal rune\nactions: {}".format(list_functions(__name__))
```

It's important to point out that every function requires an argument, but if an argument isn't necessary than just pass `_` to the function.

Let's test it out!

```bash
$ ./ojar.py
> p ?
[p]ersonal rune
actions: info
```

And we got ourselves a rune! The only thing that our rune can do currently is display all of it's actions, boring! Let's make it do something more fun, crack open that `p.py` file again with your favorite text editor.

```python
def swag(n):
    for _ in range(int(n)):
        print "Look mom no hands!"
```

So now we got a sweet new action called swag that will print a silly phrase however many times you tell it. Keep in mind that all arguments are passed as a string, so it was necessary to convert `n` into an integer.

```bash
$ ./ojar.py
> p swag 3
Look mom no hands!
Look mom no hands!
Look mom no hands!
```







a
