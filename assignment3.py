# **Q3 (Monday 2-5) - Assignment (Class 03)**

# Lesson 05: Control Flow and Loop

# Usage of If, Else, and Elif in Python

# Simple Python Chatbot Program

def simple_chatbot():
    """A simple chatbot that responds to user input using if-elif-else statements."""

    print("Hello! I am a Simple Chatbot. How can I help you?")  # Greeting message

    while True:  # Infinite loop to keep the chatbot running until the user exits
        user_input = input("You: ").lower()  # Taking user input and converting it to lowercase for consistency

        # Checking user input with different conditions
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hello! How can I assist you?")

        elif user_input == "how are you":
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")

        elif user_input == "what is your name":
            print("Chatbot: I am a Python chatbot!")  # Responding with chatbot's name

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")  # Exit message
            break  # Stops the loop when user types "bye"

        else:
            print("Chatbot: Sorry, I don't understand that. Can you ask something else?")  # Default response for unknown input


# Function Calling to start the chatbot
simple_chatbot()

# Using for loop, break, continue, and throwaway variable in Python

# Loop through numbers from 1 to 100
# `_` is a throwaway variable since we don't need to reference it later
for _ in range(1, 101):

    # Check if the number is divisible by both 3 and 5
    if _ % 3 == 0 and _ % 5 == 0:
        print("FizzBuzz")  # Print "FizzBuzz" for multiples of both 3 and 5
        continue  # Skip the rest of the loop and move to the next number

    # Check if the number is only divisible by 3
    elif _ % 3 == 0:
        print("Fizz")  # Print "Fizz" for multiples of 3

    # Check if the number is only divisible by 5
    elif _ % 5 == 0:
        print("Buzz")  # Print "Buzz" for multiples of 5

    else:
        print(_)  # If not divisible by 3 or 5, print the number itself

    # Stop the loop early when we reach 50
    if _ == 50:
        print("Reached 50, stopping early!")  # Inform the user about stopping
        break  # Exit the loop

"""# Lesson 06: Lists, Tuples and Dictionary"""

# Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Original List:", fruits)        # Original List: ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']

# Accessing Elements
print("First Fruit:", fruits[0])       # First Fruit: Apple
print("Last Fruit:", fruits[-1])       # Last Fruit: Grapes

# Modifying Elements
fruits[1] = "Blueberry"
print("Modified List:", fruits)        # Modified List: ['Apple', 'Blueberry', 'Mango', 'Orange', 'Grapes']

# Common List Methods
fruits.append("Pineapple")
print("After Append:", fruits)         # After Append: ['Apple', 'Blueberry', 'Mango', 'Orange', 'Grapes', 'Pineapple']

fruits.insert(2, "Strawberry")
print("After Insert:", fruits)         # After Insert: ['Apple', 'Blueberry', 'Strawberry', 'Mango', 'Orange', 'Grapes', 'Pineapple']

fruits.remove("Mango")
print("After Removing Mango:", fruits) # After Removing Mango: ['Apple', 'Blueberry', 'Strawberry', 'Orange', 'Grapes', 'Pineapple']

popped_item = fruits.pop()
print("Popped Item:", popped_item)     # Popped Item: Pineapple
print("After Pop:", fruits)            # After Pop: ['Apple', 'Blueberry', 'Strawberry', 'Orange', 'Grapes']

index_of_orange = fruits.index("Orange")
print("Index of Orange:", index_of_orange)  # Index of Orange: 3

count_of_apple = fruits.count("Apple")
print("Count of Apple:", count_of_apple)    # Count of Apple: 1

# Sorting a List
fruits.sort()
print("Sorted List (Ascending):", fruits)  # Sorted List (Ascending): ['Apple', 'Blueberry', 'Grapes', 'Orange', 'Strawberry']

fruits.reverse()
print("Reversed List:", fruits)       # Reversed List: ['Strawberry', 'Orange', 'Grapes', 'Blueberry', 'Apple']

# Iterating Over a List
print("Iterating over List:")
for fruit in fruits:
    print(fruit)                      # Strawberry, Orange, Grapes, Blueberry, Apple (printed on separate lines)

print("Using Enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")  # Index 0: Strawberry, Index 1: Orange, Index 2: Grapes, Index 3: Blueberry, Index 4: Apple


# List Comprehension
numbers = [1, 4, 6, 8, 3, 10, 2, 7]
greater_than_five = [x for x in numbers if x > 5]

print(greater_than_five)              # Output: [6, 8, 10, 7]

# Tuples in Python

# Creating a Tuple
tuple1: tuple      = tuple(["grape", "orange", "kiwi"])
tuple2: tuple      = (5, 15, 25)
mixed_tuple: tuple = ("world", 99, 2.71, False)

print("tuple1      =", tuple1)      # tuple1      = ('grape', 'orange', 'kiwi')
print("tuple2      =", tuple2)      # tuple2      = (5, 15, 25)
print("mixed_tuple =", mixed_tuple) # mixed_tuple = ('world', 99, 2.71, False)

# Accessing elements in a tuple
print("tuple1[0] =", tuple1[0])     # tuple1[0] = grape

# Tuple slicing
print("tuple2[1:] =", tuple2[1:])   # tuple2[1:] = (15, 25)

# Tuple length
print("Length of tuple1:", len(tuple1))  # Length of tuple1: 3

# Iterating through a tuple
print("Iterating through tuple2:")
for item in tuple2:
  print(item)                        # 5, 15, 25 (printed on separate lines)

# Checking if an item exists in a tuple
print("Is 15 in tuple2?", 15 in tuple2)  # Is 15 in tuple2? True

# Concatenating tuples
tuple3: tuple = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)   # tuple1 + tuple2 = ('grape', 'orange', 'kiwi', 5, 15, 25)

# Repeating tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)        # tuple2 * 2 = (5, 15, 25, 5, 15, 25)

# Nested tuples
nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple)  # nested_tuple = (('grape', 'orange', 'kiwi'), (5, 15, 25))

# Unpacking tuples
a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)  # Unpacking tuple1: grape orange kiwi

# Dictionary in Python.

my_dict = {
  "full_name": "Sara Khan",
  "years": 28,
  "location": "Los Angeles"
}

# 1. Accessing Items
print("1. Accessing Items")
print("Full Name:", my_dict["full_name"])  # Output: Sara Khan
print("Years:", my_dict.get("years"))  # Output: 28
print("Location (using get):", my_dict.get("location"))  # Output: Los Angeles

# 2. Adding Items
print("\n2. Adding Items")
my_dict["contact"] = "sara@example.com"
print("Dictionary after adding contact:", my_dict)  # Output: {'full_name': 'Sara Khan', 'years': 28, 'location': 'Los Angeles', 'contact': 'sara@example.com'}

# 3. Modifying Items
print("\n3. Modifying Items")
my_dict["years"] = 29
print("Dictionary after modifying years:", my_dict)  # Output: {'full_name': 'Sara Khan', 'years': 29, 'location': 'Los Angeles', 'contact': 'sara@example.com'}

# 4. Removing Items
print("\n4. Removing Items")
my_dict.pop("location")
print("Dictionary after removing location (using pop):", my_dict)  # Output: {'full_name': 'Sara Khan', 'years': 29, 'contact': 'sara@example.com'}
del my_dict["contact"]
print("Dictionary after removing contact (using del):", my_dict)  # Output: {'full_name': 'Sara Khan', 'years': 29}

# 5. Dictionary Methods
print("\n5. Dictionary Methods")
print("Keys:", my_dict.keys())  # Output: dict_keys(['full_name', 'years'])
print("Values:", my_dict.values())  # Output: dict_values(['Sara Khan', 29])
print("Items:", my_dict.items())  # Output: dict_items([('full_name', 'Sara Khan'), ('years', 29)])

# 6. Clearing the Dictionary
print("\n6. Clearing the Dictionary")
my_dict.clear()
print("Dictionary after clearing:", my_dict)  # Output: {}

# Adding items back for further examples
my_dict = {
  "full_name": "Sara Khan",
  "years": 28,
  "location": "Los Angeles"
}

# 7. Updating the Dictionary
print("\n7. Updating the Dictionary")
my_dict.update({"years": 30, "country": "USA"})
print("Dictionary after updating:", my_dict)  # Output: {'full_name': 'Sara Khan', 'years': 30, 'location': 'Los Angeles', 'country': 'USA'}

# 8. Iterating Through a Dictionary
print("\n8. Iterating Through a Dictionary")
print("Iterating through keys:")
for key in my_dict:
  print(key)  # Output: full_name, years, location, country

print("\nIterating through values:")
for value in my_dict.values():
  print(value)  # Output: Sara Khan, 30, Los Angeles, USA

print("\nIterating through items (key-value pairs):")
for key, value in my_dict.items():
  print(f"{key}: {value}")  # Output: key-value pairs

# 9. Checking if a Key Exists
print("\n9. Checking if a Key Exists")
if "full_name" in my_dict:
    print("Full Name exists")  # Output: Full Name exists
else:
    print("Full Name does not exist")

# 10. Dictionary Length
print("\n10. Dictionary Length")
print("Length of the dictionary:", len(my_dict))  # Output: 4

# 11. Creating a Dictionary from Iterable
print("\n11. Creating a Dictionary from Iterable")
iterable = [("fruit1", "Apple"), ("fruit2", "Banana"), ("fruit3", "Cherry")]
new_dict = dict(iterable)
print("New dictionary:", new_dict)  # Output: {'fruit1': 'Apple', 'fruit2': 'Banana', 'fruit3': 'Cherry'}

# 12. Copying a Dictionary
print("\n12. Copying a Dictionary")
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)  # Output: {'full_name': 'Sara Khan', 'years': 30, 'location': 'Los Angeles', 'country': 'USA'}

# 13. Nested Dictionaries
print("\n13. Nested Dictionaries")
nested_dict = {
    "person1": {"name": "Aisha", "age": 22},
    "person2": {"name": "Hamza", "age": 27}
}
print("Nested dictionary:", nested_dict)  # Output: {'person1': {'name': 'Aisha', 'age': 22}, 'person2': {'name': 'Hamza', 'age': 27}}
print("Aisha's age:", nested_dict["person1"]["age"])  # Output: 22

"""# Lesson 07: The Set and Frozenset"""

# Sets and Frozen Sets in Python

# Creating a Set
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 4, 5}
set3 = set(["car", "bike", "bus"])
print("Set1:", set1)  # Output: Set1: {'banana', 'cherry', 'apple'}
print("Set2:", set2)  # Output: Set2: {1, 2, 3, 4, 5}
print("Set3:", set3)  # Output: Set3: {'car', 'bike', 'bus'}

# Adding Elements to a Set
set1.add("grape")
print("Set1 after adding grape:", set1)

# Removing Elements from a Set
set1.remove("banana")
print("Set1 after removing banana:", set1)

# Set Operations
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print("Union:", setA | setB)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Intersection:", setA & setB)  # Output: {4, 5}
print("Difference:", setA - setB)  # Output: {1, 2, 3}
print("Symmetric Difference:", setA ^ setB)  # Output: {1, 2, 3, 6, 7, 8}

# Frozen Sets (Immutable Sets)
frozen_set1 = frozenset([10, 20, 30, 40])
print("Frozen Set:", frozen_set1)  # Output: Frozen Set: frozenset({40, 10, 20, 30})

# Famous Example: Removing Duplicates from a List
num_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = list(set(num_list))
print("Unique numbers:", unique_numbers)  # Output: Unique numbers: [1, 2, 3, 4, 5, 6, 7]
