import shutil

# copies the file to the new location
shutil.copy('c:\\file.txt', 'c:\\delicious')
# copies and renames file to new location
shutil.copy('c:\\file.txt', 'c:\\delicious\\filefilefile.txt')
# copies recursively from directory
shutil.copytree('c:\\delicious', 'c:\\delicious_backup')
# moves file to new location
shutil.move('c:\\file.txt', 'c:\\delicious\\walnut')
# rename works the same as bash, move file to same directory but with a new name
shutil.move('c:\\delicious\\walnut\\file.txt', 'c:\\delicious\\walnut\\document.txt')