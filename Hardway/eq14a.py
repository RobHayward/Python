from sys import argv

date, user_name = argv
prompt = '>'

print "The date was %s" % (user_name, script)
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """

Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice. 
""" % (likes, lives, computer)
