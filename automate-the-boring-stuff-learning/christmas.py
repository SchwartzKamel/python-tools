import re

lyrics = '12 drummers drumming,11 pipers piping,10 lords a leaping,9 ladies dancing,8 maids a milking,7 swans a swimming,6 geese a laying,5 golden rings,4 calling birds,3 french hens,2 turtle doves,and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# regex matches only vowels
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.'))
# matches only vowels next to one another
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.'))
# matches all characters EXCEPT for vowels
consonantesRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantesRegex.findall('Robocop eats baby food.'))