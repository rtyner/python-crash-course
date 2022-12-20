location = "\nWhat is your favorite vacation place? "
location += "\nType 'quit' to end the session. "

active = True
while active:
    user_location = input(location)
    if user_location == 'quit':
        active = False
    else:
        print(f"{user_location.title()} is a great vacation spot! ")