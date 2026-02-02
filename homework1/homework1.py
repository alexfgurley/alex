# file: homework1. py 
# --- Variables and Data Types --- 
# 1. 
a = 10 
print(a)
print(type(a)) # a is an integer, a whole number with no deciamls. 
b = 1.5 
print(b)
print(type(b)) # b is a float, it is a decimal number
c = 3j 
print(c)
print(type(c)) # c is a complex variable or complex number, a number with both a real part "3" and imaginary part "j"
d = "hello" 
print(d)
print(type(d)) # d is a string, it is simply a series of characters that the computer will print out
e = {1, 2, 3}
print(e)
print(type(e)) # e is a list, a series of numbers 
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dicitonary, a list that defines variables and their values 
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, used to store multiple items in a variable
def print_variable(variable):
    print(variable)
    print(type(variable))
h = ["apple", "banana", "strawberry"]
print_variable(h) # h is a list just in a different format than before 
i = True 
print_variable(i) # i is a boolean variable, that is a true or false variable
j = None 
print_variable(j) # class type is none because the variable has the value of none
k = [True, "blue", 12]
print_variable(k) # k is a list containing multiple different items from booleans to integers an strings
l = str(14)
print_variable(l) # l is a string that contains the characters 14
m = 1e4
print_variable(m) # m is a float written in scientific notation 1e4=1 * 10^4
# check is above descriptions are true using the internet

# questions: 
# 1. How many different data types did you find? 
# we found 10 different types of data 
# 2. List all the data types you found. 
# integer, float, complex, string, set, dictionary, type, list, boolean, none, 
# 3. What variables have the same data tpyes? 
# b = m, d = l, h = k 
# 4. What was the data type of l? Why is it not an integer? What does str() do?
# l is a string, it is not an integer because python reads everything inside the str command as a string, it is the same thing as saying l = "14" where although 14 is an integer python reads it as a string because of the ""
# the str() function converts data into a string datatype. 
# 5. Look up one more data type not given above. 
n = range(1, 3)
print_variable(n)

# --- Booleans --- 
print(10 > 9) # True because 10 is greater than 9
print( 10 == 9) # False, because 9 is not equal to 10
print(10 <= 9) # False because 9 is not greater than or equal to 10
print(bool("abc")) # True because a boolean is only false when a string is none or false? 
print(bool(123)) # True same as above
print(bool(["apple", "cherry", "banana"])) # true because a list with nonempty characters is true
print(bool(True)) # True becuase the value of a string is always true
print(bool(False)) # False because bool for a non numeric value is only false when the value is False or none
print(bool(0)) # False because 0 is read as a false statement for a boolean
print(bool("")) # False because there are no characters in the ""
print(bool(" ")) # True because there character in the "" is a space
print(bool(())) # False because the () are empty, there is nothing to check a boolean for so the boolean is false
print(bool([])) # False same reasoning as above
print(bool({})) # False same as above
print(bool(True and False)) # False because false is in the boolean so it reads false 
print(bool(True and True)) # True because both operators are true so the and operator returns true 
print(bool(False and False)) # False because the and operator only returns true if both items are true
print(bool(True or False)) # True because the or operator returns true if at least one thing in the operator is true, in this case true is true. 
print(bool(True or True)) # True because only two options are True
print(bool(False or False)) # False because the only two boolean options are False
print(bool(not(False))) # True because opposite of False is True
print(bool(not(True))) # False because python reads the opposite of True statement which is False

# Questions: 
# 1.What pattern do you notice about expressions returning True or False?
# I noticed that the False boolean is given when there is nothing inside of "" or {}/[]
# 2. Which expression surprised you about its result?
# bool(True and False) surprised me as it returned False 
# 3. Create an expression that will return true not given above 
name = "Your Name"
print(bool(name)) # This expression is true becuase the boolean will only return false if there is "False" or nothing in the string
# 4. Create an expression, not given above, that will return False. Why is it False? 
variable_none = False
print(bool(variable_none)) # because the variable is given the false value so the boolean will always return false.

# --- Operators --- 

