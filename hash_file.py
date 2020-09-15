import hashlib
import os
import shutil

path = '/media/tunguyen/Devs/MtaAV_stuff/exe_thang5/binary'
path = '/media/tunguyen/TuTu_Passport/MTAAV_data/bin/game_Linh'
report_dir = '/media/tunguyen/TuTu_Passport/MTAAV_data/data_report/benign_635/benign'
BLOCK_SIZE = 65536 # The size of each read from the file

ar = []

for filename in os.listdir(path):
    # realname = filename.split('__')[2]
    realname = filename

    file = os.path.join(path, filename) # Location of the file (can be set a different way)

    file_hash = hashlib.sha1() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        # fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        # while len(fb) > 0: # While there is still data being read from the file
        #     file_hash.update(fb) # Update the hash
        #     fb = f.read(BLOCK_SIZE) # Read the next block from the file
        fb = f.read()
        file_hash.update(fb)

    hash_val = file_hash.hexdigest()

    # print('file_hash', hash_val) # Get the hexadecimal digest of the hash
    # os.rename(file, os.path.join(path, '{}__{}'.format(hash_val, realname)))

    # find in report folder
    report_path = '{}/{}.json'.format(report_dir, hash_val)
    print('report_path', report_path)
    if os.path.exists(report_path):
        shutil.copy(report_path, report_path.replace('benign_635', 'game_Linh'))

    # ar.append('{} @ {}'.format(filename, hash_val))

# with open('map_filename_hash.txt', 'w') as f:
#     f.write('\n'.join(ar))



