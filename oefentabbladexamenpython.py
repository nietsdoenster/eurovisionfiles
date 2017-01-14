print("===========================")
#printing the countries

import csv
with open('euro2016.csv', 'r') as csvfile:
	results = []
	euroreader = csv.reader(csvfile, delimiter=';')
	for row in euroreader:
		results.append(row)
		print(" ".join(row))
print(results)



westerneurope = ['United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg']
#def count_westerncountries(mylist, westerneurope):
#	count = 0
#	for country in mylist:
#		if country in westerneurope:
#			count += 1
#		return count
#print(count_westerncountries(mylist, westerneurope))

print("===========================")

import csv
with open('euro2016.csv', 'r') as csvfile:
	countries = []
	readFILE = csv.reader(csvfile, delimiter=';')
	for row in readFILE:
		countries.append(row[0])
		#print(row[0])

print(type(countries))
mylist = countries
print(mylist)


def count_westerncountries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg']:
			count +=1
		else:
			None
	return count

print(count_westerncountries(mylist))

def X(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Belgium', 'Netherlands']:
			count +=1
		else:
			None
	return(count)

#def count_westerncountries(tokens):
#	emptylist = []
#	count = 0
#	for token in tokens:
#		if token in ['United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg']:
#			count +=1
#			emptylist = emptylist.append(token)
#			emptylist = len(emptylist)
#			return count

#print(count_westerncountries(mylist))

