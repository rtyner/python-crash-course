fav_places = {
    'devontae': ['portugal', 'argentina', 'england'],
    'rusty': ['russia', 'slovakia', 'serbia'],
    'joe': ['england', 'belarus', 'chile'],
}

for name, places in fav_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(f"{place.title()}")
