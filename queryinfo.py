import census2010

brooklyn_pop = census2010.allData['NY']['Kings']['pop']
print('The population of Brookly in 2010 was ' + str(brooklyn_pop) + ' .')

fayette_county_pop = census2010.allData['GA']['Fayette']['pop']
print('The population of Fayette County(my home county) in 2010 was ' + str(fayette_county_pop) + ' .')
# Find population sum of a particular state
for i in census2010.allData['GA']:
  sum = 0
  i['']
