#!/usr/bin/env python

#
# roonbot - A bot for OSRS in Python.
# https://github.com/vesche
#

import getpass
import os
import sys
import time

try:
    import autopy
except ImportError:
    print 'Error, autopy must be installed (sudo pip install autopy).'
    sys.exit(1)

if not sys.platform.startswith('linux'):
    print 'Error, roonbot must be run on a Linux operating system.'
    sys.exit(1)

BANNER = '''
                                    dP                  dP
                                    88                  88
88d888b. .d8888b. .d8888b. 88d888b. 88d888b. .d8888b. d8888P
88'  `88 88'  `88 88'  `88 88'  `88 88'  `88 88'  `88   88
88       88.  .88 88.  .88 88    88 88.  .88 88.  .88   88
dP       `88888P' `88888P' dP    dP 88Y8888' `88888P'   dP

ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
ooo           https://github.com/vesche/roonbot           ooo
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
'''


def roonbot_init():
    # start the unix-runescape-client
    username = os.popen('whoami').read().strip()
    try:
        os.system('export DISPLAY=:0')
        os.system('cd /home/{0}/.config/runescape/bin && LD_LIBRARY_PATH=/opt/runescape/rsu/3rdParty/linux/cairo-nogl/i386/:/opt/runescape/rsu/3rdParty/linux/cairo-nogl/x86_64/:/usr/lib/jvm/java-7-openjdk-amd64/jre/bin/../lib/amd64/:/usr/lib/jvm/java-7-openjdk-amd64/jre/bin/../lib/amd64/jli/:$LD_LIBRARY_PATH /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java -XX:+UseCompressedOops -XX:+AggressiveOpts -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+TieredCompilation -XX:ReservedCodeCacheSize=256m -XX:+UseAdaptiveGCBoundary -XX:SurvivorRatio=16 -XX:+UseParallelGC -Dhttps.protocols=TLSv1,TLSv1.1,TLSv1.2 -Duser.home=\'/home/{0}/.config/runescape/share/cache\' -cp jagexappletviewer.jar -Dcom.jagex.config=http://oldschool.runescape.com/jav_config.ws -Xmx512m -Xss2m -Dsun.java2d.noddraw=true jagexappletviewer /share/img/OldSchool > /dev/null 2>&1 &'.format(username))
    except:
        print 'Error, the unix-runescape-client did not start.'
        sys.exit(1)

    print BANNER
    print 'Starting the unix-runescape-client, wait about 20 seconds...'
    time.sleep(20)

    # click the initial 'Existing User' button on the client
    init = autopy.bitmap.Bitmap.open('img/init.png')
    retry = 1
    while retry < 4:
        scrot = autopy.bitmap.capture_screen()
        try:
            pos = scrot.find_bitmap(init)
            autopy.mouse.move(pos[0], pos[1])
            autopy.mouse.click(autopy.mouse.LEFT_BUTTON)
            break
        except TypeError:
            print 'Unable to capture the unix-runescape-client (retry {}/3)...'.format(retry)
            retry += 1
            time.sleep(5)
    else:
        print 'Error, unable to find the unix-runescape-client after starting.'
        sys.exit(1)

    username = raw_input('OSRS Username? ')
    password = getpass.getpass('OSRS Password? ')
    print 'Logging in...'

    # attempt to login to client
    autopy.key.type_string(username, 150)
    autopy.key.tap(autopy.key.K_RETURN)
    autopy.key.type_string(password, 150)
    autopy.key.tap(autopy.key.K_RETURN)

    # tmp kill
    c = raw_input('kill app [y/n]').lower()[0]
    if c == 'y':
        os.system('pkill java')


if __name__ == '__main__':
    roonbot_init()
