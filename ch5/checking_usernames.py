current_users = ['alice', 'bob', 'charlie', 'dave', 'edward']
new_users = ['Alice', 'gavin', 'harold', 'ivy', 'juliet']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry the username {user} is unavailable")
    else:
        print(f"The username {user} is available")
