import os
import re


# p = re.compile(r'(.*)(\||\\|\<|\>)\s*(.*)')
p = re.compile(r'(.*)(\||\│|\╎|\└|\\|\<|\>)\s(.*)')

root = '../asm_raw'

for dirname in os.listdir(root):
    dir = os.path.join(root, dirname)

    for file in os.listdir(dir):
        filepath = os.path.join(dir, file)

        cleaned = []
        with open(filepath, 'r') as fo:
            lines = fo.readlines()
            for line in lines:
                line = ' '.join((line).split()).strip()
                # print('line[0]', line[0])
                if line[0] not in ['/', ';']:
                    # cleaned.append(line)

                    # line = line.replace('|')[1].strip()
                    m = p.search(line)
                    if m:
                        lin = m.group(3)
                        # print('\tm', m)
                        # if len(m) > 1:
                        #     line = m[1]
                        # else:
                        #     line = m[0]
                        #     print('***********', line)
                    else:
                        lin = line
                    # print('line[0]', line[0])
                    # print('\tlin', lin)
                    if lin[0] not in ['-', ';', '┌']:
                        lin = lin.split(';')[0]
                        
                        if lin[:2] == '0x':
                            spl = lin.split(' ')
                            lin = ' '.join(spl[2:])

                        cleaned.append(lin)
                    # elif lin[0] in ['┌']:
                    #     lin = lin.split(':')[1].split(';')[0].strip()
                    #     cleaned.append(lin)

        # print('* cleaned\n', '\n'.join(cleaned))
        with open('../asm_cleaned/{}/{}'.format(dirname, file), 'w') as fw:
            fw.write('\n'.join(cleaned))


# p = re.compile(r'(.*)(\||\│|\\|\<|\>)\s(.*)')
# s = "| 0x0040109c 66894767 mov word [edi + 0x67], ax"
# s = "\ 0x00401056 c3 ret"

# s = "││ 0x0041c100 97 xchg eax, edi"
# m = p.search(s)           # Run a regex search anywhere inside a string
# if m:                     # If there is a match
#     print('hiu', m)
#     print(m.group(3))     # Print Group 1 value

# line = '; XREFS: CALL 0x004012b7 CALL 0x004012c0'
# if line[0] not in [';']:
#     print('hihi')