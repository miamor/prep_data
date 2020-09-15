import hashlib
import os

file = '../bin/game_Linh/1.0.154_chromesetup_154_59.exe'
file = '../bin/Microsoft.v4.02.dll'

files = ['../bin/game-remakes/3-Days--Zoo-Mystery', '../bin/game-remakes/10-Days-Under-the-Sea']

for file in files:
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        fb = f.read()
        file_hash.update(fb)
    hash_val = file_hash.hexdigest()
    print(file, '\t hash_val', hash_val)


