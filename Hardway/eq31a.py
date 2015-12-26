print "There is an opportunity to develop a new fisncisl roeuct.  Do  you say 'yes' (#1) or 'no# (#2)?"

finprod = raw_input("> ")

if finprod == "1":
	print "The product is ssucccessful, bank makes lots of money and you get a large bonus"
	print "1. Expand productoin"
	print "2. iStart to look for other products"
	
	prod = raw_input(">")
	
	if prod == "1":
		print "iRisk incresaes and you put the bank at risk from bad loans"
	elif prod == "2":
		print "The search is successful and you move into new prpducs"
	else:
		print "iWell better to %s than anyting else" % bear

elif finprod == "2":
	print "Keep doing wht you are doing, but"
	print "1. Try to increase lending" 
	print "2. Look for other products"
	print "3. You increse cuation nd hold back"

	insanity = raw_input(">")

	if insanity == "1" or insanity == "2":
		print "You over-extend, brea the bank and get sacked!"
	else: 
		print "You hve been successful"
else:
	print "You make a dortune nd  liave happily ever after"
	
