people = {
    'bbobbert': {
        'first': 'bob', 
        'last': 'bobbert', 
        'age': '69', 
        'city': 'tampa',
    },

    'sjean': {
        'first': 'skeeter', 
        'last': 'jean', 
        'age': '45', 
        'city': 'portland',
    },

    'mboofalo': {
        'first': 'mark', 
        'last': 'boofalo', 
        'age': '23', 
        'city': 'madrid',
    },
}

for username, user_info in people.items():
   fullname = f"{user_info['first']} {user_info['last']}"
   print(f"\nUsername: {username}") 
   print(f"Name: {fullname.title()}")
   print(f"Age: {user_info['age']}")
   print(f"City: {user_info['city'].title()}")
