import os
import time
import poopthrow

while True:
    ctime = os.popen('date').read().split()[3]
    ctemp = os.popen('sensors').read().split()[25][0:5]

    poopthrow.insert('temp', '1.data', ctime, ctemp)
    time.sleep(5)