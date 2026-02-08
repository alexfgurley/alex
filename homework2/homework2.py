# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a program that allows for manipulation of code over different users/computers, github is the online web service that allows for the sharing of different code to multiple people, gitbash is what allows for windows computers to have command line/terminal communication between the computer and the user. 

# 2) What’s the difference between the terminal and the command line?
# they refer to the same thing, the terminal is the application that allows for direct communication with the computer, while the command line is the actual thing that you type into

# 3) How does Windows PowerShell differ from Git Bash?
# windows powershell uses a slightly different language and is the main way that the windows operating system was developed, however, in order to use the terminal on windows we must use a different language, becuase the windows power shell uses slightly different language, so in order to understand it we use gitbash to help convert. Another difference is that mac machines come predownloaded with gitbash allowing for almost seamless interaction between user and machine.  

# 4) What’s the difference between Anaconda, conda, and Python?
# python is a programming language used to develop applications, anaconda is a full package designed to aid in the applications of python programming and comes with python preinstalled. and conda is a environment manager. Essentially, conda has python, and anaconda has both conda, python and many other applications. 

# 5) What is VS Code? 
# Vs Code is a python interpreter that makes designing and running python code easier, it allows for the installation of different plug ins that help with debugging or reading code. 

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# Jupyter Notebook is used to explore and utilize data, will Jupyter Lab includes notebook and allows for the use of many different notebooks.

# 7) What does ~/ mean?
# ~/ refers to the home directory

# 8) What’s the difference between an absolute path and a relative path?
# an absolute path refers to all the directories used to get to a file location, that being user/downoads/......, can also be seen as the location of a file from the home directory, whereas relative path is the path to a file from the current working directory. 

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# absolute path: Users/alexgurley/python_decal_sp26/AlexGurley/course_assignments/homework2 
# relative path: AlexGurley/course_assigments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd .. 

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# it would remove all the files in the current directory

# 12) What do the following commands do?
# git add  --> adds a file to the staging area, essentially saying that this is one of the files that you want to upload on the next commit
# git commit --> saves the files in their current state to upload
# git push --> uploads the local changes from local repository to the remote repository

# 13) What's the difference between "git add ." and "git add <file>"?
# git add . adds all the files in a directory, while git add <file> only adds a specific file

# 14) What do "git status" and "git log -1" do?
# git status checks to see the path of the current directory and the repository

# 15) What’s the difference between cloning a repository and pulling from it?
# cloning a repository takes all the files of a current repository in their current state, pulling from a repository updates current parts of the cloned repository if they have been updated by another user

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# the most frustrating bug is when using loops and if else statements because the syntax is very particular and as such it makes it difficult to work with them. 

# 17) What’s a question you still have? What’s something you’re confused about?
# no current questions

# 18) Tell me a fun fact!
# there are more trees on earth than stars in the galaxy

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
import math 
x = 15.7
y = math.floor(x)
print(y) # the floor function rounds any number to its lowest integer, for example in this case the float 15.7, rounding down gives us the integer 15. This is useful for turning float values into integer values. 
print(type(x))
print(type(y))
