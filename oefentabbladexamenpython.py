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
country_string = country_string.strip(",")
country_string = country_string.strip("" "")
country_string = country_string.split()

print(len(country_string))
print(country_string)

westerneurope = ['United Kingdom', 'Germany', 'France', 'Austria', 'Belgium', 'Netherlands', 'Luxembourg']
def count_westerncountries(country_string, westerneurope):
	count = 0
	for country in country_string:
		if country in westerneurope:
			count += 1
		return count
print(count_westerncountries(country_string, westerneurope))
