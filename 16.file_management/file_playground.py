import os
import shutil
from glob import iglob
from pathlib import Path


# os way
os.makedirs('os_folder')
shutil.copy('Lord_of_a_Thousand_Suns.txt', 'os_folder')
# I'm copying instead of removing, so I will not lose the file when I'll delete the folder

for path in iglob('../test/*'):
    shutil.copy(path, 'os_folder')
os.rename('os_folder/Lord_of_a_Thousand_Suns.txt', 'os_folder/Lord_of_a_Thousand_Daughters.txt')
# Oh, it's not Sons, nevermind.

for path in iglob('os_folder/*'):
    os.remove(path)
os.rmdir('os_folder')


# pathlib way
p = Path('pathlib_dir')
p.mkdir()
shutil.copy('Lord_of_a_Thousand_Suns.txt', 'pathlib_dir')
for path in iglob('../test/*'):
    shutil.copy(path, 'pathlib_dir')
Path('pathlib_dir/bubble_sort.py').rename('pathlib_dir/monkey_sort.py')
shutil.rmtree('pathlib_dir')
