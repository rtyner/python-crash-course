toppings = "\nPlease enter the toppings you would like. "
toppings += "\nType 'quit' at any time to stop entering toppings. "

toppings_requested = ""

while toppings_requested != 'quit':
    toppings_requested = input(toppings)
    print(f"Adding {toppings_requested} to your pizza")

else:
    print("Ending")