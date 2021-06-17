#!/usr/bin/env python

import os

from fabric import Connection

conn = Connection(
    host='192.168.1.83',
    user='user',
    port=22,
    connect_kwargs={'password': 'hhserver'}
)

# TODO: create sudo config
conn_root = Connection(
    host='192.168.1.83',
    user='root',
    port=22,
    connect_kwargs={'password': 'hhserver'}
)

# end current hhfrontend
conn_root.run('systemctl stop hhfrontend')
conn.run('rm -rf frontend.tar.gz frontend/')

# put new hhfrontend in place
os.system('rm frontend.tar.gz')
os.system('tar cvf frontend.tar.gz ../frontend/')
conn.put('frontend.tar.gz', '/home/user/frontend.tar.gz')
conn.run('tar xvf frontend.tar.gz')
conn.run('pip3 install -r /home/user/frontend/requirements.txt --user')
# TODO: installer - systemd service file in place

# restart hhfrontend
conn_root.run('systemctl restart hhfrontend')
