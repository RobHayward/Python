# This is an exercise to try to prepare for training data
print "Date?", 
Date = raw_input()
print "Time?", 
Time = raw_input()
print "Programme?",
Programme = int(raw_input())
print "Calories?",
Calories = float(raw_input())
print "Time taken?", 
Time_taken = float(raw_input())

print "Date, %r, Time, %r, Programme, %r, Calories, %r, Time_taken, %r, Calories per minute %r" % (Date, Time, Programme, Calories, Time_taken, Calories/Time_taken)
