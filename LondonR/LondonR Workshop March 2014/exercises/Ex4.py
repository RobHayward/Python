
# Read in data 
filepath = "Change me to point to location of data folder"
input_file = open(filepath + "/Oxford.txt", 'rb')

# Initialise data structure
# A dictionary of lists, one for each column.
fields = ['year', 'month', 'tmax', 'tmin', 'af', 'rain', 'sun', 'comments']
D = {}
for f in fields:
    D[f] = []

for line in input_file:
    if line.startswith(' '):
        # Line is header or data
        line = line.strip()
        if line.startswith('yyyy'):
            # Line is header, store and add a comment column
            header = line.split() + ['comment']
        elif line.startswith('degC'):
            # Line is units of header, disregard for now
            continue 
        else:
            # Line is data
                
            #
            # Your Code goes Here
            #
