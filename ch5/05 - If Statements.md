## Conditional Tests
- At the heart of every `if` statement is an expression that can be evaluated as `True` or `False` and is called a *conditional test*
- == - Equality operator returns `True` if the values on the left and right of the operator match, and `False` if they don't match
- != - Inequality operator, opposite of above
- `and` - Check whether two conditions are simultaneously `True`
```python
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21
```
- `or` - Check whether either or both conditions are `True`
```python
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >=21
```
- `in` - Check whether an item exists in a list
```python
requested_toppings = ['mushrooms', 'pineapple', 'onions']
'mushrooms' in requested_toppings
>>> True
'pepperoni' in requested_toppings
>>> False
```

## if Statements
```python
if conditional_test:
	do something
```
- If the conditional value evaluates to `True` Python executes the code following the `if` statement. If the test evaluates to `False` Python ignores the code following the `if` statement.
- if-elif-else chain
	- When you need to test more than two possible solutions you will use this
```python
age = 12

if age < 4:
	print("Your admission cose is $0")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("Your admission cost is $40")
```
- Python executes one block at a time, running each conditional test in order until one passes. Once one passes the code stops executing the chain.
- You can clean up the chain by only have one print line and storing the value in variables
```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"Your admission price is ${price}")
```
- Multiple `elif` blocks
```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission price is ${price}")
```
- Python doesn't require the else block at the end of the chain
	- Sometimes it's clearer to use an additional `elif` statement
	- **The else block is a catchall statement. It matches any condition that wasn't matched by a specific `if` or `elif` test**
- The if-elif-else chain is only appropriate to use when you just need one test to pass
- Checking whether a list is empty or now
	- When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.
```python
requested_toppings = []
if requested_toppings: # this is where the check of the list happens
	for requested_topping in requested_toppings:
	...
```
- Using multiple lists
```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry we dont have {requested_topping}")
		
>>> Adding mushrooms
>>> Sorry we dont have french fries
>>> Adding extra cheese
```
- Convert a list to lower case
```python
current_users = ['alice', 'bob', 'charlie', 'dave', 'edward']
current_users_lower = [user.lower() for user in current_users]
```