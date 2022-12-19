cities = {
    'belgrade': {
        'country': 'serbia',
        'language': 'serbian',
        'population': 1_300_000,
    },
    
    'st. petersburg': {
        'country': 'russia',
        'language': 'russian',
        'population': 4_991_000,
    },

    'moscow': {
        'country': 'russia',
        'language': 'russian',
        'population': 11_920_000,
    },

    'warsaw': {
        'country': 'poland',
        'language': 'polish',
        'population': 1_765_000,
    },
}

for city, city_info in cities.items():
    print(f"{city.title()} is in {city_info['country'].title()}, "
        f"the population is {city_info['population']}, and " 
        f"and the language spoken is {city_info['language'].title()}.")