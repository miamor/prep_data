import os
import requests

host = '192.168.126.26'
port = 5002
cuckoo_API = 'http://'+host+':1337'
cuckoo_SECRET_KEY = "Bearer RALTrRjHNT21MZdDCksugg"

HEADERS = {"Authorization": cuckoo_SECRET_KEY}

tasks_to_delete = (1, 5570)

for task_id in range(tasks_to_delete[0], tasks_to_delete[1]):

    r = requests.get(cuckoo_API+'/tasks/delete/'+str(task_id), headers=HEADERS)

    response = r.json()
    print(task_id, response)
