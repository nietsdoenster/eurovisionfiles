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

#for t in tests:
	#print(t, "->", greeting.parseString(t))
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


country_string = str(countries)
country_string = country_string.split()
print(len(country_string))
print(country_string)
unique_countries = set(countries)
sorted_unique_countries = sorted(unique_countries)
print(sorted_unique_countries) #prints the countries in alphabetical order, pretty
#print("Number of individual contestants" + len(unique_countries)) 
print(len(unique_countries)) #How many separate countries did parttake at the eurovision songcontest?
# now we are going to divide the countries into Western Europe, Southern Europe, North Europe, Eastern Europe and 'others'
#count = 1
westerneurope = ['United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg']
def count_westerncountries(country_string, westerneurope):
	count = 0
	for country in country_string:
		if country in westerneurope:
			count += 1
		return count
print(count_westerncountries(country_string, westerneurope))
#Does not seem to be properly working yet
print("=================")

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
print("The amount of years that have been examined in this study", year_count)
#91 lines of code

print("I push a change!")
#CountryandScore = country + points
#CountryandScore = Group(country.setResultsName("country")+points.setResultsName("score"))
#euroResult = CountryandScore.setResultsName("country score")+year.setResultsName("year")
#for result in eurosong:
#	stats = (euroResult).parseString(test)
#	if CountryandScore != CountryandScore:
#		if points > points:
#			result = "won by" + CountryandScore
#print(result) #that did not work 
