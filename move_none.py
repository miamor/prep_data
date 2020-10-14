import os
import shutil
import hashlib
import time
from multiprocessing import Pool

__THREADS_NUM__ = 16


none_full_root = '../bin/none_full'


def check_bin(filename):
    file = os.path.join(none_full_root, filename) # Location of the file (can be set a different way)
    # print(filename, file)

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read()
        file_hash.update(fb)

    hash_val = file_hash.hexdigest()

    # find in old none (635) folder
    print(filename, hash_val)
    # old_none_path = '../bin/none/'+hash_val
    # if not os.path.exists(old_none_path):
    #     if not os.path.exists('../bin/none_new/'+filename+'__'+hash_val):
    #         shutil.copy(none_full_root+'/'+filename, '../bin/none_new/'+filename+'__'+hash_val)
    if os.path.exists('../bin/none_old/'+hash_val):
        print('\t Existed')
        shutil.copy(none_full_root+'/'+filename, '../bin/none/'+filename+'__'+hash_val)

# def check_bin(filename):
#     file = os.path.join(none_full_root, filename) # Location of the file (can be set a different way)
#     # print(filename, file)

#     file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
#     with open(file, 'rb') as f: # Open the file to read it's bytes
#         fb = f.read()
#         file_hash.update(fb)

#     hash_val = file_hash.hexdigest()

#     # find in old none (635) folder
#     old_none_path = '../bin/none/'+hash_val
#     if os.path.exists(old_none_path):
#         print('old_none_path', old_none_path)
#         if os.path.exists('../bin/none_new/'+filename+'__'+hash_val):
#             os.remove('../bin/none_new/'+filename+'__'+hash_val)


files = os.listdir(none_full_root)

p = Pool(__THREADS_NUM__)
p.map(check_bin, files)
