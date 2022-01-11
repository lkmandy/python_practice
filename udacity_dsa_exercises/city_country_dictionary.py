"""
Time to play with Python dictionaries! You're going to work on a dictionary that
stores cities by country and continent. One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by modifying the structure.
Then, you should print out the values specifiedby looking them up in the structure.

Print the following (using "print")
1. A list of all cities in the USA in alphabetic order.
2. All cities in Asia, in alphabetic order, next to the name of the country.

In your output, label each answer with a number so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country
"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': 'Cairo'}
locations['North America']['USA'].append('Atlanta')

print('1')
american_cities = sorted(locations['North America']['USA'])

for city in american_cities:
    print(city)


print('2')
asian_cities = []
for country, city in locations['Asia'].items():
    city_country = city[0] + " - " + country
    asian_cities.append(city_country)

sorted_asian_cities = sorted(asian_cities)

for city in sorted_asian_cities:
    print(city)
