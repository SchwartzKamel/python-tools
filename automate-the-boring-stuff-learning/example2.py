print('How many cats do you have?')
numCats = input()
try:
	if int(numCats) >= 4:
		print('That is a lot of cats.')
	if int(numCats) == 0:
		print('You do not have any cats.')
	if int(numCats) < 0:
		print('You cannot have negative cats.')
	else:
		print('That is not many cats.')
except ValueError:
	print('You did not enter a number.')