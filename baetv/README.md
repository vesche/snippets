# baetv

Kivy mobile app code & custom pyvizio server for Amy's vizio tv.

## Note

Right and up key wouldn't work had to modify pyvizio `_protocol.py` with:

```
 ...
 "RIGHT2": (3, 7),
 "UP2": (3, 8),
 ...
```

