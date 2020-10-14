import os
import shutil
import hashlib

root = '../bin/TuTu/benign'
# root = '../asm_final/TuTu/malware'
# root = '../../MTAAV/cnn-img-bytes/data/image64/malware/RGB'

for file in os.listdir(root):
    filepath = root+'/'+file

    file_hash = hashlib.sha256()
    with open(filepath, 'rb') as f:
        fb = f.read()
        file_hash.update(fb)
    hash_val = file_hash.hexdigest()

    # shutil.move(filepath, root+'_/{}__{}'.format(hash_val, file))

    if file[-4:] == '.asm':
        fn = file.split('.asm')[0]
    else:
        fn = file
    print(fn)

    hash = fn.split('__')[0]
    if '__' not in fn:
        print('\t Move')
        shutil.move(root+'/'+file, root+'/'+file+'__')
        continue

    # if hash != hash_val:
    #     shutil.move(root+'/'+file, root+'/'+hash_val+'__'+hash+'.asm')
    #     continue

    # filename = fn.split(hash+'__')[1]
    # # print(file, '~~', filename)
    # if filename == hash:
    #     # print('\t hiu')
    #     shutil.move(root+'/'+file, root+'/'+hash+'__.asm')