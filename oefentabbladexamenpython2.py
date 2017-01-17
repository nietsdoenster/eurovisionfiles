import csv
from itertools import islice #islice = interesting little tool that I found on the world wide web
#prevented me from writing a difficult def function
with open('euro2016.csv', 'r') as lines:
	rowsyear2016 = []
	reader = csv.reader(lines, delimiter=';')
	for line in islice(reader, 0, 26):
		rowsyear2016.append(line)
#deze lijnen staan al in de code

print("===========")
import csv
with open('results2016.csv', 'w', newline='') as new_file: #newline='' addition: filters unattractive and bothersome newlines
	writer = csv.writer(new_file)
	writer.writerows(rowsyear2016)
import csv
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
	datareader = csv.reader(csvfile)
	my_list = list(datareader)
print(my_list)
csvfile.close()

#import csv
#with open('results2016secondedit.csv') as sample, open('orderedresults2016.csv', 'w') as out:
#    datareader = csv.reader(sample)
#    header = next(datareader, None)
#    writer = csv.writer(out)
#    if header:
#        writer.writerow(header)
#    writer.writerows(sorted(datareader, key=lambda x:int(x[0])))
#print(my_list)

#import csv
#csvwriter = csv.writer(open('neweurofile.csv', 'wb'))
#header = next(pointspercountry2015, None)
#if header:
#	csvwriter.writerow(header)
#csvwriter.writerows(sorted(pointspercountry2015, key=lambda x:int(x[0])))
#19 additional lines

#eurovision2016score = list(zip(countries2016, points2016sorted))
#print(eurovision2016score)

#pointspercountry2015 = [int(x) for x in pointspercountry2015]
#pointspercountry2015.sort()
#print(pointspercountry2015)
#sadly enough, that did not work