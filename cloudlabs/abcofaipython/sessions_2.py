
# Data Types and Structures in Python

# --- Numbers ---
# Integers (int): Whole numbers
integer_variable = 10  #Example of an integer
print(f"Integer: {integer_variable}, Type: {type(integer_variable)}")

# Floating-point numbers (float): Numbers with decimal points
float_variable = 3.14  #Example of a float
print(f"Float: {float_variable}, Type: {type(float_variable)}")

# Complex numbers (complex): Numbers with real and imaginary parts
complex_variable = 2 + 3j #Example of a complex number
print(f"Complex: {complex_variable}, Type: {type(complex_variable)}")


# --- Strings ---
# Strings (str): Sequences of characters
string_variable = "Hello, world!" #Example of a string
print(f"String: {string_variable}, Type: {type(string_variable)}")

#String manipulation
substring = string_variable[7:12] #Slicing a string
print(f"Substring: {substring}")
string_length = len(string_variable) #Finding the length of a string
print(f"String Length: {string_length}")


# --- Booleans ---
# Booleans (bool): True or False values
boolean_variable_true = True  #Example of a boolean
boolean_variable_false = False #Example of a boolean
print(f"Boolean True: {boolean_variable_true}, Type: {type(boolean_variable_true)}")
print(f"Boolean False: {boolean_variable_false}, Type: {type(boolean_variable_false)}")


# --- Lists ---
# Lists: Ordered, mutable (changeable) sequences of items
list_variable = [1, 2, 3, "apple", "banana"]  #Example of a list. Lists can contain mixed data types.
print(f"List: {list_variable}, Type: {type(list_variable)}")
list_variable.append("orange") #Adding an element to a list
print(f"List after append: {list_variable}")
list_variable[0] = 10 #Modifying an element in a list.
print(f"List after modification: {list_variable}")



# --- Tuples ---
# Tuples: Ordered, immutable (unchangeable) sequences of items
tuple_variable = (1, 2, 3, "apple", "banana") #Example of a tuple
print(f"Tuple: {tuple_variable}, Type: {type(tuple_variable)}")
#tuple_variable[0] = 10 #This will cause an error because tuples are immutable


# --- Sets ---
# Sets: Unordered collections of unique items
set_variable = {1, 2, 2, 3, "apple"} #Example of a set. Duplicates are automatically removed.
print(f"Set: {set_variable}, Type: {type(set_variable)}")


# --- Dictionaries ---
# Dictionaries: Unordered collections of key-value pairs
dictionary_variable = {"name": "Alice", "age": 30, "city": "New York"} #Example of a dictionary
print(f"Dictionary: {dictionary_variable}, Type: {type(dictionary_variable)}")
print(f"Accessing value by key: {dictionary_variable['name']}") #Accessing a value using its key


# --- None ---
# NoneType: Represents the absence of a value
none_variable = None #Example of NoneType
print(f"None: {none_variable}, Type: {type(none_variable)}")


