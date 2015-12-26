print "You enter a dark room with two doors.  Do you go through the door #1 or do you try door #2"

door = raw_input("> ")

if door == "1":
	print "There is a giant bear here eating a cheese cake. Wht do you do?"
	print "1. Take the cake."
	print "2. Screen the bear."
	
	bear = raw_input(">")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probbly better. Bear runs way." % bear

elif door == "2":
	print "You stare into the endless abyss t Cthunlhu's retina."
	print "1. Bluberries." 
	print "2. Yellow jacket  clothespints."
	print "3. Understanding revolvers yelling memories."

	insanity = raw_input(">")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a amind of jello. Good job!"
	else: 
		print "The insanity rots your eyes into a pool of muck. Good job!"
else:
	print "Your stumble around and fall on a knie and die. Good Job!"
	
