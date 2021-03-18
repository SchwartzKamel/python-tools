#commaCodev2
egg = input() #takes raw input as a string
spam = egg.split() #turns that string into a list
print(spam) #prints the list

musubi = (", ".join(spam)) #turns the list into a string where each list value is separated by ", "
print(musubi) #prints the new string