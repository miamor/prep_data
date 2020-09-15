import os
import shutil

bin_dir = '/media/tunguyen/Devs/MtaAV_stuff/exe_thang5/binary'
rp_dir = '/media/tunguyen/Devs/MtaAV_stuff/data_report/cuckoo_ADung/malware'

rp_files = os.listdir(rp_dir)
print(rp_files)

for bin in os.listdir(bin_dir):
    bin_path = os.path.join(bin_dir, bin)
    hash = bin.split('__')[0]
    
    # print('bin', bin, hash)

    if hash+'.json' in rp_files:
        print('\t found report')
        shutil.copyfile(bin_path, os.path.join(rp_dir, bin))

