import os
import random

# How To Run :
# Make sure there is one main folder of FRIENDS containing folders of seasons and NOTHING else.
# Each season folder should ONLY contain video files.
p = '/Users/kunalkushwaha/Desktop/FRIENDS'
os.chdir(p)

folder_name = random.choice(os.listdir(p))

folder_path = str(os.path.realpath(folder_name))
while folder_path == ".DS_Store":
    folder_path = str(os.path.realpath(folder_name))
os.chdir(folder_path)

file_name = random.choice(os.listdir(folder_path))
while file_name == ".DS_Store":
    file_name = random.choice(os.listdir(folder_path))

# print('Playing Episode {} from Season {}\n'.format(file_name[12:14], folder_name))
print("ENJOY!!\n")

os.system("open " + file_name)  # FOR MAC
# os.system("start " + filename)  # FOR WINDOWS
