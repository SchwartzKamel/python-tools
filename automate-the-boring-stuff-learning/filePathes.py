import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

print(os.sep)

print(os.getcwd)

os.path.abspath('file.png') # absolute file path of the file, can convert a relative file path to an absolute one

os.path.isabs('c:\\folder\\folder') # checks if the path is absolute or relative in a true\false manner

os.path.relpath('c:\\folder1\\folder2\\folder3\\file.png', 'c:\\folder1') # gives relative path from whatever starting point you specify

os.path.dirname('c:\\folder1\\folder2\\file.png') # outputs the directory path

os.path.basename('c:\\folder1\\folder2\\file.png') # outputs the file name

os.path.basename('c:\\folder1\\folder2') # outputs the name of 'folder2'

os.path.exists('c:\\folder1\\folder2\\spam.png') # outputs whether or not a file path is present on the host

os.path.isfile() # checks if the path is a file or not
os.path.isdir() # checks if the path is a directory or not

