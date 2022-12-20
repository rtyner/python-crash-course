responses = {}
# set a flag to indicate polling is active
polling_active = True

while polling_active:
    # prompt for users name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain do you like? ")

    # store the responses in a dict
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete, show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")