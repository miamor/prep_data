import os

files = []
with_bin = 0
for setname in ['train', 'test']:
    with open('../../MTAAV/TuTu_nosys_'+setname+'_list.txt') as f:
        for line in f.readlines():
            fnr = list(filter(None, line.strip().split('__')))
            fn = '__'.join(fnr[2:])
            if len(fnr) <= 3 and fnr[0] == 'malware':
                fn = fn+'__'
                # print('fn', fn)
            if not os.path.exists('../bin/TuTu/benign/'+fn) and not os.path.exists('../bin/TuTu/malware/'+fn):
            	files.append(fn)
            else:
                with_bin += 1
print('with_bin', with_bin)
print('without_bin', len(files))

with open('report_without_bin.txt', 'w') as f:
    f.write('\n'.join(files))



