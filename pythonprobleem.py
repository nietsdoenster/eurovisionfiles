import csv
with open('results2016firstedit.csv', 'r') as csvfile:
	results = []
	countries = []
	datareader = csv.reader(csvfile)
	my_list = list(datareader)
	for row in my_list:
		results.append(row[1])
		countries.append(row[0])
csvfile.close()

results1 = []
for result in results:
	result = int(result)
	results1.append(result)


teller = 1
count = 0
for country, result in zip(countries,results1):
	if result > count:
		winner = country
		teller += 1
		count = result
	else:
		None

for country, result in zip(countries, results1):
	if result < count:
		loser = country
		teller += 1
		count = result
	else:
		None

print("The winner of Eurovision 2016 is:", winner) 
print("The loser of Eurovision 2016 is:", loser)
# 32 lines of code
#that obviously does not work - winner output should be Ukraine! 

winningcountry = max(my_list,key=lambda item:item[1])
print(winningcountry)

def identity(x):
	return(x)

def winner_of_eurovision(sequence, key_func=None):
	if not sequence:
		raise ValueError('Empty file - or worse - bad code!')

	if not key_func:
		key_func = identity

	maximum = sequence[0]

	for item in sequence:
		if item[1] > maximum[1]:
			maximum = item

	return maximum

def points(x):
	return x[1]

print(winner_of_eurovision(my_list, key_func=points)) #Again, the wrong output. 

def identity(x):
	return(x)

def loser_of_eurovision(sequence, key_func=None):
	if not sequence:
		raise ValueError('Empty file - or worse - bad code!')

	if not key_func:
		key_func = identity

	minimum = sequence[0]

	for item in sequence:
		if item[1] < minimum[1]:
			minimum = item

	return minimum

def points(x):
	return x[1]

print(loser_of_eurovision(my_list, key_func=points)) #Output should be Germany
