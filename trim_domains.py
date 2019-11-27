import re

with open('Filterlists/1Hosts.txt', 'r+') as Hosts:
    for i in range(25):
        Hosts.readline()
    content = Hosts.read()
    Hosts.seek(0)
    Hosts.write(re.sub('^\S+ (.*)', '\g<1>', content, count=0, flags=re.M))
    Hosts.truncate()

with open('Filterlists/notracking.txt', 'r+') as NoTracking:
    for i in range(15):
        NoTracking.readline()
    content = NoTracking.read()
    NoTracking.seek(0)
    NoTracking.write(re.sub('^address=\/(.*?)\/.*', '\g<1>', content, count=0, flags=re.M))
    NoTracking.truncate()
