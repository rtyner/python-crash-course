pets = []

pet = {
    'animal type': 'dog',
    'name': 'scooter',
    'owner': 'ray',
    'weight': 42,
}

pets.append(pet)

pet = {
    'animal type': 'lizard',
    'name': 'dante',
    'owner': 'charlie',
    'weight': 2,
}

pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'goku',
    'owner': 'misty',
    'weight': 27,
}

pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'raskolnikov',
    'owner': 'mildred',
    'weight': 31,
}

pets.append(pet)

for pet in pets:
    print(f"Here is what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")