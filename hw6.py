
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 6
# 
# Homework 6 covers exercises that involve working with functions
# 
# The below sites have some interesting and useful information on working with files
# 
# https://www.learnpython.org/en/Functions
# https://www.tutorialspoint.com/python/python_functions.htm
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw5.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# ** Slides ** for Week 6 can be found at 
# 
# https://docs.google.com/presentation/d/1XGV2NR0ZAAmQYjlRuy81zzlW2g5lWS8L6a7iRV-lreQ/edit?usp=sharing
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


# #### Sample Exercises with Functions
# 
# Refer to Week 6 slides for a recap of what happened in Week 6
# 
# https://docs.google.com/presentation/d/1XGV2NR0ZAAmQYjlRuy81zzlW2g5lWS8L6a7iRV-lreQ/edit?usp=sharing

# **Exercise 1 - Testing your knowledge of functions **
# 
# Answer the below questions
# 
# 1. What is a function in Python?
# 2. What are the advantages of using functions?

# << a function is reusable code, the advantage is that its written once and gets used a lot of time >>

# #### Exercise 2 -  Max of three numbers
# 
# Write a Python function to find the Max of three numbers.
# 
# Make sure you invoke this function in your main program and display the result

# In[2]:

### YOUR CODE GOES 
def maxNum(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
            
print maxNum(50,88,3)
### END CODE


# #### Exercise 3 - Finding the sum of numbers in a list
# 
# Write a Python function to sum all the numbers in a list
# 
# Make sure you invoke this function in your main program and display the result

# In[22]:

### YOUR CODE GOES BELOW
numberlist = "2,4,6,8,10"

def sumnumbers (numberlist):
    numbers = numberlist.split(",")
    sum = 0
    
    for i in numbers:
        temp = int(i)
        sum = sum + temp
    print sum

sumnumbers(numberlist)
### END CODE


# #### Exercise 4 - Finding the product of numbers in a list
# 
# Write a Python function to multiply all the numbers in a list
# 
# Make sure you invoke this function in your main program and display the result

# In[25]:

### YOUR CODE GOES BELOW
numberlist = "2,4,6,8,10"

def sumnumbers (numberlist):
    numbers = numberlist.split(",")
    product = 1
    
    for i in numbers:
        temp = int(i)
        product = product * temp
    print product

sumnumbers(numberlist)

### END CODE


# #### Exercise 5 - Reversing a String
# 
# Write a Python function to reverse a string
# 
# Make sure you invoke this function in your main program and display the result

# In[6]:

### YOUR CODE GOES BELOW
mystring = "Have a nice day"

def strrev (mystring):
     print mystring[::-1]

strrev(mystring)
### END CODE0


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6
# 
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# Make sure you invoke this function in your main program and display the result

# In[6]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 7
# 
#  Write a Python function to print the even numbers from a given list..
#  
#  Make sure you invoke this function in your main program and display the result

# In[7]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 8
# 
# Write a Python function that checks whether a passed string is palindrome or not.
# 
# Make sure you invoke this function in your main program and display the result

# In[13]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 9
# 
# Write a recursive Python program to compute the result of fibonacci series. 
# 
# This is what a fibonacci series is https://www.mathsisfun.com/numbers/fibonacci-sequence.html
# 
# Make sure you invoke this function in your main program and display the result

# In[14]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 10
# 
# Write a python program to autocorrect user input using the edit distance method. 
# 
# Make sure you invoke this function in your main program and display the result

# In[ ]:

### YOUR CODE GOES BELOW


### END CODE

