import os
import time

def getdata():
    lhost,lport,rhost,rport,state,pid,prog=[],[],[],[],[],[],[]

    data = os.popen('/bin/netstat -natup').read().split()
    del data[0:16]

    return data

def main():
    while True:

if __name__ = "__main__":
    main()