# Arithmetic Operators
print(10 + 5) # Performs the addition operation
print(10 - 5) # - performs subtraction 
print(2 * 4) # * performs multiplication
print(6 / 3) # / performs division
print(5 % 2) # % performs modular arithmetic
print(3 ** 2) # ** raises the first number to power of the second number
print(15 // 2) # // is floor division, basically dividiing two numbers and rounding down

# Comparison Operators
print(5 == 2) # prints a boolean value if the two integers are equal or not
print(10 != 10) # prints true if the two integers are not equal
print(2 < 5) # prints a boolean if the first integer is less than the second integer
print(12 > 5) # prints a boolean if the first integer is greater than the second integer
print(5 <= 6) # prints true if the first integer is first integer is less than or equal to the second integer
print(1 >= 10) # prints true if first integer greater than or equal to the second

# Assignments Operators 
x = 5 
x += 5 # performs x + 5
x -= 4 # performs x - 4 
x *= 3 # performs x * 3
print(x) 

# Logical Operators
# 1.What does the operator and do? Write an expression that results in True. Write an expression that results in False.
# The and operator returns true if both operands are true, for example for p and q to be true p must be true and q must be true
x = 5 == 5 
y = 3 >= 1
print(bool(x and y))
x = 5 == 2
y = (3 * 2) <= 10
print(bool(x and y))
# 2. what does the operator or do? Write an expression that results in True. Write an expression that results in False.
# Prints true if only one of the operands is true, for example p or q is true if p is ture and q is false or if p is false and q is true or both are true, it is only false when both p and q are false. 
x = True 
y = False 
print(bool(x or y))
x = 1 - 1 
y = 5 - 5 
print(bool(x or y))
# 3. What does the operator not do? Write an expression that results in True. Write an expression that results in False
# prints the opposite boolean of the statement given, for example if p is true not p is false. 
condition = False 
print(not(condition)) 
x = 5 != 10 
print(not(x))

# More Questions 
# 1. What is the difference between / and //?
# / does regular division and usually results in a float/decimal value while // is floor division meaning that it will always round the value tto the lowest integer. 
# 2. What is the difference between % and //?
# % is modular arithmetic meaning that operations are done through taking remainders mod m, // does floor division. 
# 3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
# to find the remainder after dividing two numbers I would use the % or modular arithmetic operation as that produces a remainder. for example if we divide 5 by 2 the remainder is 1 and 5 mod 2 is 1. 
# 4. How do assignment operators work? 
# assigment operators assigment a variable to an operation with a integer and execute the operation. 

# --- Strings --- 
my_string = "hello"
print(my_string) # prints: hello
print(my_string[0]) # prints the first letter in the string "h"
print(my_string[1]) # prints the second letter in the string "e"
print(my_string[2]) # prints the third letter of the string "l"
print(my_string[4]) # prints the fourth letter of the string "o"
print(my_string[-1]) # prints the last letter of the string "o" because the first letter is 0 letter so -1 letter is the last letter
print(my_string[1:3]) # prints the second and third letters of the string "el"
print(my_string[0:5:2]) # prints the the first, fifth, and second letter of the string but prints in order of lowest number to highest number
print(len(my_string)) # prints the number of characters in the string
print(my_string + " goodbye") # prints the two strings together
print(7 * my_string) # prints the string seven times 

# Questions 
#1. Define the term slicing. For which of the manipulations did you slice your string?
# slicing takes a portion of the string and prints it, we used slicing for the first 9 operations 
#2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name) #prints the string hello my name is and then inserts the variable for name
# 3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}") #prints the same string as the previous operation.
#4.What is the difference between the two last print statements?
# the second string is an f string which allows you to insert the variable directly into the string using {variable}. 

# --- Terminal Commands --- 

# ch 
# changes directories to move from one folder to another folder
# Example: cd alexgurley

# ls 
# lists all the contents of a file 
# ls 

# ls -a 
# lists all files in a directory including hidden files 
# ls -a alexgurley 

# mkdir 
# makes a new directory 
# mkdir python_decal_sp26 

# cat
# concatenates a file or displays it 
# cat filename.py

# pwd 
# lists the file path to get to the current directory
# pwd filename

# cd ..
# changes directory backwards so if youre in a file to moves out of that file
# cd .. filename

# cd . 
# changes directory to the current directory so it basically does nothing 
# cd . filename

# cd ~ 
# changes directory to the home directory 
# cd ~ filename

# cp 
# copy files or directories 
# cp filename 

# mv 
# used to move or rename a file or directory 
# mv filename

# rm 
# removes a file from the current directory
# rm filename

# clear 
# clears the terminal screen 
# clear 

# grep 
# searches for text patterns in a file
# grep filename

# Questions 
# 1. Look up 3 other commands not present. Define and explain how to use them on the command line.
# touch file -- creates an empty file 
# head file -- show the first 10 lines of a file 
# man command -- shows manuel/help for commands
# 2. What is the difference between ls and ls -a?
# ls -a lists all files including hidden files while ls doesnt show hidden files
# 3. What is a hidden file?
# a file that states with a . is a hidden file for example .filename
# Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
# -t = sort by time, -R = lists directories recursively, -l = long listing format
