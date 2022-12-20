prompt = "\nPlease enter your age. "
prompt += "\nType 'quit' when you are done. "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age > 110:
        print("Bad input")
        break

    if age < 0:
        print("Bad input")
        active = False

    if age < 3 and age > 0:
        print("Your ticket is free")

    elif age < 13 and age > 0:
        print("Your ticket is $10")

    elif age > 0 and age > 13:
        print("Your ticket is $15")