import os
import requests

host = '192.168.126.26'
port = 5002
cuckoo_API = 'http://'+host+':1337'
cuckoo_SECRET_KEY = "Bearer RALTrRjHNT21MZdDCksugg"
cuckoo_timeout = 90

REST_URL = cuckoo_API+"/tasks/create/file"
HEADERS = {"Authorization": cuckoo_SECRET_KEY}

SUBMIT_URL = 'http://{}:{}/api/v1/capture/gen_report'.format(host, port)

BIN_ROOT = '../../MTAAV_data/bin'
count = 0


files = ['007b3fad8b53c10b6a9c87a956ca035f1f8cf882e95ffd798343969665382b9e']

FROM_DIR = True



# 06.09.20
# BIN_ROOT+'TuTu/benign' contains 643 benign files 
# (from new_a_Dung/benign + game_Linh + gametop + miniclip)
if FROM_DIR:

    files_to_skip = []
    # with open('data_pickle/done.txt', 'r') as f:
    #     for line in f.readlines():
    #         filename = line.split(' ')[1].split('/')[-1]
    #         files_to_skip.append(filename)


    for filename in os.listdir(BIN_ROOT+'/none_new'):
        if filename in files_to_skip:
            continue
        
        # if count > 0:
        #     continue

        count += 1

        filepath = BIN_ROOT+'/none_new/'+filename

        with open(filepath, "rb") as sample:
        # if True:
            print(count, filepath)

            files = {"file": sample}
            data = {"enforce_timeout": True, "timeout": cuckoo_timeout}
            r = requests.post(REST_URL, headers=HEADERS, files=files, data=data)

            # files = {"files[]": open(filepath, "rb")}
            # r = requests.post(SUBMIT_URL, files=files)

            # print('\t', r)
            response = r.json()
            # print('\t Task', response['data'])
            print('\t Task', response['task_id'])
            # print(count, filepath, ' Task', response['task_id'])

else:

    for filename in files:
        count += 1
        filepath = BIN_ROOT+'/TuTu/benign/'+filename

        with open(filepath, "rb") as sample:
            # print(count, filepath)

            files = {"file": sample}
            data = {"enforce_timeout": True, "timeout": cuckoo_timeout}
            r = requests.post(REST_URL, headers=HEADERS, files=files, data=data)

            # files = {"files[]": sample}
            # r = requests.post(SUBMIT_URL, files=files)

            # print('\t', r)
            response = r.json()
            # print('\t Task', response['data'])
            # print('\t Task', response['task_id'])
            print(count, filepath, ' Task', response['task_id'])


