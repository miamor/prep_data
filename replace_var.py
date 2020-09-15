import os
import re

root = '../asm_cleaned'

p = re.compile(r'((0x|fcn\.|arg\_|var\_)([0-9a-z]{1,8}))')

for dirname in os.listdir(root):
    dir = os.path.join(root, dirname)

    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)

        cleaned = []
        with open(filepath, 'r') as fo:
            lines = fo.readlines()

            for line in lines:
                s = ' '.join((line).split()).strip().replace('int3', 'int')

                for x in re.finditer(p, s):
                    s = s.replace(x.group(), 'var')
                # print('s', s)

                cleaned.append(s)

        with open('../asm_final/{}/{}'.format(dirname, file), 'w') as fw:
            fw.write(' . '.join(cleaned))



s = 'mov eax, dword [0x462730] '
s = 'mov eax, 0x46095c [0x462730] call fcn.0100e11a'

for x in re.finditer(p, s):
    print('x', x.group(1))
    s = s.replace(x.group(), 'var')
print('s', s)

# # m = p.findall(s)           # Run a regex search anywhere inside a string
# # if m:                     # If there is a match
# #     print('hiu', m)
# #     # print(m.group(2))     # Print Group 1 value
