
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 9
# 
# Homework 9 covers exercises that involve the creation and execution of command line Python programs and passing arguments to a Python program.
# 
# The below sites have some interesting and useful information on working with files
# 
# http://www.pythonforbeginners.com/argv/more-fun-with-sys-argv
# https://docs.python.org/2/library/argparse.html
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw9.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# ** Slides ** for Week 9 can be found at 
# 
# https://drive.google.com/open?id=15v1bLJ5ek5Z8mY3bZDOj67o4H3Ojhxuk-8ICI_FY6O4
# 
# **Please refer back to hw1 and slack for instructions on how to setup your computer for developing using Python.**

# ### Helpful Jupyter Commands
# 
# Below are some useful commands to know when using Jupyter
# 
# 1. You can add a new cell by clicking on the "+" icon on top.
# 2. You can delete a cell by selecting that cell and clicking on the "scissors" icon on top.
# 3. You can execute a cell by either pressing shift+enter or selecting the "play" button on top.
# 4. You can create a new file in Jupyter via the File menu->New Notebook option. Make sure to select Python 2 when creating your notebook.
# 5. Also, for your code blocks make sure that Code is selected instead of another option like Markdown.
# 6. Use the Enter key to go to the next line in a cell to enter the next statement.
# 7. You can clear results by clicking on the Cell menu item and selecting Current Output->Clear or All Output->Clear depending on whether you are trying to just clear the output for one cell or for all cells.
# 8. In case your program has crashed for some reason (infinite loop, for example), you can restart your Python session by select Kernel in the menu and selecting Restart.
# 

# #### Check Python Version

# In[1]:

get_ipython().system(u'python --version')


# #### Sample Exercises with Exception Handling
# 
# Week 9 Class Work can be found here
# 
# https://github.com/cis024c/fall2017classwork/tree/master/week9

# **Exercise 1 - Testing your knowledge of command line programs **
# 
# Answer the below questions
# 
# 1. What is the benefit of executing a program from the command line as opposed to running it from within an editor like Jupyter or Spyder.
# 2. Name a Python library that you would use in order to pass arguments from the command line

# <<1. Jupyter notebook is a python editor, it allows the user to excute progrmas using that interface, when running a python code from the command line, arguments can be passed to it during excution, it also can integrate with other applications, the output of the comomand line can be processed by other applications
# 2.sys.argv is used to pass arguments to a python program >>

# #### Exercise 2 -  Creating and executing a command line program
# 
# Write a Python program that gets two numbers from the user and displays the sum of the two numbers. Make sure to make this program a .py file, something you can run from the command line.
# 
# **Note:**
# * You can use the %%writeline magic command in Jupyter to create this file, or you can simply use an external editor to create this file. Please refer to classwork in Github for examples.

# In[4]:

### YOUR CODE GOES 
## below code is in add_2numbers.py
import sys

userNumber1 = int(raw_input("please enter your first number: "))
userNumber2 = int(raw_input("please enter your second number: "))

print "The sum of the two numbers you entered is:", userNumber1+userNumber2
### END CODE


# #### Exercise 3 - Accepting arguments from the command line
# 
# Repeat the command line program above, however, this time, instead of accepting the numbers from the user using raw_input, pass in the two numbers as command line arguments.
# 
# **Note**
# You can use sys.argv or argparse, whichever you are more comfortable with.

# In[ ]:

### YOUR CODE GOES BELOW
# below is the same code in week9_exercise3.py 

import sys

userNumber1 = int(sys.argv[1])
userNumber2 = int(sys.argv[2])

sum = userNumber1+userNumber2

print "The sum of the two numbers you entered is: ", sum
### END CODE


# #### Exercise 4 - Command Line programs with multiple modules
# 
# This is also an extension to Exercises 2 and 3.
# 
# Write a Python program to add two numbers. Your Python program must have a function called **add** that is placed in a separate module called **helper.py**. Your main program, which is also a standalone Python program **main.py** must import **helper.py** and use this module to add the two numbers. 
# 
# The numbers to be added must be passed via the command line.
# 
# Here is an example of how your program would be invoked assuming the numbers to be added are 3 and 2
# 
# **python main.py 3 2**
# 
# 
# 
# 

# In[ ]:

### YOUR CODE GOES BELOW
# below is the same code in main.py

import sys
import helper

#print "Number of arguments: ", len(sys.argv), 'arguments'
#print "Argument List:", str(sys.argv)

userNumber1 = int(sys.argv[1])
userNumber2 = int(sys.argv[2])

sum = userNumber1+userNumber2

print "The sum of the two numbers you entered is:", helper.add(userNumber1,userNumber2)
### END CODE


# #### Exercise 5 - Python program with multiple modules to sort a list of numbers
# 
# Write a Python program to sort a list of numbers in ascending order. Your Python program must have a function called **sortNumbers** that is placed in a separate module called **sorthelper.py**. This function **sortNumbers** accepts a **list** of numbers. Your main program, which is also a standalone Python program **main.py** must import **sorthelper.py** and use this module to sort the numbers. 
# 
# The numbers to be sorted must be passed via the command line.
# 
# Here is an example of how your program would be invoked assuming the numbers to be sorted are 5 4 3 and 8
# 
# **python main.py 5 4 3 8**

# In[ ]:

### YOUR CODE GOES BELOW
# below is the same code as in main_exercise5.py

import sys
import sorthelper

x = []

#print "Number of arguments:", len(sys.argv), 'arguments'
#print "Argument List: ", str(sys.argv)

argCount = len(sys.argv)
#print argCount

for i in range(argCount):
  if i > 0:
     x.append(int(sys.argv[i]))

sorthelper.sortNumbers(*x)

### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6
# 
# Repeat Exercise 4 using argparse module

# In[2]:

### YOUR CODE GOES BELOW


    
### END CODE


# #### Exercise 7
# 
# Repeat Exercise 5 using argparse module

# In[3]:

### YOUR CODE GOES BELOW


    
### END CODE

