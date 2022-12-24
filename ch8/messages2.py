def show_messages(list):
    """takes a list and prints the messages"""
    for message in list:
        msg = f"{message}"
        print(msg)

list = ['this chapter is hard', 'im having trouble focusing', 'it\'s cold outside']
show_messages(list)
