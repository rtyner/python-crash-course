## Resources
- [Python Crash Course Solutions](https://ehmatthes.github.io/pcc_2e/)

## Terms
- String - Series of characters
- Variable - Labels that you can assign values to
- List - Collection of items in a particular order
- Dictionary - Collection of key:value pairs
- Tuple - A list that doesn't change, uses parenthesis instead of square brackets
- Slice - A specific group of items in a list, accessed by specifying the indices of the items
## Methods
| Name        | Definition                                         | Chapter |
| ----------- | -------------------------------------------------- | ------- |
| `title()`   | changes to Title case                              | 2       |
| `upper()`   | changes to upper case                              | 2       |
| `lower()`   | changes to lower case                              | 2       |
| `strip()`   | removes whitespace from both sides of a string     | 2       |
| `rstrip()`  | removes whitespace from the right side of a string | 2       |
| `lstrip()`  | removes whitespace from the left side of a string  | 2       |
| `len()`     | gets the length of a list                     | 2       |
| `append()`  | appends a value to the end of a list               | 3       |
| `insert()`  | inserts a value into a specific part of a list     | 3       |
| `pop`       | removes and item from a list but stores it for use |         |
| `del`       | deletes an item in a list at a specific index      |         |
| `remove()`  | removes an item from a list by its specific value  | 3       |
| `sort()`    | sorts a list alphabetically                        | 3       |
| `reverse()` | reverses the sort of a list                        | 3       |
| `get()`     | retrieves an item from a dict                      | 6       |
| `set()`     | filter duplicate items                             | 6       |
| `items()`   | returns a sequence of key:value pairs              | 6       |
| `keys()`    | returns only the keys in a dict                    | 6       |
## Code Examples
- List comprehension - Ch. 4
```python
# non list comprehension code:
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
# using list comprehension
squares = [value**2 for value in range(1,11)]
```

## Topics to Research