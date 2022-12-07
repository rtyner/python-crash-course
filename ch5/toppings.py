requested_toppings = ['mushrooms', 'extra cheese']

if requested_toppings != 'anchovies':
    print("Hold the anchovies")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Addin pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza")