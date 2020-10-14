import os
import shutil


map_hash_bins = {}
hashes = []
map_hash_bin_selected = {}

for set in ['TuTu_dup', 'TuTu']:
    for file in os.listdir('../bin/'+set+'/benign'):
        hash = file.split('__')[0]
        name = file.split('__')[1]
        if hash not in map_hash_bins:
            map_hash_bins[hash] = [file]
        else:
            map_hash_bins[hash].append(file)
# print('map_hash_bins', map_hash_bins)

new_list = {
    'train': [],
    'test': []
}
for setname in ['train', 'test']:
    with open('../../MTAAV/TuTu_nosys_'+setname+'_list.txt') as f:
        for line in f.readlines():
            line = line.strip()
            fnr = list(filter(None, line.split('__')))
            fn = '__'.join(fnr[2:])
            # print('fnr', fnr)
            hash = fnr[2]
            name = fnr[3] if len(fnr) > 3 else ''
            if len(fnr) <= 3 and fnr[0] == 'malware':
                fn = fn+'__'
                # print('fn', fn)

            if os.path.exists('../bin/TuTu/benign/'+fn) or os.path.exists('../bin/TuTu/malware/'+fn):
                new_list[setname].append(line)
                continue
            elif fnr[0] == 'benign' and not os.path.exists('../bin/TuTu/benign/'+fn) and hash in map_hash_bins:
                # print(hash, name)
                # check all bin having this hash
                for bin_name in map_hash_bins[hash]:
                    # print('\t bin_name', bin_name)
                    if os.path.exists('../bin/TuTu/benign/'+bin_name):
                        # print('\t\t OK')
                        new_list[setname].append(fnr[0]+'__'+fnr[1]+'__'+bin_name)
            else:
                print(hash, fn, 'not found')

for setname in ['train', 'test']:
    print('len new_list[setname]', setname, len(new_list[setname]))
    with open('../../MTAAV/TuTu_nosys_'+setname+'_list.txt', 'w') as f:
        f.write('\n'.join(new_list[setname]))