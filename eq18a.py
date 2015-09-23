def date(*ar):
	arg1, arg2 = args
        print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that  *args is actully pointless, we can just do this
def prog_time(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def time(arg1):
	print "arg1: %r" % arg1

# this one takes no argument 
def print_none():
	print "Trainingg data."

date("20/01/2015", "10:00")
prog_time("20/01/2015", "5")
time("20:14:00")
print_none()

