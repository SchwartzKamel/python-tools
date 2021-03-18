def eggs(someParameter):
	someParameter.append('Hello') #This will append 'Hello' to the end of the list in spam

spam = [1,2,3]
eggs(spam)
print(spam)