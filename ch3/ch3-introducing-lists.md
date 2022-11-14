## Functions used in this chapter
```python
len()
title()
append()
insert()
del 
pop
remove()
sort()
reverse()
```

## What is a list?
- A list is a collection of items in a particular order
- Lists can include letters, digits 0-9, names, words, etc
- [] indicate a list and items are separated by commas
- Lists are ordered collections, you can access any element by giving python the position or *index* of the item desired
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
>>>trek
```
- You can apply string methods to list objects too
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
>>>Trek
```
- To access the last item in a list you can use the `-1` index
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
>>>specialized
```

## Changing, Adding, and Removing Elements
- To change an element in a list you specify the name of the list, the index of the element you want to change, and provide a new value for the element.
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
```
- To add an element to a list you will use the `append()` method
```python
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
>>>['honda', 'yamaha', 'suzuki', 'ducati']
```
- To insert an element into a list you will use the `insert()` method
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
>>>['ducati', 'honda', 'yamaha', 'suzuki']
```
- To remove an element from a list you will use the `del` statement with the index of the item you want to remove
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
>>>['yamaha', 'suzuki']
```
- To remove an item from a list and store it for use elsewhere you can use the `pop` method
	- **Without an index this pops the last item in the list by default**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
>>> suzuki
```
- Popping a specific item in a list
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(first_owned)
>>> honda
```
- To remove an item by its value you will use the `remove()` method
	- The `remove()` method only removes the first occurrence of an item in a list, if you need to remove more than one you will need to use a `for` loop.
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
#can store the value in a variable or call it itself
motorcycles.remove(too_expensive)
motorcycles.remove('honda')
print(motorcycles)
>>> ['yamaha', 'suzuki']
```

## Organizing a List
- Use the `sort()` method to sort a list
- Can use the `reverse=True` argument to reverse the sort
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
>>> ['toyota', 'subaru', 'bmw', 'audi']
```
- To only sort a list temporarily use the `sorted()` function
- You can use this to display a sorted order, but not alter the list itself
- To reverse the sorted method you would enter `reverse=True` after the list variable
	- `print(sorted(var, reverse=True))`
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
>>> ['toyota', 'subaru', 'bmw', 'audi']
print(sorted(cars))
>>> ['audi', 'bmw', 'subaru', 'toyota']
```
- To reverse the order of a list use the `reverse()` method
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
>>> ['subaru', 'toyota', 'audi', 'bmw']
```
- To find the length of a list use the `len()` method
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
>>> 4
```