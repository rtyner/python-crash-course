books_read_2022 = 4
books_read_2021 = 3

print(books_read_2021 == books_read_2022)

print(books_read_2021 == books_read_2022 and 
books_read_2022 > books_read_2022)

print(books_read_2021 == books_read_2022 and 
books_read_2022 < books_read_2022)

print(books_read_2021 == books_read_2022 or 
books_read_2022 < books_read_2022)

favorite_book_upper = 'Crime and Punishment'
favorite_book_lower = 'crime and punishment'

print(favorite_book_lower == favorite_book_upper)
print(favorite_book_lower.lower() == favorite_book_upper.lower())

books_to_read_2022 = ['the brothers karamazov', 'the good war', 'ghengis khan']

book = 'the lord of the rings'
if book not in books_to_read_2022:
    print(f"the book {book.title()} is not in your list")
else:
    print(f"the book {book.title()} is in your list")

books_to_read_2022.append('the lord of the rings')
if book not in books_to_read_2022:
    print(f"the book {book.title()} is not in your list")
else:
    print(f"the book {book.title()} is in your list")