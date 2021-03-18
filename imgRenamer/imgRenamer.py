# renames all image files in a directory to a number (does not respect order, etc.)
import os
import glob

# gets the path
print('Enter the path of your files.')
fpath = input()
os.chdir(fpath)

index = 0
for f in glob.glob('*.*'):
    filename, file_extension = os.path.splitext(f)
    os.rename(f, str(index) + file_extension)
    index += 1