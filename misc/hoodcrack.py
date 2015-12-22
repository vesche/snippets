import os

def command_data(command):
    return os.popen(command).read().split()

def netstat():
    netstat = command_data("netstat -ano")

    return netstat

def tasklist():
    data = command_data("tasklist")
    del data[0:21]

    name, pid, mem_usage = [], [], []

    for i in range(len(data)):
        try:
            a, b, _, _, c, _ = data[0:6]
            del data[0:6]
        except:
            break

        name.append(a)
        pid.append(b)
        mem_usage.append(c)

    return name, pid, mem_usage

def main():
    print tasklist()

if __name__ == "__main__":
    main()
