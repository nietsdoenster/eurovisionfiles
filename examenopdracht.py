#test round: We will start with a small test, which demonstrates how pyparsing works and how it is useful. 
from pyparsing import Word, Literal, alphas, OneOrMore, Group, Suppress, stringEnd

word = Word( alphas +"'.")
salutation = Group(OneOrMore(word)) 	#Groups the salutation and the greetee nicely, so that both words [Good morning] are displayed between the same brackets
comma = Suppress(Literal(",")) 			#Suppresses the comma in the outcome
greetee = Group(OneOrMore(word))
exclamationmark = Literal("!") | Literal("?")
#OneorMore = the salutation and the greetee can consist of more than one word, this simplification doesn't require that much. 
greeting = salutation + comma + greetee + exclamationmark

tests = ("Hi, man!",
	"Hey, Carl!",
	"Yo, chick!",
	"Good morning, miss Watson!",
	"Good evening, mister!",
	"Waddup, dog!",
	"Hello, mum!",
	"Hello, sir?")

salutations = []
greetees = []
for t in tests:
	salutation, greetee, exclamationmark = greeting.parseString(t)
	salutations.append( ( " ".join(salutation), exclamationmark))
	greetees.append( " ".join(greetee))
	print(salutation, greetee, exclamationmark)

print(salutations)
print(greetees)

#Importing random salutations

print("===========")
import random

str(salutations)
str(greetees)

for i in range(10):
	salutation = random.choice(salutations)
	greetee = random.choice(greetees)
	print(salutation[0], greetee, salutation[1])

import random
for i in range(10):
	print("%s, say '%s' to %s." % ( random.choice( greetees ), "".join(random.choice( salutations )), random.choice(greetees)))
