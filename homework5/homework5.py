# Homework 5 

# 3.1 Vocab Review
# 1. Git vs. GitHub -- Git is a language that we use to communicate with the computer through the terminal, Github is a 3th party application which allows for multiple people to collaborate on a project and allows for you to share your code with a group.
# 2. Terminal vs. Command Line -- The terminal is the software/application that creates an input/output of commands with the computer itself, the command line is sort of the way of communication where we type a command such as pwd mkdir etc and the computer prints/executes the output/command itself. 
# 3. Local vs. Remote Repository -- A local repository is located directly on your machine, for example the YourName directory is my local repository where i store all the files that I need to upload. The remote repository is located on Github and allows for you to send/push files into the remote such that others can see and look at your code. 
# 4. Version Control -- Tracks changes to code/files over time allowing for us to see how edits/changes what and when they did it. 
# 5. Staging Area -- the staging area is where we choose which files to push to the remote repository. 
# 6. git add -- adds a specific file to the staging area so that we can push/commit to the remote repository
# 7. git commit -- saves changes to the local repository 
# 8. git push -- uploads the files to the remote repository
# 9. git status -- checks that status of the connection between local and remote, as well as what files in the remote have already been upload/pushed
# 10. git pull -- pulls a file from the remote repository into the local for example if someene makes changes to the files in the remote repository git pull will pull the updated files into the local repository
# 11. pwd -- path to working directory shows the path taken to the current directory we are in 
# 12. ls -- lists the items in a directory, for example ls while in homework5 lists all the files inside homework5 
# 13. cd -- change directory, moves into a new specified directory or moves backwards by using cd .. 
# 14. nano -- allows us to create and edit a file inside a directory, such as a .py .txt file 
# 15. touch -- creates a file but does not automatically edits it 
# 16. mv -- moves a file from one location into another usually need to specific the new location using a path of directories
# 17. rm -- remove, permantely delates a file or directory
# 18. cat -- concatenate, used to combine files in a directory 

# 3.2 Directory Tree 
# 1. pwd will tell you your current directory
# 2. ls will list all files in judy_decal
# 3. cd .. to move back into the python_decal directory then cd into breanna repo then we can make sure we are in the correct directory using pwd and use git pull to pull the updated file
# 4. Use the mv command something like mv homework.py ../python_decal/judy_decal
# 5. cd .. to move into python_decal then cd judy_decal 
# 6. nano homework5.py 
# 7. first make sure the homework5.py file is saved then us git add, then git commit then git push
# 8. the remote repository has commits that the local does not have so we need to update the local then push the change again using git pull and git push 
# 9. Users/username/Recents/ 

# 4.1 Datatypes

def checkdatatype(input) : 
    possible = int, float, str, dict, list, complex, tuple, range
    for x in possible : 
        if type(input) == x : 
            return f"'{x.__name__}'"

# checkdatatype(3.1)
# checkdatatype("oawing")

# 4.2 Conditionals
def EvenOrOdd(int) : 
    if int % 2 == 0 :
        print("'Even'")
    elif int % 2 == 1: 
        print("'Odd'")

# EvenOrOdd(7) 
# EvenOrOdd(6)

# 5 Loops
def SumWithLoop(lst) : 
    sum = 0 
    for int in lst : 
        sum += int
    print(f"'{sum}'")

# SumWithLoop([1,2,3,4,5,6,7])

# 6.1 Lists
def duplicate_list(lst) : 
    lst_new = []
    for x in lst : 
        lst_new.append(x)
        lst_new.append(x)
    print(lst_new) 
# duplicate_list([1,2,3])

# 6.2 Debugging 
def square(num) : 
    print(num * num)

# square(4)

# 7. Running VS Code

print(checkdatatype([1,2,3,4,5]))

