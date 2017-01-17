import csv
with open('euro2016.csv', 'r') as csvfile:
	countries = []
	readFILE = csv.reader(csvfile, delimiter=';')
	for row in readFILE:
		countries.append(row[0])
		#print(row[0])

import csv
with open('euro2016.csv', 'r') as csvfile:
	points = []
	readFILE = csv.reader(csvfile, delimiter=';')
	for row in readFILE:
		points.append(row[1])

print(points)
pointsstring = str(points)
print(pointsstring)
print(type(pointsstring))

pointspercountry = list(zip(countries, points))
filter = sorted(pointspercountry)
print(filter)
print(type(filter))

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

f = open('euro2016.csv', 'r')
reader = csv.reader(f, delimiter=';')
#reader = csv.reader(open('euro2016.csv', 'r'), delimiter=';')
#26 entries from 2016, so in computer language these are lines [0-25]
lines_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#Wat wil ik ook alweer precies doen? --> Ik wil de data van 2016 in een apart bestand krijgen

#f.close()

def read_my_lines(reader, lines_list):
	rowsyear16 = []
	lines_set = set(lines_list)
	for line_number, row in enumerate(reader):
		if line_number in lines_set:
			rowsyear16.append(row)
			if not lines_set:
				raise StopIteration

print(read_my_lines(reader, lines_list))


#import csv
#import collections

#w = csv.writer(open('neweurofile.csv', 'wb'))
#csvfile = csv.reader(open('euro2016.csv', 'r'), delimiter=';')
#next(csvfile) #skip the header

#def divide(x, y):
#	return x/y 

#z = divide(pointsstring, 2)



