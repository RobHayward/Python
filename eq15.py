# import argument variables from the system
from sys import argv
# the argument variable is called filename
script, filename = argv
# open the file that  has been named, 
txt = open(filename)
# print the filename
print "Here's your file %r:" % filename
# pring what is in the text. 
print txt.read()
# Ask for the file name
print "Type the filenme again:"
# raw_input
file_again = raw_input("> ")
# open the file that has been allocated to file_again
txt_again = open(file_again)
# print the contents of the file. 
print txt_again.read()


