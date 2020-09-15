import os
import requests
import random

ips = ['192.168.147.085', '192.168.147.023', '192.168.147.072', '192.168.147.011', '192.168.147.014', '192.168.147.116', 
        '192.168.126.016', '192.168.126.029', '192.168.126.075']

host = '192.168.126.26'
port = 5002

SUBMIT_URL = 'http://{}:{}/api/v1/capture/check'.format(host, port)

# BIN_ROOT = '/home/mtaav/Desktop/old_uploads/'
BIN_ROOT = '/media/tunguyen/TuTu_Passport/MTAAV_data/old_uploads/'
# UPLOAD_DIR = '/home/mtaav/CODE/mta-av-webservice/uploads/'
count = 0


if True:
    for filename in sorted(os.listdir(BIN_ROOT)):
        filepath = BIN_ROOT+filename
        print('** filepath', filepath)

        if count > 1:
            break

        # if os.path.exists(UPLOAD_DIR+filename):
        #     print('\t Skip')
        #     continue

        count += 1

        source_ip = random.choice(ips)
        destination_ip = random.choice(ips)
        while destination_ip == source_ip:
            destination_ip = random.choice(ips)


        with open(filepath, "rb") as sample:
            # print(count, filepath)

            files = {"files[]": sample}
            data = {"source_ip": source_ip, "destination_ip": destination_ip, "protocol": "http"}
            r = requests.post(SUBMIT_URL, files=files, data=data)

            # print('\t', r)
            response = r.json()
            # print('\t Task', response['data'])
            # print('\t Task', response['task_id'])
            print(count, filepath, ' Task', response)
