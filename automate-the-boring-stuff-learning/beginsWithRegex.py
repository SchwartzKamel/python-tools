import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"') == None)

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!srhsasiasdoas') == None)

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('234567876543456789'))
print(allDigitsRegex.search('6789766789x789076789') == None)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

serve = '<To serve humans> for dinner.>'

nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
print(prime)
# re.DOTALL catches new lines
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))
# re.I means case insensitive
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))
