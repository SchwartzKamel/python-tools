import webbrowser, sys, pyperclip

sys.argv # ['mapIt.py', '870', 'Valencia', 'St.']

# Check if commadn line arguments were passed
if len(sys.argv) > 1:
    # ['mapIt.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)