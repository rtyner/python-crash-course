## Taking User Input
- `input()` - pauses the program and waits for the user to enter text, once that input is received python assigns that info to a variable
- storing the input in a variable
```python
prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello {name}")
```
- When you use `input()` Python interprets everything as a string, if you need to convert it to an int do:
```python
age = input("How old are you? ")
age = int(age) # converts the string input into an int
```

## Modulo Operator `%` - Divides one number by another and returns the remainder
- Doesn't show how many of times a number fits into another; it only tells you what the remainder is
```python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```
- When one number is divisible by the other the remainder is 0, you can use this fact to determine if a number is even or odd
```python
number = input("Enter a number and I will tell you if it's even or odd ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else: 
    print(f"The number {number} is odd.")
```
## `while` Loops
- Loop that runs as long as a certain condition is true
- `+=` operator - shorthand for variable + 1
- Letting the user decide to quit the program
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = "" # must give an empty value so Python can run
# the users input is stored in the variable message, as long as that variables value != 'quit', the loop continues to run
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit': # wont print out the quit value
		print(message)
	
```
- flag - variable that can be assigned to determine if a `while` loop should quit
	- program runs while the value is set to `True` and stops when it is `False`
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# active flag is set at the start so that the loop runs
active = True # sets the active flag to True
while active: # while the active value is True, the loop will run
	message = input(prompt)
	
	if message == 'quit': # if 'quit' is entered the loop active value will change to False and the loop will end
		active = False # sets the active flag to False
	else: # if anything other than 'quit' is entered it printes what was entered
		print(message)
```
- `break` - exits a `while` loop without running remaining code
	- directs the flow of your program; you can use it to control which lines of code are executed and which aren't
- A loop that starts with `while True` will run forever unless it hits a `break` statement
```python
prompt = "\nPlease enter the name of a city you have visited. "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")
```
- `continue` - returns to the beginning of a loop based on the result of a conditional test
- Test every `while` loop when you're writing it to avoid infinite loops

## Using a `while` Loop with Lists and Dictionaries
- When you need to modify a list as you work through it you use a `while` loop
- Verifying users in a list with a `while` loop
```python
unconfirmed_users = ['alice', 'brian', 'candace'] # users who need to be verified
confirmed_users = [] # empty list to move the users to once confirmed

while unconfirmed_users: # loop through unconfirmed users
    current_user = unconfirmed_users.pop() # pop off an unconfirmed user and store it in current_user

    print(f"Verifying user: {current_user.title()}") # pulls the popped user from current_user
    confirmed_users.append(current_user) # appends current_user to confirmed_users
    # while loop through the rest as long as there are users in the unconfirmed list

# display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users: # pull out users 1 at a time from confirmed_users and print the value
    print(confirmed_user.title())
```

## Using a `while` loop to remove all instances of an item from a list
```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```