# Python Programming 101
Build a solid foundation in Python, an excellent starting language known for its versatility and concise syntax.

# Instructor
- name: Terence Stone
- email: terence@simplefractal.com
- website: [simplefractal.com](http://simplefractal.com)

# What do you need?
- Terminal for Mac users, Command Prompt for Windows users
- Python 2.7 or higher (Run `python --version` in your Terminal or Command Prompt to see what you have installed)
- Alternatively, you can run Python using an [online interpreter](https://repl.it/languages/python3)

# The Basic Data Types
What are the basic data types?
- Integers, e.g. 1, 2, 3
- Floating point numbers, e.g 2.3, 3.782738
- String, e.g. "John Krasinski"
- Boolean, True or False
- None, which just corresponds to empty or null, if you've used other languages

Let's start with integers and floats.

Let's go into the python shell.
To do this, open up your terminal and type 'python' and then press Enter.

We can do math in the shell.
```python
>>> 2 + 2
4
>>> 2 * 3.5
7.0
>>> 7 / 2.0
3.5
```

Practice question - try these out in the shell:
```
1. 2 * 7 * 3.5
2. 3 + 5 - (2 * 6)
3. (3 + 5 - 2) * 6
4. 4 == 5
5. 5 == 5
6. 4 < 5
7. 5 >= 4
8. 9 != 9
9. 8 != 9
```

Explanations:
```
In 1., we learned that you can chain operations
In 2 and 3, we learned that order matters and you can use parentheses to indicate the order, as part of the usual mathematical order of operations.
In 4 and 5, we learned about the equality operator.
In 6 and 7, we learned about inequality comparions like less than or greater than equal to.
In 8 and 9, we learned about the not-equal-to operator.
```

Now let's talk variables. What's a variable? It's a placeholder for a value.
```python
>>> x = 5
>>> y = 2
>>> x + y
7
>>> x = 3
>>> x + y
5
```

Practice question:
Given x=10, y=2, predict the answers to the following and then try them out in the shell:
```
1. x + y
2. x * y
3. (x + 7) / y
4. (x + 7.0) / y
5. x == y
6. x != y
```

Now let's talk about Booleans.
Simply put, a boolean variable is either True or False, and every python object or data has a boolean value.
We can find out what the true-false value is by using bool()

Let's try it out:
```python
>>> bool(False)
False
>>> bool(True)
True
>>> bool(0)
False
>>> bool(7)
True
>>> bool(None)
False
>>> bool(7 == 0)
False
>>> 7 == 0
False
```
Last stop on our journey into basic data types: Strings
A string is a sequence of characters, for example "Hello" or "My id # is 1235!"
Let's try a few in our shell:
```python
>>> "Hello World!"
Hello World!
>>> "Hello" + " World!"
>>> 1 + "world"
```

Practice problem:
```
- Set a variable called `name` equal to your full name.
- Set a variable called `first_name` equal to your first name.
- Set a variable called `last_name` equal to your last name.
- Then combine `first_name` and `last_name` so that it equals your full name, and save this in a variable called `full_name`.
- Prove using the == operator that they are equal.
```

What if we wanted to prompt the user to set the variables as opposed to having them pre-defined? We can use `input` (Python 3+) or `raw_input` (Python 2.x) like so:

```python
>>> first_name = input("What is your first name? ")
>>> last_name = input("What is your last name? ")
>>> print("Your full name is: {} {}".format(first_name, last_name))
```

The above is an example of "string interpolation", a technique used for interpolating strings with variables.


Application and Numbers Recap: Lemonade Accounting

Prompt the user for how many lemonades he/she sold and over how many hours.
Use code to print out how much profit the user made, as well as the user's average hourly income.

Assume the following:
 - It takes 4 lemons to make a lemonade
 - Each lemon costs 50 cents
 - You charge $5 per lemonade
 - Cost of the lemonades is your only expense
 - When prompted, the user will input valid integer values

```python
num_lemonades = int(input("How many lemonades did you sell? "))
num_hours = int(input("Over how many hours? "))

lemons_per_lemonade = 4
price = 5
lemon_cost = 0.5

revenues = num_lemonades * price
expenses = lemon_cost * num_lemonades * lemons_per_lemonade

profit = revenues - expenses

print("You made ${}, or ${} per hour.".format(profit, profit / num_hours))
```

# Lists
Lists is a super useful data type often used to store a multitude of similar things.
It's an ordered collection of items, which you can modify by adding or removing elements.

Let's learn the syntax of a list:
```python
>>> x = [1, 2, 3, 4, 5]
>>> len(x)
5
>>> # what's between the brackets is called the index
>>> x[0]
1
>>> x[1]
2
>>> x[4]
5
>>> x[6]
IndexError
>>> x.append("hello")
>>> len(x)
6
>>> x[5]
"Hello"
>>> # can remove elements, defaults to popping off the last one
>>> x.pop()
"Hello"
>>> print x
[1, 2, 3, 4, 5]
>>> # can specify the index
>> x.pop(2)
3
>>> print x
 [1, 2, 4, 5]
>>> # can do a boolean check if something is in the list
>>> 5 in x
True
>>> 3 in x
False
```

Practice problem:
```
- Create a list called `restaurants` consisting of the following elements in this order:
"Laut", "Random String", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"
- Get the third element of the list
- Add "Ootoya" to the end of the list
- Use .pop() to remove "Random String" from the list
- Print the list
- Check if 'Chipotle' is in the list
- Check if 'Dunkin Donuts' is in the list
- Get the length of the list
```

Let's learn about slicing:
```python
>>> y = [1, 2, 3, 4, 5, 6, 7, 8]
>>> y[2:]
[3, 4, 5, 6, 7, 8]
>>> y[:4]
[1, 2, 3, 4]
>>> y[1:3]
[2, 3]
>>> y[-3:]
[6, 7, 8]
```
- In the square brackets after the list, there is now a colon to indicate slicing.
- Slicing produces a new list that is a subsection of the original list.
- What comes before the colon is the first index we wish to include. It defaults to 0.
- The sliced list includes all element up until but not including the index specified after the colon. If you don't specify it, all elements through the last element of the list will be included in the sliced list.
- Negative indices are supported. `-3` refers to the third element from the end of the list.

# Dictionaries
Dictionaries are also massively useful. One use case is for storing several attributes or data points about the same thing. You can think of them as maps, between a set of keys and their corresponding values.
Let's look at one in the shell to better understand how they work and how they can be useful:

```python
>>> # Here's the syntax, `{}` with `key:value`, with `key` being a string.
>>> dog = {"name": "Lucky", "age": 12, "friends": ["Penny", "Pancho"]}
>>> # like for lists, we use the brackets to reference data inside but instead of the index, we provide the key name as a string
>>> dog["name"]
"Lucky"
>>> dog["friends"].append("Spot")
>>> len(dog["friends"])
3
>>> dog["random"]
KeyError
>>> dog["breed"] = "golden retriever"
>>> dog
{'friends': ['Penny', 'Pancho', 'Spot'], 'age': 12, 'name': 'Lucky', 'breed': 'Golden Retriever'}
>>> key = "age"
>>> dog[key] += 1
>>> dog
{'friends': ['Penny', 'Pancho', 'Spot'], 'age': 13, 'name': 'Lucky', 'breed': 'Golden Retriever'}
>>> del dog[key]
>>> dog
{'friends': ['Penny', 'Pancho', 'Spot'], 'name': 'Lucky', 'breed': 'Golden Retriever'}
>>> dog.keys()
dict_keys(['friends', 'name', 'breed'])
>>> dog.values()
dict_values([['Penny', 'Pancho', 'Spot'], 'Lucky', 'Golden Retriever'])
>>> dog.items()
dict_items([('friends', ['Penny', 'Pancho', 'Spot']), ('name', 'Lucky'), ('breed', 'Golden Retriever')])
>>> # check if a key exists in the dictionary
>>> "name" in dog
True
>>> "favorite_food" in dog
False
```
Practice problem:
```
Create a dictionary called `class_data` with the following keys:
- "course_name", which should correspond to "Intro to Python"
- "student_count", which should correspond to number of students, say 20
- "instructor", which should itself be a dictionary with the following keys
    - "name" ("Henry")
    - "gender" ("M")
    - "can_program" (True)
- get the student count from the dictionary
- get the instructor name from the dictionary
- delete the gender key under instructor
- change the instructor name to "Henry Xie"
```

# If/Else
If/else statements are blocks of our code that allow us to do different things based on some logical condition
Let's learn the syntax, note INDENTATION is important:
```python
>>> x = 5
>>> if x > 4:
        print("Hello")
    else:
        print("World")
Hello
>>> if x < 5:
        print("Less than five")
    else:
        print("Greater than or equal to five")
>>> if x == 1 or x == 2:
        print("Ha")
    elif x == 3:
        print("Hey")
    else:
        print("Hi")
```

Practice problem:
```
- Prompt the user for an integer between 0 and 100 using `input` or `raw_input`
- If the number is greater than 75, print "You picked a large number!"
- Else if the number is greater than 40, print "You picked a decently large number."
- Else if the number is greater than 10, print "Ok, that's still respectable."
- Else print "Wow, your number is really small."
```

# Loops
Loops let us pass through a set of values and do some operation on each.
There are different kinds of loops, for loops and while loops. They're quite similar, but let's look at the canonical loop, the for loop.

```python
>>> numbers = [1, 2, 8, 7, 9, 10]
>>> odds = []
>>> for number in numbers:
        if number % 2 == 1:
            odds.append(number)

>>> odds
[1, 7, 9]
```
- the `number` in the for loop syntax is a dummy variable that refers to the element in the list that we're passing through. The first time around, number refers to 1, the last time it refers to 10.
- we are going through this list and if the number is odd, we add it to the odds list that we initialized before the for loop.
- this technique/algorithm of initializing a variable (in this case as an empty list), and constructing it as we loop over data, is very common and useful.

Before we move on to some practice problems, here is a useful function:
```python
>>> range(10)
```

Practice problems:
```
- Construct a list of numbers between 0 and 1000 that are divisible by 33
- Given the following list
["Donald Duck", "Mickey Mouse", "Daffy Duck", "Goofy", "Minnie Mouse", "Pluto"]
Get the sum of all of the lengths of these strings.
- Given the above list, create a list of all of the elements that have the letter "d" or the letter "m" in them
```

# Functions
Functions are the heart and soul of python. Functions are blocks of code that take an input and based on some rules produce an output.

Let's learn the syntax of functions:

```python
>>> def add(a, b):
        return a + b
>>> z = add(3, 4)
>>> print(z)
7
```
a and b are variables that the function `add` takes, a.k.a. ARGUMENTS

Practice problems:
```
- create function `multiply` that takes two variables and returns their product
- create function `subtract` that takes two variables and returns their difference
```

Let's write a function that takes a variable, which is a list of numbers, and then returns just the ones that are divisible by 33.

```python
def div_by_33(numbers):
    by_33 = []
    for number in numbers:
        if number % 33 == 0:
            by_33.append(number)
    return by_33
```

Practice problem: Write a function that takes a list of numbers and returns True if the sum of the numbers is even and False otherwise.

# Methods
Methods are functions that are attached to things, or "objects" in programming-speak. These methods are accessed on the object using dot notation. Here is an example:

```python
>>> greeting = "Hello, World"
>>> print(greeting.lower())
hello, world!
```
- `greeting` is a variable that contains a string. All strings have the `lower` method, which when called, produces the lowercase value of the string it was called on.
- methods and functions are conceptually the same

# 'Real-life' problem: Restaurant Recommendation Engine
- figuring out where to eat lunch everyday is annoying
- let's automate it
- First version is going to be given a list of restaurants, randomly pop out a recommendation until the list is depleted

Let's learn about the random library, a pretty useful builtin python library:
```python
>>> import random  # this is how we make accessible the random library code
>>> numbers = [1, 3, 5, 6, 7]
>>> shuffled = random.shuffle(numbers)
>>> for number in shuffled:
        print(number.pop())
3
1
6
5
7
```

Problem 1:
```
Given a list of restaurants,
["Laut", "Random String", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"]

Write a function that takes the list of restaurants, shuffles the list,
and one by one pops out a restaurant as a recommendation.
```

What happens when we deplete the list and need to recommend again, let's go by the following algorithm:
- Each time, randomly recommend a restaurant from the list that has not been recommended in the last 4 tries

We're going to create a file called recommender.py and type the below in there.

```python
import random

# Keep track of the recommendations
recommendation_history = []
restaurants = ["Laut", "Random String", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"]

def recommend():
    random.shuffle(restaurants)
    for choice in restaurants:
        # Slice the list starting from the fourth last element to the end
        if choice not in recommendation_history[-4:]:
            recommendation_history.append(choice)
            return choice
```
# Extras
## Base64
- 8 bit binary encoded into format that can be presented by 7bits
- This is done only using A-Z, a-z, 0-9, +, and /to represent data and ‘=‘ to pad data
- Allows binary data to be represented in a way that looks and acts like plain text which makes it more reliable
- Encoding in base64 just means converting binary data into a limited character set of 64 characters mentioned above
- For every 3 bytes of data, there are 4 bytes of base64 encoded data so ends up being longe

### Practice
1. Click [this link](https://cms-assets.tutsplus.com/uploads%2Fusers%2F1181%2Fposts%2F25588%2Fimage-1451298364838.gif) and save the image to your desktop
2. Execute the following:
```
image = open('Desktop/deer.gif')`
`read = image.read()`
`encoded = base64.encodestring(read)`
`decoded = base64.decodestring(encoded)`
`open('Desktop/deer_decode_2.gif', 'w').write(decoded)`
```
    
# Useful python libraries to know
- random
- math
- datetime
- collections
- csv

# Crazy cool python libraries to know
- pandas
- nlptoolkit

# So many cool things you can do with python
- AI/ Machine learning/ Natural language processing
- Web development
- Data science

# What's next?
- Web development: [Django](http://djangoproject.com) or [Flask](http://flask.pocoo.org/)
- Data science: [pandas](http://pandas.pydata.org/)
- Tutorial: [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
- [Practice problems with full solutions](https://github.com/suneel0101/python-powerup)
- Practice problems: [Project Euler](https://projecteuler.net/)
