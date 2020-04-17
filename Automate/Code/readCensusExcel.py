#! python3
# readCensusExcel.py = Tabulates population and number of census tracts 
# for each county. 

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('../automte_online-materials/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Popultion by Census Tract')
couhnryData ={}


for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

# Make sure the key for this state exists
countryData.setdefault(state, {})
# Make sure the key for this country in this state exists
countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})

# each row represents on census trct so increment by one
countryData[state][county]['tracts'] += 1
# Increase the county pop by the pop in this  census tract
countyData[state][county]['pop'] += int(pop)

# OPen a new text file and write the contents of countyData to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFIle.close()
print('DOne.')




