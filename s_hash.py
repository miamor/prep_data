import hashlib
import os
import shutil

root = '../bin/TuTu/benign/'


# for file in os.listdir(root):
#     file_hash = hashlib.sha256()
#     with open(root+file, 'rb') as f:
#         fb = f.read()
#         file_hash.update(fb)
#     hash_val = file_hash.hexdigest()
#     # print(file, '\t hash_val', hash_val)
#     fnr = list(filter(None, file.split('__')))
#     if len(fnr) > 1:
#     	hash = fnr[0]
#     	if hash_val != hash:
#     		print('different hash')

#     # new_name = hash_val+'__'+file
#     # shutil.move(root+file, '../bin/TuTu/benign/'+new_name)


files = ['4c6b020b32e7fd19196ef8d52949e8312846076903102ddc763ad73c4ccc2335__962dc51f-100a-42a7-9e62-710472b84d01']
for file in files:
    file_hash = hashlib.sha256()
    with open(root+file, 'rb') as f:
        fb = f.read()
        file_hash.update(fb)
    hash_val = file_hash.hexdigest()
    print(file, '\t hash_val', hash_val)
