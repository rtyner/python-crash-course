def greet_users(names): # define the function and give the parameter names
    """print a greeting to each user""" # docstring
    for name in names: # pulling out each name in the list provided
        msg = f"Hello, {name.title()}!" # storing the pulled out name and a message in msg
        print(msg)

usernames = ['hannah', 'ty', 'margot'] # provided names
greet_users(usernames) # calling the function with the list of names 
