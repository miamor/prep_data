import os
import shutil


root = '../../MTAAV/cnn-img-bytes/data/image64'

for type in ['L', 'RGB']:
	for file in os.listdir(root+'/benign/'+type):
		fn = os.path.splitext(file)[0]

		if os.path.exists('../bin/TuTu/malware/'+fn):
			shutil.move(root+'/benign/'+type+'/'+file, root+'/malware/'+type+'/'+file)
		elif not os.path.exists('../bin/TuTu/benign/'+fn):
			shutil.move(root+'/benign/'+type+'/'+file, root+'/__/'+type+'/'+file)