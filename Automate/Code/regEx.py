import re 

message = 'call me 415-555-1011 tomorrow, or at 415-555-999.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#\r is a raw string, \d is a digit
mo = phoneNumRegex.search(message)
#search method
# matched object
print(mo.group())
# group will display the text
# alternatively, just post the text where 'message' is.
# the finalall method will find all cases of the regular expression
# This will return a list of strings. 
