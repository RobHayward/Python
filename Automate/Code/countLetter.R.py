# count the number of instances of a letter in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] +1
print(count)
