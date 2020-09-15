import os
import shutil

for setname in ['train', 'test']:
    with open('{}_list.txt'.format(setname), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            lbl = line.split('__')[0]
            name = line.split('__')[1].split('.')[0]
            print('name', name, lbl)
            shutil.copy('/media/fitmta/Storage/MinhTu/prep_data/asm_final/{}/{}.asm'.format(lbl, name), '/media/fitmta/Storage/MinhTu/VAE/assembly/data/asm_final/{}/{}/{}.asm'.format(setname, lbl, name))                