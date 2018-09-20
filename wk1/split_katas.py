import glob
import os

for existing_file in glob.glob('[0-9][0-9].py'):
    os.remove(existing_file)

with open('all_katas.py') as input_file:
    contents = input_file.read()
    katas = contents.split('\n\n\n')
    for i, kata in enumerate(katas):
        file_name = str(i + 1).zfill(2) + '.py'
        open(file_name, 'w').write(kata.strip() + '\n')
