from  sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, 'a')

print "Identify the assets that you bought"
line1 = raw_input("Identify the assets that you bought")
print "Make a note of the reason for the change"
line2 = raw_input("Make a note of the reason for the change")
print "Expectations for the future"
line3 = raw_input("Expecations for the future")

print "I'm going to write these lines to the file."

target.write("First Move")
target.write("\n")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
