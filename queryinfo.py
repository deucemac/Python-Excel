import census2010

brooklyn_pop = census2010.allData['NY']['Kings']['pop']
print('The population of Brookly in 2010 was ' + str(brooklyn_pop) + ' .')

fayette_county_pop = census2010.allData['GA']['Fayette']['pop']
print('The population of Fayette County(my home county) in 2010 was ' + str(fayette_county_pop) + ' .')
# Find population sum of a particular state




# def total_state_pop():
#   sum = 0
#   for i in census2010.allData['GA']:
#     sum = int(i['pop']) + sum
#   return sum
def total_state_pop(state):
  sum = 0
  for i in census2010.allData[state]:
    for x in census2010.allData[state][i]:
      pop = census2010.allData[state][i]['pop']
      sum = sum + pop
  return sum


new_york_pop = str(total_state_pop('NY'))
north_dakota_pop = str(total_state_pop('ND'))
print('The population of NY is ' + new_york_pop + ', but the population of North Dakota is only ' + north_dakota_pop)

