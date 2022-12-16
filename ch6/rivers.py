rivers = {'danube': 'egypt', 'thames': 'england', 'mississippi': 'america'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for country in rivers.values():
    print(country)
for river in rivers.keys():
    print(river)