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

# 24 lines of code
#Importing random salutations

print("=====================================")
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
print("=====================================")
#using a csvfile as it is very easy to collect data on these files 
import csv
with open('euro2016.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	my_list = list(datareader)
print(my_list)
# below my first eurovision statistics! 
num_lines = sum(1 for line in open('euro2016.csv'))
print("The number of entries in the years 2015 - 2016 were in total:", num_lines) #number of entries in the years 2015 - 2016 in total 

csvfile = open('euro2016.csv', 'r')
text = csvfile.read()
csvfile.close()
eurosong = text.splitlines()
print(eurosong)

#print(text) just to make sure everything went well: and it luckily did! 
from pyparsing import Word, alphas, OneOrMore, nums, Group, Literal, Suppress, Combine #number of lines:50
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

stringEnd

#Now that I have my results printed in a pretty fashion, I'm first going to separate the rows
print("===========================")
#printing the countries
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
#country_string = str(countries)
#country_string = country_string.split()
#print(len(country_string))
#print(country_string)
unique_countries = set(countries)
sorted_unique_countries = sorted(unique_countries)
print(sorted_unique_countries) #prints the countries in alphabetical order, pretty
#print("Number of individual contestants" + len(unique_countries)) 
print(len(unique_countries)) #How many separate countries did parttake at the eurovision songcontest?
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
print("================") #100 lines

def count_northerncountries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Norway', 'Sweden', 'Denmark', 'Iceland']:
			count +=1
		else:
			None
	return count

print(count_northerncountries(mylist))
numberofscandinaviancountries = count_northerncountries(mylist)
print("The number of Scandinavian entries, for instance from Norway or Iceland, in the years 2015-2016 -summed up- is:", numberofscandinaviancountries)
print("=================")

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
print("=================")

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
print("=================")

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
print("=================")

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
print("=================")

def count_southern_slavic_countries(tokens):
	first1 = tokens
	count = 0
	for token in first1:
		if token in ['Bosnia and Herzegovina', 'Croatia', 'Serbia', 'Montenegro', 'Bulgaria', 'Macedonia']:
			count +=1
		else:
			None
	return count

print(count_southern_slavic_countries(mylist))
numberofsouthernslaviccountries = count_southern_slavic_countries(mylist)
print("The number of entries from Southern Slavic countries, like Serbia and Croatia, in the years 2015-2016 -summed up- is:", numberofsouthernslaviccountries)
print("=================")

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
print("=================")


import csv
with open('euro2016.csv', 'r') as csvfile:
	points = []
	readFILE = csv.reader(csvfile, delimiter=';')
	for row in readFILE:
		points.append(row[1])

pointspercountry = list(zip(countries, points))
print(sorted(pointspercountry))

import csv
with open('euro2016.csv', 'r') as csvfile:
	years = [0]
	reader = csv.reader(csvfile, delimiter=';')
	for row in reader:
		years.append(row[2])
		#print(row[2])
csvfile.close()
separate_years = set(years) #200 lines
separate_years.remove(0) #removed an unnecessary zero from the output. I had no idea where the zero came from, but the problem was easily solved this way.
sorted_separate_years = sorted(separate_years)
print("The years that were examined -summed up- are", sorted_separate_years)
year_count = len(separate_years) #Number of years 
print("The amount of years that have been examined in this study equals the amount", year_count)

#'Approximately 205 lines of code

#CountryandScore = country + points
#CountryandScore = Group(country.setResultsName("country")+points.setResultsName("score"))
#euroResult = CountryandScore.setResultsName("country score")+year.setResultsName("year")
#for result in eurosong:
#	stats = (euroResult).parseString(test)
#	if CountryandScore != CountryandScore:
#		if points > points:
#			result = "won by" + CountryandScore
#print(result) #that did not work 
