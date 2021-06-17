#!/usr/bin/env python

import os

from fabric import Connection

conn = Connection(
    host='192.168.1.84',
    user='user',
    port=22,
    connect_kwargs={'password': 'hhagent'}
)

# remove old agent zip
os.system('rm agent.zip')

# delete old agent from the endpoint
conn.run('del agent.zip', warn=True)
conn.run('rmdir agent /s /q', warn=True)

# zip up new agent
os.system('pushd .. && zip -r agent.zip agent/ && mv agent.zip tools/')

# put new agent on endpoint
conn.put('agent.zip', 'agent.zip')
conn.run('unzip agent.zip')

# uninstall/install package
conn.run('python -m pip uninstall hhagent -y', warn=True)
conn.run('cd agent && python setup.py install --user')

# TODO: net service to start the server (net start hhagent)