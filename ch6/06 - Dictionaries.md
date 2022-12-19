- A dictionary is just a collection of key-value pairs
- A keys value can be a number, a string, a list, or even another dictionary
- wrapped in braces {} with a series of key value pairs inside the braces
- To retrieve the value of a key, give the name of the dict and place the key inside of square brackets
```python
alien_0 = {'color': 'green'}
print(alien_0['color']
```
- You can have an unlimited number of key value pairs in a dict
- You can add new entries to a dict at any time
- To add a value you would give the name of the dict followed by the new key in square brackets and the value outside after =
```python
alien_0['x_position'] = 0
alien_0['y_position'] = 25
```
- To change the value in a dict just do the same thing as adding a new entry but call the existing value
- To delete a value in a dict you use the `del` statement to completely remove a key value pair
	- a `del` needs the name of the dict and the key you want to delete
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
>>>{'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)
>>>{'color': 'green'}
```
- Multi lined dicts
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', # it's good practice to inclide a comma after the last value, so you are ready to add more later
}
```
- Using the `get()` method to retrieve an item from a dict
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points']) #this fails because there is no value: points

point_value = alien_0.get('points', 'No point value assigned')
# this get() method asks for the value for points, and it sets a default value for it if it doesn't exist
print(point_value)
```
## Looping through a dictionary
- You can loop through all of a dicts key value pairs, through it's keys, or through its values
```python
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```
- `items()` method returns a sequence of **key value pairs**
```python 
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}."
```
- `keys()` method returns only the keys in a dict
```python
for name in favorite_languages.keys(): # can omit keys(), default action is too loop through the keys
    print(name.title())
```
- When you wrap `set()` around a collection of values that contains duplicate items, Python identifies the unique items in the collections and builds a set from those items

### Nesting
- Storing multiple dicts in a list or a list of items as a value in a dict
```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # storing the dicts of aliens in a list
```
- generate items and store in an empty list
```python
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# show how many aliens have been created
print(f"The total number of aliens is {len(aliens)}")
```
- Storing a list in a dict
```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
```
- You can nest a list in a dict when you need more than one value associated with a key