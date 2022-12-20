sandwich_orders = ['ham', 'turkey', 'club', 'tuna']
completed_orders = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        print(f"I made your {sandwich} sandwich.")
        completed_orders.append(sandwich)
    break
print(f"The following sandwiches were made {completed_orders}")