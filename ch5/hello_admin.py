usernames = ['admin', 'rt', 'jr', 'md', 'dn']

if usernames:    
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user} thanks for logging in")