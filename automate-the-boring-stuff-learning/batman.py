import re

# This matches either statement, the '?' allows for the term 'Batman' and 'Batwoman'
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

# This matches all statements, and as many uses of the 'wo' in woman before man. I.e 'wowowowoman'
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowowowowowoman')
print(mo.group())

# This requires the 'wo' to be present at least once or many times. 
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowowowowowoman')
print(mo.group())

# Put it all together
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())
regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*?+*?+*? regex syntax')
print(mo.group())

# {} is for number of occurances to check for
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

# matches 3 of the complicated patern 
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())

# checks for between 3 and 5 (min and max # of repetitions)
# if there are more than 5, it will only match the first 5 instances
# {3,} is for 3 or more
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

# by default Python will try to match the longest string that matches the pattern. AKA 'greedy matching'
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())

# non-greedy matching requires the '?' after the {}, this matches the smallest possible
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())

