import os
import re
import requests

# These are the domains of the different filter lists we use.
input_lists =  [("https://1hos.cf/complete/hosts.txt", "1Hosts"), \
                ("https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt", "NoTracking"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/nocoin.txt", "NoCoin"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/easylist.txt", "EasyList"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/coinblocker.txt", "CoinBlocker"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/adguard.txt", "AdGuard") ]

# This for loop writes each domain of each list into a file.
for list in input_lists:
    ex_request = requests.get(list[0])
    if ex_request.status_code != 200:
        print("failed to download list from" + list) # later substitute to log or notify owner
    else:
        f = open("Filterlists/" + list[1] + ".txt", 'w')
        f.write(ex_request.text);
        f.close()

# Formats the domains in 1Hosts.txt to match our standard.
with open('Filterlists/1Hosts.txt', 'r+') as OneHosts:
    for i in range(25):
        OneHosts.readline()
    content = OneHosts.read()
    OneHosts.seek(0)
    OneHosts.write(re.sub('^\S+ (.*)', '\g<1>', content, count=0, flags=re.M))
    OneHosts.truncate()

# Formats the domains in NoTracking.txt to match our standard.
with open('Filterlists/NoTracking.txt', 'r+') as NoTracking:
    for i in range(15):
        NoTracking.readline()
    content = NoTracking.read()
    NoTracking.seek(0)
    NoTracking.write(re.sub('^address=\/(.*?)\/.*', '\g<1>', content, count=0, flags=re.M))
    NoTracking.truncate()

# Creates a set() of all the domains in all the txt files.
dir = "Filterlists"
master_set = set()
for file in os.listdir(dir):
    f = open(dir + '/' + file)
    for line in f:
        master_set.add(line)
    f.close()

# Further formats each domain in the set to match the standards of the Chrome APIs and then adds it to a list.
master_list = []
for ele in master_set:
   master_list.append("*://*." + str(ele).strip() + "/*")

# Writes the fully formatted domains to MASTER_FILTER_LIST.txt which will be transferred to our JavaScript code.
with open('MASTER_FILTER_LIST.txt', 'w') as master:
    master.write(str(master_list))

