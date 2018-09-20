import glob
import subprocess

for file_name in glob.glob('[0-9][0-9].py'):
    subprocess.call(['python', file_name])
