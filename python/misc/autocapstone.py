#!/usr/bin/python

# autocapstone v0.1 - Austin Jackson
# Given a url, attempts to automate the five phase offensive methodology process.

import os
import sys
import time

def write_cmd(cmd, file_name):
    with open(file_name+'.txt', 'w') as f:
        f.write(os.popen(cmd).read())

def prompt_stop():
    prompt = raw_input('Continue (y/n)? ')
    if prompt[0].lower() == 'n':
        sys.exit(1)

# start
print '----------------------------------'
print 'Autocapstone v0.1 - Austin Jackson'
print '----------------------------------'
url = raw_input('Url? ')

# info gather
print 'Performing nslookup...'
write_cmd('nslookup {0}'.format(url), 'nslookup')
print 'Performing whois...'
write_cmd('whois {0}'.format(url), 'whois')
print 'Finding nameservers...'
write_cmd('dig {0} NS'.format(url), 'nameservers')

# get web server ip
with open('nslookup.txt', 'r') as f:
    web_ip = f.read().split()[-1]
    if len(web_ip.split('.')) != 4:
        print 'nslookup failed, url not up?'
        sys.exit(1)
print 'Got IP of webserver!'

# get name server ip
with open('nameservers.txt', 'r') as f:
    for line in f.readlines():
        if line[0] != ';':
            try:
                ip = line.split()[-1]
                if ip.split('.')[0] == web_ip.split('.')[0]:
                    ns_ip = ip
            except:
                continue

#zone transfer
try:
    ns_ip
    print 'Got a nameserver IP!'
except:
    print 'No name server found.'
    prompt_stop()
try:
    print 'Performing zonetransfer...'
    write_cmd('dig @{0} {1} AXFR'.format(ns_ip, url), 'zonetransfer')
except:
    print 'Zone Transfer failed.'
    prompt_stop()

# Gather IPs
hosts = []
subnet = '.'.join(web_ip.split('.')[0:3]) + '.0/24'
print 'Performing probe scan...'
write_cmd('nmap -sP '+subnet, 'nmap_probe')
with open('nmap_probe.txt') as f:
    for line in f.readlines():
        if 'Nmap scan report' in line:
            hosts.append(line.split()[-1])

# host scanning
print 'Agressively scanning hosts...'
for host in hosts:
    print 'Scanning', host
    write_cmd('nmap -A '+host, 'nmap_'+host)

# spider website for emails
print '\nCrawling the website for emails!'
os.system('python email_crawl.py '+url)
raw_input("Let me know when the coast is clear...")

# Get mail server
with open('zonetransfer.txt') as f:
    for line in f.readlines():
        ip = line.split()[-1]
        if ('mail' in line) and (ip.split('.')[0] == web_ip.split('.')[0]):
            mail_ip = ip
            break

# send emails to get browser data
# cmd = 'sendmail -f mrobinson@{0} -t {1} -u \"Hello!\" -s {2}:25 -o message-content-type=html \
# -o message-file=/root/scripts/fake_email.html'.format(url, victim, mail_ip)

print '----------------------------------'
print 'Done, double check files please!!!'
print '----------------------------------'