## Variables 
- Variable names can only contain letters, numbers, and underscores. Can't start with a number.
- Spaces are not allowed in variable names
- Avoid using Python keywords and function names as variable names.
- Variables are just labels you can assign to values - Variables reference a certain value

## Strings
- string is a series of characters, anything inside of quotes is considered a string in python ' ' " "
### Methods
- `title()`
- `upper()`
- `lower()` - The lower() method is particularly useful for storing data. Many times you won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them. Then when you want to display the information, you’ll use the case that makes the most sense for each string.
```python
name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())
```

### Using Variables in Strings
- To insert a variable into a string place the letter `f` immediately before the opening quote, but braces around the names of any variables you want to use
- These strings are called `f` strings, the  `f` is for format because python formats the string by replacing the name of any variable in braces with its value
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

Whitespace
- Adding whitespace
	- Whitespace is spaces, tabs, and end-of-line symbols
	- To add a tab - `\t`
	- To add a newline - `\n`
- Stripping whitespace
	- `rstrip()` - removes whitespace to the right of a string
	- `lstrip()` - removes whitespace to the left of a string
	- `strip()` - remove whitespace from both sides of a string

```python
favorite_language = ' python '  
favorite_language.rstrip()  
>>>' python'  
favorite_language.lstrip()  
>>>'python '  
favorite_language.strip()  
>>>'python'
```
- This strip is only temporary, to save it store the stripped value in a variable
	- `favorite_language = favorite_language.rstrip()`
## Numbers

Integers
- You can add (+), subtract (-), multiply (*), and divide (/) integers in python

Floats 
- decimal points numbers
- When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float

Underscores in Numbers
- When writing long numbers you can group digits using underscores to make them more readable
```python
universe_age = 14_000_000_000
print(universe_age)
>>>14000000000
```

Multiple Assignment
- You can assign values to more than one variable using a single line
- separate the variable names and values with commas
```python
x, y, z = 0, 0, 0
```

Constants 
- A constant is a variable whose value stays the same throughout the life of a program
- use CAPITAL LETTERS for the variable name for constants