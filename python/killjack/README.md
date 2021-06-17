# killjack

This is an anti-forensics kill-switch that monitors your headphone jack for changes and will immediately shut down your computer. It was inspired by [usbkill](https://github.com/hephaest0s/usbkill) which does the same thing for usb ports. Currently this utility is only going to work on Linux and may not work with specific hardware sets and distros. If I'm feeling motivated sometime maybe I'll make it usable on most Linux systems and macOS.

You can test killjack out and it won't shut your system off if you run it with the `--testing` option. If you want to have it run in the background just run `sudo python killjack.py & disown` or similar.

```
$ python killjack.py --help
usage: killjack.py [-h] [-i INTERVAL] [-t]

headphone jack monitor kill-switch

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        monitor interval in seconds (default 1 sec)
  -t, --testing         testing mode, system will not shutdown

$ sudo python killjack.py --testing
killjack is running...
Alert: A jack has changed state.
Alert: A jack has changed state.
Alert: A jack has changed state.

$ sudo python killjack.py & disown
```
