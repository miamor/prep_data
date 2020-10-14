import os
import shutil

root = '../asm_final/TuTu'

hashes = []
for lbl in ['benign', 'malware']:
	for file in os.listdir(root+'/'+lbl):
		hash = file.split('__')[0]
		print(hash, file)
		if hash not in hashes:
			if os.path.exists('../bin/TuTu/'+lbl+'/'+file.split('.asm')[0]):
				# print('Append hash')
				hashes.append(hash)
		else:
			print('Move dup', root+'/'+lbl+'/'+file)
			shutil.move(root+'/'+lbl+'/'+file, root+'_dup/'+lbl+'/'+file)


# for file in os.listdir('../asm_final/TuTu/benign'):
# 	if not os.path.exists(root+'/benign/'+file):
# 		shutil.move('../asm_final/TuTu/benign/'+file, '../asm_final/TuTu_dup/benign/'+file)


# root = '../bin/TuTu'
# # p = '../../MTAAV/cnn-img-bytes/data/image64'
# p = '../../MTAAV/cnn-img-bytes/data/seq'
# for lbl in ['benign', 'malware']:
# 	# for type in ['L', 'RGB']:
# 	if True:
# 		type = ''
# 		p1 = p+'/'+lbl+'/'+type
# 		p2 = p+'_dup/'+lbl+'/'+type
# 		if not os.path.exists(p2):
# 			os.makedirs(p2)
# 		for file in os.listdir(p1):
# 			file_noext = os.path.splitext(file)[0]
# 			if not os.path.exists(root+'/'+lbl+'/'+file_noext):
# 				shutil.move(p1+'/'+file, p2+'/'+file)