party = input("How many people are in your party? ")
party = int(party)

if party > 8:
    print("You will need to wait for a table.")
else:
    print("There is an available table")