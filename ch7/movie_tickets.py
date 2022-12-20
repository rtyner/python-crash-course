prompt = "\nPlease enter your age. "
prompt += "\nType 'quit' when you are done. "

# age < 3 - free
# age > 3 < 12 $10
# age > 12 $15
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free")

    elif age < 13:
        print("Your ticket is $10")

    else:
        print("Your ticket is $15")