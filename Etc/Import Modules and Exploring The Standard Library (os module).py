# Here we will import my_module that we created in another file.

import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']
# To use the find_index function in my_module
index = my_module.find_index(courses, 'Math')
print(index)

# We can also write 'import my_module as mm'. then we can write my_module as mm in the code.
# Ex: index = mm.find_index(courses, 'Math')

# Importing function or any other thing(ex: a string) from a module:
from my_module import find_index, test
index2 = find_index(courses, 'History')
print(index2)
print(test)

# Import Everything: Usually never used cuz it makes it harder to track problems.
from my_module import *

# Where does python look for the modules when we import them? we can see the paths by:

import sys
print(sys.path)

# What if our module is somewhere like in the desktop
# One way:
# We can add the directory of our module to sys.path, run print(sys.path and you will see this Desktop location added in the end of it means it will also search the desktop for out module)
import sys
sys.path.append('/Users/SicParvisMagna/Desktop')    # Location where the module is.
import my_module
print(sys.path)
# Another way :
# An environment variable is a dynamic "object" on a computer, containing an editable value, which may be used by one or more software programs in Windows. Environment variables help programs know what directory to install files in, where to store temporary files, and where to find user profile settings. They help shape the environment in which programs run on your computer.
# We can change the next place in which sys.path looks for our module that we import. i.e. the python path environment variable. We can do this in terminal for mac: SEE Corey Schafer Python Tutorial 9

# USING STANDARD LIBRARIES
# Random module
import random
random_course = random.choice(courses)
print(random_course)

import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
date_today = datetime.date.today()
print(date_today)
print(calendar.isleap(2017))

# OS Module: Gives acces to the underlying operating system
import os
print(os.getcwd())  # Print which directory we are currently working in, cwd = current working directory

# These modules are just python files and we can see their location by:
print(os.__file__)

print(dir(os))  # Shows methods available in the module os
os.chdir('/Users/SicParvisMagna/OneDrive/Documents')    # Changes current working directory
print(os.getcwd())
# Now to see what files and folder are there in the above changed new path
print(os.listdir())

os.chdir('/Users/SicParvisMagna/OneDrive/Documents/Python programs/PyCharm/Tutorials')
print(os.getcwd())

# Creating new folder in the cwd
os.mkdir('OS_Demo')
# OR
os.makedirs('OS_Demo/Sub_dir')  # Use this to create a directory which is a few level deep.

# Deleting Folders
os.rmdir('OS_Demo/Sub_dir')     # Will not remove intermediate directory i.e. OS_Demo
os.removedirs('OS_Demo/Sub_dir')
os.rename('text.txt', 'demo.txt')   # Rename text.txt to demo.txt

# Printing info about files
print(os.stat('demo.txt'))  # Can display specific info from these like:
print(os.stat('demo.txt').st_mtime)  # Will show last date the file was modified
from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))     # Shows time that we can read

# To see the entire directory tree and files use os.walk function
# It will print 3 valued tuples containing the path, the directories and the files within the directories (folders)
# It will be a tuple that's why we can use for loop:
for dirpath, dirnames, filenames in os.walk('/Users/SicParvisMagna/Documents'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)    # Folders
    print('Files: ', filenames)

# getting Environment variables
print(os.environ.get('HOME'))   # Home environment variable i.e. User's Home Directory
# Joining paths
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')  # Will join the two paths 'HOME' and 'text.txt'. Will not create new file.
print(file_path)

# Doesnt have to be a real path
print(os.path.basename('/tmp/test.txt'))    # Will just show which is the file name in the path we have provided.
print(os.path.dirname('/tmp/test.txt'))     # Will show directory
print(os.path.split('/tmp/test.txt'))       # Will show both
print(os.path.exists('/tmp/test.txt'))       # Will show if the path exists or not
# To check is it is a directory or a file
print(os.path.isdir('/tmp/vgyhbn'))
print(os.path.isfile('/tmp/abcabc'))
print(os.path.splitext('/tmp/test.txt'))       # it will split the file root and extension or The root of the path in the extension.
print(dir(os.path))  # Shows all the path functions available
