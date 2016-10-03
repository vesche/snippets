# ojar (Oh, Just Another REPL)

Welcome to ojar, a little toolkit for using and organizing python scripts that do simple tasks. It uses a syntax of runes (single letters) as categories, actions (words with meaning) to define what you want to do, and arguments (supplied data).

### How do I use this thing?
It's as easy as rune, action, argument. For example, let's say you wanted to know the length of a string. Well then use the [s]tring rune, the 'length' action, and supply it an argument. Check it out:
```
> s length Hello, world!
13
```

### Hmm, nifty. So how do I know what rune does what?
The [o]jar rune is used for these admin sorts of things. Run `o runelist` to get a list of all the runes and their purpose.

### Cool, but how do I know what I can do with a rune?
When in doubt use `?`. For example, if you wanted to know all the actions you could do with the [s]tring rune see `s ?`.

### I want to make a rune!
See the [Runecrafting](doc/RUNECRAFTING.md) document.
