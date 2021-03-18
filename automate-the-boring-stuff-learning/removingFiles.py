import os
import shutil

# delete single file from current working directory
os.unlink('bacon.txt')
# delete directory, must be empty directory
os.rmdir('c:\\delicious')
# remove directory recursively
shutil.rmtree('c:\\delicious')
# install the send2trash module, this sends files to trash can as opposed to deleting the file entirely