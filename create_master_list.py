import os
import re
import requests

input_lists =  [("https://1hos.cf/complete/hosts.txt", "1Hosts"), \
                ("https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt", "NoTracking"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/nocoin.txt", "NoCoin"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/easylist.txt", "EasyList"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/coinblocker.txt", "CoinBlocker"), \
                ("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/adguard.txt", "AdGuard") ]

for list in input_lists:
    ex_request = requests.get(list[0])
    if ex_request.status_code != 200:
        print("failed to download list from" + list_url) # later substitute to log or notify owner
    else:
        f = open("filterlists/" + list[1] + ".txt", 'w')
        f.write(ex_request.text);
        f.close()

with open('filterlists/1Hosts.txt', 'r+') as OneHosts:
    for i in range(25):
        OneHosts.readline()
    content = OneHosts.read()
    OneHosts.seek(0)
    OneHosts.write(re.sub('^\S+ (.*)', '\g<1>', content, count=0, flags=re.M))
    OneHosts.truncate()
    
with open('Filterlists/NoTracking.txt', 'r+') as NoTracking:
    for i in range(15):
        NoTracking.readline()
    content = NoTracking.read()
    NoTracking.seek(0)
    NoTracking.write(re.sub('^address=\/(.*?)\/.*', '\g<1>', content, count=0, flags=re.M))
    NoTracking.truncate()

dir = "Filterlists"
master_set = set()
for file in os.listdir(dir):
    f = open(dir + '/' + file)
    for line in f:
        master_set.add(line)
    f.close()

master_list = []
for ele in master_set:
   master_list.append("*://*." + str(ele).strip() + "*")

with open('MASTER_FILTER_LIST.txt', 'w') as master:
    master.write(str(master_list))

