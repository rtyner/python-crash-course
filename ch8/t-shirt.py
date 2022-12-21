def make_shirt(size, text):
    """accepts size and text to print on a shirt"""
    print(f"The size of your shirt is: {size} and the message is {text}")


make_shirt('XL', 'positional arguments')
make_shirt(size='M', text='keyword argument')
