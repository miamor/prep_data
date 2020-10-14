import os
import shutil

mal_names = os.listdir('../bin/new_a_Dung/malware') + os.listdir('../bin/none') + os.listdir('../bin/none_new')

for filename in sorted(os.listdir('../data_report/TuTu/benign')):
    sha256 = filename.split('__')[1]
    if sha256 in mal_names:
        shutil.move('../data_report/TuTu/'+filename, '../data_report/TuTu_all/benign_wrong/'+filename)