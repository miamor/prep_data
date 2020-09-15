import r2pipe
import os

# root = '../bin/new_a_Dung'
# for dirname in os.listdir(root):

root = '../bin'
dirname = 'game_Linh'
if True:
    dir = os.path.join(root, dirname)

    if not os.path.exists('../asm_raw/'+dirname):
        os.makedirs('../asm_raw/'+dirname)
    if not os.path.exists('../asm_cleaned/'+dirname):
        os.makedirs('../asm_cleaned/'+dirname)
    if not os.path.exists('../dot/'+dirname):
        os.makedirs('../dot/'+dirname)

    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)

        print('processing', filepath)

        if os.path.exists('../asm_raw/{}/{}.asm'.format(dirname, file)):
            continue

        r = r2pipe.open(filepath)
        # print('aaa')
        # r.cmd('aaa')
        # print('agC > dot/{}/{}.dot'.format(dirname, file))
        # og = r.cmd('agC > dot/{}/{}.dot'.format(dirname, file))
        # print('agC', og)

        print('pd > ../asm_raw/{}/{}.asm'.format(dirname, file))
        od = r.cmd('pd > ../asm_raw/{}/{}.asm'.format(dirname, file))
        # print('pd', od)
