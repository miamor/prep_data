import r2pipe
import hashlib
import os
import shutil

# root = '../bin/new_a_Dung'
# for dirname in os.listdir(root):

# hashes = []
# for filename in os.listdir('../data_report/TuTu_sm/benign'):
#     hash = filename.split('__')[1]
#     hashes.append(hash)


# for file in os.listdir('../bin/game_Linh'):
#     filepath = os.path.join('../bin/game_Linh', file)

#     file_hash = hashlib.sha256()
#     with open(filepath, 'rb') as f:
#         fb = f.read()
#         file_hash.update(fb)
#     hash_val = file_hash.hexdigest()

#     print(filepath, hash_val)

#     if hash_val not in hashes:
#         print('Not in dataset. Skip.')
#         continue

#     shutil.move(filepath, '../bin/TuTu_sm/benign/'+file)


root = '../bin'
dirname = 'TuTu/benign'
if True:
    dir = os.path.join(root, dirname)

    if not os.path.exists('../asm_raw/'+dirname):
        os.makedirs('../asm_raw/'+dirname)
    if not os.path.exists('../asm_cleaned/'+dirname):
        os.makedirs('../asm_cleaned/'+dirname)
    if not os.path.exists('../asm_final/'+dirname):
        os.makedirs('../asm_final/'+dirname)
    if not os.path.exists('../dot/'+dirname):
        os.makedirs('../dot/'+dirname)

    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)

        if os.path.exists('../asm_raw/{}/{}.asm'.format(dirname, file)):
            print(filepath, 'processed. Skip.')
            continue

        print('processing', filepath)

        r = r2pipe.open(filepath)
        # print('\t aaa')
        # r.cmd('aaa')
        # print('\t agC > dot/{}/{}.dot'.format(dirname, file))
        # og = r.cmd('agC > dot/{}/{}.dot'.format(dirname, file))
        # print('\t agC', og)

        print('\t pd > ../asm_raw/{}/{}.asm'.format(dirname, file))
        od = r.cmd('pd > ../asm_raw/{}/{}.asm'.format(dirname, file))
        # print('pd', od)




# set = 'TuTu_nosys'
# files = []
# for setname in ['train', 'test']:
#     print('../../MTAAV/'+set+'_'+setname+'_list.txt')
#     with open('../../MTAAV/'+set+'_'+setname+'_list.txt') as f:
#         for line in f.readlines():
#             fnr = list(filter(None, line.strip().split('__')))
#             fn = '__'.join(fnr[2:])
#             print(line, fn)
#             files.append(fn)

# print('files', len(files))

# n = 0
# for lbl in ['benign', 'malware']:
#     dir = '../bin/TuTu/'+lbl

#     if not os.path.exists('../asm_raw/'+set+'/'+lbl):
#         os.makedirs('../asm_raw/'+set+'/'+lbl)
#     if not os.path.exists('../asm_cleaned/'+set+'/'+lbl):
#         os.makedirs('../asm_cleaned/'+set+'/'+lbl)
#     if not os.path.exists('../asm_final/'+set+'/'+lbl):
#         os.makedirs('../asm_final/'+set+'/'+lbl)
#     # if not os.path.exists('../dot/'+set+'/'+lbl):
#     #     os.makedirs('../dot/'+set+'/'+lbl)

#     for file in os.listdir(dir):
#         if lbl == 'benign' and len(list(filter(None, file.split('__')))) < 2:
#             continue

#         if file not in files:
#             print(dir+'/'+file, 'not in SET. Skip.')
#             continue

#         filepath = os.path.join(dir, file)
#         n += 1

#         if os.path.exists('../asm_raw/{}/{}.asm'.format(set+'/'+lbl, file)):
#             # print(filepath, 'processed. Skip.')
#             continue

#         print('processing', filepath)

#         shutil.copy('../asm_raw/{}/{}.asm'.format('TuTu/'+lbl, file), '../asm_raw/{}/{}.asm'.format(set+'/'+lbl, file))
#         shutil.copy('../asm_cleaned/{}/{}.asm'.format('TuTu/'+lbl, file), '../asm_cleaned/{}/{}.asm'.format(set+'/'+lbl, file))
#         shutil.copy('../asm_final/{}/{}.asm'.format('TuTu/'+lbl, file), '../asm_final/{}/{}.asm'.format(set+'/'+lbl, file))

#         # r = r2pipe.open(filepath)
#         # # print('\t aaa')
#         # # r.cmd('aaa')
#         # # print('\t agC > dot/{}/{}.dot'.format(dirname, file))
#         # # og = r.cmd('agC > dot/{}/{}.dot'.format(dirname, file))
#         # # print('\t agC', og)

#         # print('\t pd > ../asm_raw/{}/{}.asm'.format(set+'/'+lbl, file))
#         # od = r.cmd('pd > ../asm_raw/{}/{}.asm'.format(set+'/'+lbl, file))
#         # print('pd', od)

# print('n', n)