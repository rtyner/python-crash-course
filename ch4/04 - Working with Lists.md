##  Looping Through an Entire List
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # this line tells python to retrieve the first value from the list magicians and associate it with the variable magician
    print(magician)
>>> alice
    david
    carolina
```
- Breaking down a for loop
	- `for magician in magicians:` is essentially `for variable in list:`, it will read the value from the list and assign it to the variable until it reaches the end of the list
	- Once Python reaches the end of the list it proceeds to the next line of the program, in the example earlier that's the `print()` statement
- The set of steps in a for loop are repeated once for each item in the list, no matter how many items there are
- You can choose any name you want for the temporary variable
- Using singular or plural names can help identify whether a section of code is working with a single element from the list or the entire list
- You can write as much code as you want in the for loop, each indented line following `for magician in magicians:` is considered inside of the loop and is executed once for each value in the list
## Making Numerical Lists
- `range()` function can be used to create a series of numbers
```python
for value in range(1,5):
	print(value)
>>> 1
    2
    3
    4
```
- The `range()` function starts counting at the first value you give it and stops when it *reaches* the second value you provided
	- It stops at the second value, and will never include it
- You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example, range(6) would return the numbers from 0 through 5.
- You can convert the results of `range()` directly into a list using the `list()` function
```python
numbers = list(range(1,6))
```
- You can use the `range()` function to have Python skip numbers in a given range. If you pass a third argument to `range()` that value will be used as a step size when generating numbers
```python
even_numbers = list(range(2,11,2))
print(even_numbers)
>>> [2, 4, 6, 8, 10]
```
- With the value 2 at the end, Python will count to 11 by 2's - Starts with the value 2 and then adds 2 to that value and adds 2 repeatedly until it reaches or passes the end value, 11
- You can make a list of the first 10 square numbers
```python
squares = []
for value in range(1,11):
    square = value ** 2 #stores the value from the range raised to the power of 2 and stores it in the square variable
    squares.append(square) #appends the values from above to the original list

print(squares)
```

## Simple Statistics with a List of Numbers
- Finding the minimum, maximum, and sum of a list of numbers
```python
>>> digits = [1,2,3,4,5,6,7,8,9,0]
>>> min(digits)
0   
>>> max(digits)
9   
>>> sum(digits)
45
```

## List Comprehensions
- allows you to generate a list in 1 line of code instead of the 4 lines used for the squares
```python
squares = [value**2 for value in range(1,11)]
print(squares)
>>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
- A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element
## Working with Part of a List
- Slice - Working with specific items in a list
- To make a slice you specify the index of the first and last elenets you want to work with, same as `range()` Python stops one item before the last index
- To output the first 3 elements in a list you would request indicies 0 through 3 which would return elements 0, 1, and 2
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
>>> ['charles', 'martina', 'michael']
#if you omit the first index in a slice, the slice starts at the beginning of a list
print(players[:4])
>>> ['charles', 'martina', 'michael', 'florence']
# if you want all items from the third index to the last, start with index 2 and omit the second value
print (players[2:])
>>> ['michael', 'florence', 'eli']
# if you want to output the last 3 items in the list
print(players[-3:])
>>> ['michael', 'florence', 'eli']
```
## Copying a List
- To copy a list, you can make a slice that included the entire original list by omitting the first index and the second index
	- `([:])`
## Tuples
- A list that doesn't change
- Formatted like a list, but uses parenthesis instead of square brackets
	- `dimensions = (200, 50)`
```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```
- To change a tuple you have to recreate the tuple
```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
	for dimension in dimensions:
print(dimension)
```

## Code Styling
- Tabs = 4 spaces, set your editor to do this. Python can get confused when tabs are mixed with spaces.
- Line length - 80 characters
- Use blank lines to group parts of your programs