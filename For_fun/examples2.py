user_input = input()
entries = user_input.split(',')
country_pop = {}

for pair in entries:
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }

country_pop ={'China':1365830000,'India':1247220000,'United States':318463000,'Indonesia':252164800}
for c in country_pop:
    p=country_pop[c]
    print(country, 'has', pop, 'people.')