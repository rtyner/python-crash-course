fav_language = {
    'carl': 'c',
    'sara': 'rust',
    'jesus': 'c++',
    'frank': 'bash',
}

new_poll_entries = ['mike', 'pyotr', 'carl', 'dunya', 'jesus', 'frank']

for entry in new_poll_entries:
    if entry in fav_language.keys():
        print(f"{entry.title()}, thanks for taking the poll")
    else:
        print(f"{entry.title()}, please submit your answer")