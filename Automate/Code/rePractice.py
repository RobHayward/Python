import re
message = 'Call me on 415-444-1234 tomorrow or 415-222-1454'
# create re object
#re-compile will define the text that we are looking for
# use the raw strinng funcition so that backslash can be identified
phoneNumrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#the regular expression data type has a resarch method
#create a matched object (this has a method called grouped that returns the
# actual text. 
#mo = phoneNumrex.search(message)
# use phoneNumrex.findall() for all the phone numbers in message.
# mo = phoneNumrex.findall(message)
print(phoneNumrex.findall(message))
