#lijn 1 t/m 100: 30 witregels
#lijn 101 t/m 200: 28 witregels
#lijn 201 t/m 300: 30 witregels
#lijn 301 t/m 400: 21 witregels
#lijn 401 t/m 500: 22 witregels
#lijn 501 t/m 600: 25 witregels
#lijn 601 t/m 700: 31 witregels
#Totaal: 187 = 513 - 7 = 495 lijnen 
#498 lijnen

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
#using a csvfile as it is very easy to collect data with these files 
import csv
with open('resulteurovision2016.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	my_list = list(datareader)

csvfile = open('resulteurovision2016.csv', 'r')
text = csvfile.read()
csvfile.close()
eurosong = text.splitlines()

from pyparsing import Word, alphas, OneOrMore, nums, Group, Literal, Suppress, Combine 
word = Word(alphas)
num = Word(nums)
country = OneOrMore(word)
points = Word(nums)
year = Word(nums)
weirdsymbol = Suppress(Literal(";"))
annualscore = country + points + year
annualscore1 = country + weirdsymbol + points + weirdsymbol + year 
country.setParseAction(lambda tokens: " ".join(tokens)) #combines output like 'United' 'Kingdom' into ONE string, more pretty result. 
# Because at first I couldn't get the program to properly work, I did a short testround. 
tests2 = """Bulgaria 206 2016
Germany 0 2015
Belgium 500 2016"""# we want to add splitlines to this code: doing the following --> new variable + splitlines()
# ---> 

experiment = tests2.splitlines()

for test in experiment:
	simple_stats = annualscore.parseString(test)
	print(simple_stats.asList()) #--> or
#Test round gone well, now we will move on to the real file."

#eurosong = eurosong.splitlines()
newlist = []
for result in eurosong:
	stats = annualscore1.parseString(result)
	newlist.append(stats.asList())

print(newlist)
newstring = " ".join(str(x) for x in newlist)
print(newstring)

countries = []
results = []
years = []
for x in newstring:
	country, points, year = annualscore1.parseString(x)
	countries.append( " ".join(country))
	results.append( " ".join(points))
	years.append( " ".join(year))



#for i in range(10):
#	print("%s, has scored '%s' points in the year %s." % ( country, "".join(points), year))
#stringEnd
