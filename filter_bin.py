import os
import shutil


# hash_selected = []
# for file in os.listdir('../bin/TuTu/malware__'):
# 	hash_selected.append(file)
# print('hash_selected', hash_selected)

# for file in os.listdir('../bin/none_new'):
# 	hash = file.split('__')[-1]
# 	print('hash', hash)
# 	if hash in hash_selected:
# 		shutil.copy('../bin/none_new/'+file, '../bin/TuTu/malware/'+file)


bins = {
	'benign': [],
	'malware': []
}
for lbl in ['benign','malware']:
	for fn in os.listdir('../bin/TuTu/'+lbl):
		bins[lbl].append(fn.split('__')[0])

for lbl in ['benign']:
	n = 0
	print('bins[lbl]', len(bins[lbl]))
	for file in os.listdir('../data_report/TuTu/'+lbl):
		hash = file[2:].split('__')[1]
		n += 1
		# print(n, 'hash', hash)
		if hash not in bins[lbl]:
			shutil.move('../data_report/TuTu/'+lbl+'/'+file, '../data_report/TuTu_extra/'+lbl+'/'+file)