#! python3
import csv
outputFile = open('example.csv', 'a')
csvWriter = csv.writer(outputFile)
print('write')
eggs = input()
print('write')
bacon = input()
print('write')
ham = input()
csvWriter.writerow([eggs, bacon, ham])
csvWriter.writerow([spam, bacon, ham])
outputFile.close()

