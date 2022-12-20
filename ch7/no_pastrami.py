sandwich_orders = [
    'ham', 'turkey', 'club', 'tuna', 'pastrami', 
    'pastrami', 'pastrami'
    ]
completed_orders = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        if sandwich == 'pastrami':
            print(f"Sorry, we are out of {sandwich}")
        if sandwich != 'pastrami':
            print(f"I made your {sandwich} sandwich.")
        completed_orders.append(sandwich)
    break
while 'pastrami' in completed_orders:
    completed_orders.remove('pastrami')
    
print(f"The following sandwiches were made {completed_orders}")