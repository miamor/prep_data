import os
import shutil

bin_root = '../bin/TuTu/'
rp_root = '../data_report/TuTu/'

map_hash_bin = {}

for lbl in ['benign', 'malware']:
	for file in os.listdir(bin_root+lbl):
		fnr = list(filter(None, file[:-5].split('__')))
		# print(fnr)
		hash = fnr[0]
		map_hash_bin[hash] = file[:-5]
	print('map_hash_bin', map_hash_bin)


	for file in os.listdir(rp_root+lbl):
		file = file[:-5]
		fnr = list(filter(None, file.split('__')))
		# print(fnr)
		hash = fnr[1]

		if hash not in map_hash_bin:
			continue

		bin = map_hash_bin[hash]

		fn = '__'.join(fnr[1:])
		# print(file[-2:])
		if file[-2:] == '__':
			fn = fn+'__'
			new_name = file.replace(fn, bin)
			print(fn, new_name)
			shutil.move(rp_root+lbl+'/'+file+'.json', rp_root+lbl+'/'+new_name+'.json')


for l in ['_train', '_test']:
	with open('../../MTAAV/HAN-sec-new/data_pickle/reverse/TuTu__vocabtutu__iapi__tfidf__topk=10_lv=word/graphs_name'+l+'.txt') as f:
		new = []
		for line in f.readlines():
			line = line.strip()[:-5]
			lbl = line.split('__')[0]
			file = line.split(lbl+'__')[1]
			fnr = list(filter(None, file.split('__')))
			# print(fnr)
			hash = fnr[1]

			if hash not in map_hash_bin:
				continue

			bin = map_hash_bin[hash]

			fn = '__'.join(fnr[1:])
			# print(file[-2:])
			if file[-2:] == '__':
				fn = fn+'__'
				new_name = file.replace(fn, bin)
				print(fn, new_name)
				new.append(lbl+'__'+new_name)
			else:
				new.append(line)


	with open('../../MTAAV/HAN-sec-new/data_pickle/reverse/TuTu__vocabtutu__iapi__tfidf__topk=10_lv=word/graphs_name'+l+'_new.txt', 'w') as f:
		f.write('\n'.join(new))