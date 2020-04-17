import webbrowser, sys, pyperclip
sys.argv #

# check if command line arguments are passsed
if len(argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])  # from first slice to the end
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>

webbrowser.open('https://www.google.com/maps/place/' + address)


  
