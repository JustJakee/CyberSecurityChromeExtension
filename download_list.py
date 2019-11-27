import requests

ex_request = requests.get("https://raw.githubusercontent.com/austinheap/sophos-xg-block-lists/master/adguard.txt")
if ex_request.status_code != 200:
    print("failure") # later substitute to log or notify owner
else:
    ex_list = ex_request.text.split()
    print(ex_list)
