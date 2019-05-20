# ojar Runecrafting

Let's make a rune! First clone the ojar repository and create a new rune file. There currently isn't a `p` rune, so lets make one and call it the [p]ersonal rune.

```
$ git clone https://github.com/vesche/ojar
$ cd ojar
$ vi runes/p.py
```

Every function you create inside your rune is an action that the rune will be capable of doing. At minimum a rune needs to include the `info` function which will display the name of the rune and every action that the rune has available.

```python
# -*- coding: utf-8 -*-

#
# ojar - [p]ersonal rune
# https://github.com/vesche/ojar
#


def info(_):
    from runes.common import list_functions
    return '[p]ersonal rune\nactions: {}'.format(list_functions(__name__))
```

If you don't want to type this all out you could also just `cp runes/template.py runes/p.py` to create a new rune from the template. It's important to point out that every function requires an argument, but if an argument isn't necessary than just pass `_` to the function.

Let's test it out!

```
$ ./ojar.py
ojar v0.1
Type "?" for help.

ojar > p ?
[p]ersonal rune
actions: info
```

And we got ourselves a rune! The only thing that our rune can do currently is display all of its actions, boring! Let's make this rune do something more fun, crack open that `p.py` file again with your favorite text editor.

```python
def swag(n):
    for _ in range(int(n)):
        print('Look mom no hands!')
```

Now we have a sweet new action called swag that will print a silly phrase however many times you tell it. Keep in mind that all arguments are passed as a string, so it was necessary to convert `n` into an integer.

```
ojar > p swag 3
Look mom no hands!
Look mom no hands!
Look mom no hands!
```

But what would happen if we did something like this?

```
ojar > p swag foo
Traceback (most recent call last):
  File "./ojar.py", line 74, in <module>
    main()
  File "./ojar.py", line 70, in main
    print(ojar_loop() + '\n')
  File "./ojar.py", line 63, in ojar_loop
    return str(action(argument))
  File "/home/admin/code/ojar/runes/p.py", line 15, in swag
    for _ in range(int(n)):
ValueError: invalid literal for int() with base 10: 'foo'
```

Seeing as 'foo' isn't a number (what a shame) this caused ojar to crash! For any action that uses arguments, you must provide smart error handling for it.

```python
def swag(n):
    try:
        n = int(n)
    except ValueError:
        return 'Invalid argument.'

    for _ in range(n):
        print('Look mom no hands!')
```

Let's try that again...

```
ojar > p swag foo
Invalid argument.
```

Much better! Now that you've learned the basics of creating a rune, take a peak at the other runes for more examples. Happy runecrafting! :)
