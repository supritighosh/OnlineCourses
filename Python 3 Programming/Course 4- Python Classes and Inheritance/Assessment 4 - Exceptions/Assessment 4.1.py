#The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some countries who won gold during the Olympics.
#However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the string “Did not get gold”.

gold = {"US": 46, "Fiji": 1, "Great Britain": 27, "Cuba": 5, "Thailand": 2, "China": 26, "France": 10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []
print(gold.keys())
for x in country:
    try:
        x in gold.keys()
        country_gold.append(gold[x])
    except KeyError:
        country_gold.append("Did not get gold")

print(country_gold)