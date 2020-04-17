import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 514-222-2323')
mo.group()
