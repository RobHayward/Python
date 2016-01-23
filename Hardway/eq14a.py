from sys import argv

date, hour = argv
prompt = '>'

print "The date was %s. The time was %s" % (date, hour)
print "The time is" % hour
print "What time did it take?"
time = raw_input(prompt)

print "Any notes to add?"
notes = raw_input(prompt)


