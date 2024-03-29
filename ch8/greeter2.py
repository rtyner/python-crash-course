def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease enter your name:")
    print("(enter 'q' at any time to quit")

    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print(f"Hello, {formatted_name}")
