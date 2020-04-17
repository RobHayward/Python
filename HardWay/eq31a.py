print "There is an opportunity to develop a new financial product.  Do  you say 'yes' (#1) or 'no# (#2)?"

finprod = raw_input("> ")

if finprod == "1":
	print "The product is succcessful, the bank makes lots of money and you get a large bonus.  Now you..."
	print "1. Expand production"
	print "2. Look for other products"
	
	prod = raw_input(">")
	
	if prod == "1":
		print "Risk increases and you put the bank at risk from bad loans"
	elif prod == "2":
		print "The search is successful and you move into new prpducs"
	else:
		print "You cannot make up your mind.  The value of your option is %s" % 100

elif finprod == "2":
	print "Keep doing wht you are doing, but"
	print "1. Try to increase lending" 
	print "2. Continue to look for other products"
	print "3. Retrench and increase capital"

	insanity = raw_input(">")

	if insanity == "1" or insanity == "2":
		print "There is an economic downturn.  Bad loans increase and capital is scarce"
	else: 
		print "You have protection against the downturn and are ready to pick up weak banks that are in trouble"
	
