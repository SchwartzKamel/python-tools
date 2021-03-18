import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
# find and replace Agent name to REDACTED
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob.'))
# returns just the first letter of the Agent name
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
# find and replace Agent name with Agent *first letter of name*
print(namesRegex.sub(r'Agent \1','Agent Alice gave the secret documents to Agent Bob.'))

phoneRegex = re.compile(r'''
    (\d\d\d-) |    # area code (without parens, with dash)
    (\ (\d\d\d) )  # -or- area code with parens and no dash
    -         # first dash
    \d\d\d    # first 3 digits
    -         # second dash
    \d\d\d\d  # last 4 digits
    \sx\d{2,4} # extension, like x1234
    ''', re.IGNORECASE | re.DOTALL | re.VERBOSE) # | is known as 'bitwise' for regex only, can pass multiple re.blah args for the re.compile

