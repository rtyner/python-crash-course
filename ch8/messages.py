def show_message(messages):
    """Prints from a list of text"""
    for message in messages:
        printed_message = f"{message}"
        print(printed_message)

messages_to_print = [
    'hello i am here',
    'am i doing this right?',
    'this chapter is kind of confusing',
]
show_message(messages_to_print)