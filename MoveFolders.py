import os
import re
import shutil
os.system('cls')
root_dir = 'p:\\'
d_pattern = re.compile(r'^(\d{4})-\d{2}-\d{2}$')

for folder in os.listdir(root_dir):
    fullPath = os.path.join(root_dir,folder)
    match = d_pattern.match(folder)
    if match:
        year = folder.split('-')[0]
        yPath = os.path.join(root_dir, year)
            
        if not os.path.exists(yPath):
            os.makedirs(yPath)

        newPath = os.path.join(yPath,folder)
        dest = newPath
        cnt = 1
        while os.path.exists(dest):
            dest = os.path.join(yPath,f"{folder}_{cnt}")
            cnt +=1
        shutil.move(fullPath, dest)
        print(f"{yPath, dest}")