stringEnd #it is important to properly 'close' your parser
print("===========")
#using a csvfile as it is very easy to collect data on these files 
import csv
with open('resulteurovision2016.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	my_list = list(datareader)

csvfile = open('resulteurovision2016.csv', 'r')
text = csvfile.read()
csvfile.close()
eurosong = text.splitlines()

#print(text) just to make sure everything went well: and it luckily did! 
from pyparsing import Word, alphas, OneOrMore, nums, Group, Literal, Suppress, Combine 
#word = Word( alphas +"'.")
word = Word(alphas)
num = Word(nums)
country = OneOrMore(word)
points = Word(nums)
year = Word(nums)
weirdsymbol = Suppress(Literal(";"))
annualscore = country + points + year
annualscore1 = country + weirdsymbol + points + weirdsymbol + year 
country.setParseAction(lambda tokens: " ".join(tokens)) #combines output like 'United' 'Kingdom' into ONE string, more pretty result
points = Word(nums).setParseAction(lambda tokens: int(tokens[0])) #turns the numeric strings into actual integers, but does not seem to work yet
# Because at first I couldn't get the program to properly work, I did a short testround. 
tests2 = """Bulgaria 206 2016
Germany 0 2015
Belgium 500 2016"""# we want to add splitlines to this code: doing the following --> new variable + splitlines()
# ---> 
experiment = tests2.splitlines()

for test in experiment:
	simple_stats = annualscore.parseString(test)
	print(simple_stats.asList()) #--> or
print("Test round gone well, now we will move on to the real file.")

for result in eurosong:
	stats = annualscore1.parseString(result)
	print(stats.asList())

#stringEnd

print("===========")
#printing the countries
import csv
with open('euro2016.csv', 'r') as csvfile:
	countries = []
	readFILE = csv.reader(csvfile, delimiter=';')
	for row in readFILE:
		countries.append(row[0])
mylist = countries

from collections import defaultdict
frequency = defaultdict(int)
for x in mylist:
	frequency[x] +=1
print(frequency)

print("===========")

items = []
for item in mylist:
	if item not in items:
		items.append(item)
for item in sorted(items):
	print(item, mylist.count(item))

print("===========")

num_lines = sum(1 for line in open('euro2016.csv'))
print("The number of entries in the years 2013, 2014, 2015 and 2016 were in total:", num_lines) #number of entries in the years 2015 - 2016 in total 
print("===========")
averageamountcontestants = num_lines / 4
print(averageamountcontestants)

print("===========")
unique_countries = set(countries)
print("The total number of individual UNIQUE contestants is:", len(unique_countries)) 
print("===========")
sorted_unique_countries = sorted(unique_countries) #prints the countries in alphabetical order, pretty
for x in sorted_unique_countries:
	print(sorted_unique_countries.index(x) +1, end=' ')
	print(" ", x)
print("===========")
#How many separate countries did parttake at the eurovision songcontest?
# now we are going to divide the countries into Western Europe, Southern Europe, North Europe, Eastern Europe and 'others'
#count = 1

csvfile = open('euro2016.csv', 'r')
readmyfile = csv.reader(csvfile, delimiter=';')
westerneurope = ('United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg')

def count_westerncountries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg', 'Switzerland', 'Liechtenstein', 'Ireland']:
			count +=1
		else:
			None
	return count

print(count_westerncountries(mylist))
numberofwesteuropeancountries = count_westerncountries(mylist)
print("The number of West European entries, for instance from Germany or Belgium, in the years 2015-2016 -summed up- is:", numberofwesteuropeancountries)

print("===========")

def count_northerncountries(tokens):
	first1 = tokens
	count = 0 	#HUNDRED LINES
	for token in first1:
		if token in ['Norway', 'Sweden', 'Denmark', 'Iceland']:
			count +=1
		else:
			None
	return count

print(count_northerncountries(mylist))
numberofscandinaviancountries = count_northerncountries(mylist)
print("The number of Scandinavian entries, for instance from Norway or Iceland, in the years 2015-2016 -summed up- is:", numberofscandinaviancountries)

print("===========")

def count_southerncountries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Spain', 'Portugal', 'Italy', 'San Marino', 'Andorra', 'Monaco', 'Greece', 'Cyprus', 'Malta']:
			count +=1
		else:
			None
	return count

print(count_southerncountries(mylist))
numberofsoutheuropeancountries = count_southerncountries(mylist)
print("The number of South European entries, for instance Greece and Italy, in the years 2015-2016 -summed up- is:", numberofsoutheuropeancountries)

print("===========")

def count_balticstatesandfinland(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Finland', 'Estonia', 'Latvia', 'Lithuania']:
			count +=1
		else:
			None
	return count

print(count_balticstatesandfinland(mylist))
numberofbalticcountries = count_balticstatesandfinland(mylist)
print("The number of entries from the Baltic States and Finland, in the years 2015-2016 -summed up- is:", numberofbalticcountries)

print("===========")

def count_non_europeancountries(tokens): 
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Australia', 'Georgia', 'Armenia', 'Turkey', 'Azerbaijan', 'Israel']:
			count +=1
		else:
			None
	return count

print(count_non_europeancountries(mylist))
numberofnoneuropeancountries = count_non_europeancountries(mylist)
print("The number of entries from Non-European countries, like Australia or Georgia, in the years 2015-2016 -summed up- is:", numberofnoneuropeancountries)

print("===========")

def count_slavic_countries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Poland', 'Russia', 'Ukraine', 'Czech Republic', 'Belarus', 'Slovakia']:
			count +=1
		else:
			None
	return count

print(count_slavic_countries(mylist))
numberofslaviccountries = count_slavic_countries(mylist)
print("The number of entries from Slavic countries, like Russia and Ukraine, in the years 2015-2016 -summed up- is:", numberofslaviccountries)

print("===========")

def count_southern_slavic_countries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Bosnia and Herzegovina', 'Croatia', 'Serbia', 'Serbia and Montenegro' 'Montenegro', 'Bulgaria', 'Macedonia']:
			count +=1
		else:
			None
	return count

print(count_southern_slavic_countries(mylist))
numberofsouthernslaviccountries = count_southern_slavic_countries(mylist)
print("The number of entries from Southern Slavic countries, like Serbia and Croatia, in the years 2015-2016 -summed up- is:", numberofsouthernslaviccountries)

print("===========")

def count_other_countries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Hungary', 'Albania', 'Moldova', 'Moldavia', 'Romania']:
			count +=1
		else:
			None
	return count

print(count_other_countries(mylist))
numberofothercountries = count_other_countries(mylist)
print("The number of 'odd ones out' (countries that cannot be easily grouped into another categorie) is:", numberofothercountries)

print("===========")

import csv
with open('euro2016.csv', 'r') as csvfile:
	points = []
	readFILE = csv.reader(csvfile, delimiter=';')
	for row in readFILE:
		points.append(row[1])

#pointspercountry = list(zip(countries, points))
#filter = sorted(pointspercountry)

csvfile.close()

import csv
with open('euro2016.csv', 'r') as csvfile:
	years = [0]
	reader = csv.reader(csvfile, delimiter=';')
	for row in reader:
		years.append(row[2]) 
		#print(row[2])
csvfile.close()
separate_years = set(years) 
separate_years.remove(0) #removed an unnecessary zero from the output. I had no idea where the zero came from, but the problem was easily solved this way.
sorted_separate_years = sorted(separate_years)
print("The years that were examined -summed up- are", sorted_separate_years)
year_count = len(separate_years) #Number of years  								
print("The amount of years that have been examined in this study equals the amount:", year_count)

print("===========")

def percentage(part, whole):
	return 100 * float(part)/float(whole)
#Statistics
#percentagewestern = percentage(numberofwesteuropeancountries, num_lines)
#print("The percentage of West-European countries partaking is:", percentagewestern,"%")
percentagewestern = round(percentage(numberofwesteuropeancountries, num_lines), 2) #round(x, 2) --> limiting floats to two decimal points
print("The percentage of West-European countries partaking is:", percentagewestern,"%")
percentagenorthern = round(percentage(numberofscandinaviancountries, num_lines), 2)
print("The percentage of Scandinavian countries partaking is:", percentagenorthern, "%")
percentagesouthern = round(percentage(numberofsoutheuropeancountries, num_lines), 2)
print("The percentage of South European countries partaking is:", percentagesouthern, "%")
percentagebaltic = round(percentage(numberofbalticcountries, num_lines), 2)
print("The percentage of Baltic countries (including Finland) partaking is:", percentagebaltic, "%")
percentagenoneuropean = round(percentage(numberofnoneuropeancountries, num_lines), 2)
print("The percentage of Non-European countries partaking is:", percentagenoneuropean, "%")
percentageslavic = round(percentage(numberofslaviccountries, num_lines), 2)
print("The percentage of Slavic countries partaking is:", percentageslavic, "%")
percentagesouthslavic = round(percentage(numberofsouthernslaviccountries, num_lines), 2)
print("The percentage of Southern Slavic countries partaking is:", percentagesouthslavic, "%")
percentageother = round(percentage(numberofothercountries, num_lines), 2)
print("The percentage of the 'odd ones out' partaking is:", percentageother, "%")
#Nog te doen: percentage mooier ordenen! Minder decimalen. Extra uitdaging: % teken erachter 

import csv
from itertools import islice #islice = interesting little tool that I found on the world wide web
#prevented me from writing a difficult def function
with open('euro2016.csv', 'r') as lines:
	rowsyear2016 = []
	reader = csv.reader(lines, delimiter=';')
	for line in islice(reader, 0, 26):
		rowsyear2016.append(line)

#csv.writer(new_file).writerows(rowsyear2016)

countries2016 = []
for row in rowsyear2016:
	countries2016.append(row[0])
print("Countries that were in the finals in 2016:", sorted(countries2016))
points2016 = []
for row in rowsyear2016:
	points2016.append(row[1])

pointspercountry2016 = list(zip(countries2016, points2016))
pointspercountry2016sorted = sorted(pointspercountry2016)
#print(pointspercountry2016sorted)

print("===========")

import csv
with open('results2016.csv', 'w', newline='') as new_file: #newline='' addition: filters unattractive and bothersome newlines
	writer = csv.writer(new_file)
	writer.writerows(rowsyear2016)
import csv #250
with open('results2016.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	#my_list = list(datareader)
	with open('results2016firstedit.csv', 'w', newline='') as editfile:
		writer = csv.writer(editfile)
		for x in datareader:
			writer.writerow((x[0], x[1])) #writing only the first two rows into the file, deleting the year-information '2016' [2]
csvfile.close()
new_file.close()
editfile.close()

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

count = 0
for country, result in zip(countries,results1):
	if result > count:
		winner = country
		count = result
	else:
		None

for country, result in zip(countries,results1):
	if result < count:
		loser = country
		count = result
	else:
		None

winnerresult = max(results1)
loserresult = min(results1)
print("The winner of Eurovision 2016 is:", winner, "with", winnerresult, "points.") 
print("The loser of Eurovision 2016 is:", loser, "with", loserresult, "points.")

lines.close()
csvfile.close()

print("===========")

from itertools import islice
with open('euro2016.csv', 'r') as lines:
	rowsyear2015 = []
	reader = csv.reader(lines, delimiter=';')
	for line in islice(reader, 26, 53):
		rowsyear2015.append(line)

countries2015 = []
for row in rowsyear2015:
	countries2015.append(row[0])
print("Countries that were in the finals in 2015:", sorted(countries2015))

print("===========")

points2015 = []
for row in rowsyear2015: #300
	points2015.append(row[1])
pointspercountry2015 = list(zip(countries2015, points2015))
pointspercountry2015sorted = sorted(pointspercountry2015)
print(pointspercountry2015sorted) #300 LIJNEN

print("===========")
import csv
with open('results2015.csv', 'w', newline='') as new_file: #newline='' addition: filters unattractive and bothersome newlines
	writer = csv.writer(new_file)
	writer.writerows(rowsyear2015)
import csv
with open('results2015.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	#my_list = list(datareader)
	with open('results2015firstedit.csv', 'w', newline='') as editfile:
		writer = csv.writer(editfile)
		for x in datareader:
			writer.writerow((x[0], x[1])) #writing only the first two rows into the file, deleting the year-information '2015' [2]
csvfile.close()
new_file.close()
editfile.close()

import csv
with open('results2015firstedit.csv', 'r') as csvfile:
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

scorebord2015 = zip(countries,results1)

count = 0
for country, result in scorebord2015:
	if result > count:
		winner = country
		count = result
	else:
		None

for country, result in scorebord2015:
	if result < count:
		loser = country
		count = result
	else:
		None
winnerresult = max(results1)
loserresult = min(results1)
print("The winner of Eurovision 2015 is:", winner, "with", winnerresult, "points.") 
print("The loser of Eurovision 2015 is:", loser, "with", loserresult, "points.")

secondplace = max(n for n in results1 if n!=max(results1))
print(secondplace)

points2016sorted = [int(x) for x in points2016]
points2016sorted.sort()
print(points2016sorted)

lines.close()

import csv
from itertools import islice #islice = interesting little tool that I found on the world wide web
#prevented me from writing a difficult def function
with open('euro2016.csv', 'r') as lines:
	rowsyear2014 = []
	reader = csv.reader(lines, delimiter=';')
	for line in islice(reader, 53, 79):
		rowsyear2014.append(line)

#csv.writer(new_file).writerows(rowsyear2016)

countries2014 = []
for row in rowsyear2014:
	countries2014.append(row[0])
print("Countries that were in the finals in 2014:", sorted(countries2014))
points2014 = []
for row in rowsyear2014:
	points2014.append(row[1])

pointspercountry2014 = list(zip(countries2014, points2014))
pointspercountry2014sorted = sorted(pointspercountry2014)
#print(pointspercountry2016sorted)

print("===========")

import csv
with open('results2014.csv', 'w', newline='') as new_file: #newline='' addition: filters unattractive and bothersome newlines
	writer = csv.writer(new_file)
	writer.writerows(rowsyear2014)
import csv
with open('results2014.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	#my_list = list(datareader)
	with open('results2014firstedit.csv', 'w', newline='') as editfile:
		writer = csv.writer(editfile)
		for x in datareader:
			writer.writerow((x[0], x[1])) #writing only the first two rows into the file, deleting the year-information '2016' [2]
csvfile.close()
new_file.close()
editfile.close()

import csv
with open('results2014firstedit.csv', 'r') as csvfile:
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

count = 0
for country, result in zip(countries,results1):
	if result > count:
		winner = country
		count = result
	else:
		None

for country, result in zip(countries,results1):
	if result < count:
		loser = country
		count = result
	else:
		None

winnerresult = max(results1)
loserresult = min(results1)
print("The winner of Eurovision 2014 is:", winner, "with", winnerresult, "points.") 
print("The loser of Eurovision 2014 is:", loser, "with", loserresult, "points.")

print("===========")

import csv
d = dict()
#In the file 'resultsallyears' I use the same data as in the file 'euro2016', but I edited the results from 2016, because the results in this year were doubled
#every country got to award two sets of votes: one from their professional jury and the other from televoting
#Therefore, I divided the results of this year in two, otherwise it would give an unrealistic overview of the most successful countries. 
with open('resultsallyears.csv', 'r') as csvfile:
	readFILE = csv.reader(csvfile, delimiter=';')
	countriesallyears = []
	for row in readFILE:
		if row[0] in countriesallyears:
			d[row[0]] = d[row[0]] + int(row[1])
		else:
			countriesallyears.append(row[0])
			d[row[0]] = int(row[1])
csvfile.close()

print(d) #type = dict

print("===========")

def keywithmaxval(d):
	v = list(d.values())
	k = list(d.keys())
	return k[v.index(max(v))]

mostsuccessfulcountry = keywithmaxval(d)
print("The most successful country throughout the years of Eurovision was:", mostsuccessfulcountry)

print("===========")
def keywithminval(d):
	v = list(d.values())
	k = list(d.keys())
	return k[v.index(min(v))]
leastsuccesfulcountry = keywithminval(d)
print("The least succesful country throughout the years of Eurovision was:", leastsuccesfulcountry)
print("===========")
top5countries = sorted(d, key =d.get, reverse=True)[:5]
print("The top 5 most successful countries throughout the years of Eurovision were:")
for x in top5countries:
	print(top5countries.index(x) +1, end=' ')
	print(" ", x)

print("===========")
print("The top 5 least successful countries throughout the years of Eurovision were:")
top5losercountries = sorted(d, key =d.get, reverse=False)[:5]
for x in top5losercountries:
	print(top5losercountries.index(x) +1, end=' ')
	print(" ", x)

print("===========")
print("The total ranking of all the countries is:")
totalranking = sorted(d, key =d.get, reverse=True)
for x in totalranking:
	print(totalranking.index(x) +1, end=' ')
	print(" ", x)

#465 lijnen