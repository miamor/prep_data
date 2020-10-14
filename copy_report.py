import os
import re
import shutil
import json

CUCKOO_REPORT_ROOT = '/home/mtaav/.cuckoo/storage/analyses/'
NEW_REPORT_DIR = '/media/tunguyen/TuTu_Passport/MTAAV_data/data_report/TuTu_all/benign'

REPORT_IDS = range(5703, 6201) # benign_uploads

pattern = r'"([A-Za-z0-9_\./\\-]*)"'

def copy_reports():
    for report_id in REPORT_IDS:
        report_path = CUCKOO_REPORT_ROOT+'/{}/reports/report.json'.format(report_id)
        print('* report_path', report_path)

        if not os.path.exists(report_path):
            print('\t Report not found. Skip')
            continue

        with open(report_path, 'r') as f:
            content = json.load(f)['target']['file']
            sha256 = content['sha256']
            fname = content['name']
            if fname == sha256:
                fname = ''

            print('\t sha256', sha256, 'fname', fname)
        
        filepath = NEW_REPORT_DIR+'/{}__{}__{}.json'.format(report_id, sha256, fname)
        print('\t filepath', filepath)

        if os.path.exists(filepath):
            print('\t Report copied. Skip')
            continue
        
        shutil.copy(report_path, filepath)



def remove_dup():
    l = []
    for filename in os.listdir(NEW_REPORT_DIR):
        print('filename', filename)
        sha256 = filename.split('__')[1]
        if sha256 in l:
            print('\t Duplicated')
            shutil.move(NEW_REPORT_DIR+'/'+filename, NEW_REPORT_DIR+'__dup/'+filename)
            l.append(sha256)



# copy_reports()
remove_dup()