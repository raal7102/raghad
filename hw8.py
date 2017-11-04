
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 8
# 
# Homework 8 covers exercises that using external libraries and creating user defined libraries
# 
# The below sites have some interesting and useful information on working with files
# 
# https://docs.python.org/2/library/index.html
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw7.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# ** Slides ** for Week 8 can be found at 
# 
# https://docs.google.com/presentation/d/1HcWIuVciM0_L935Umi5rPgQHJYIv1bNfYnErfOelbtw/edit?usp=sharing
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
# Week 8 Class Work can be found here
# 
# https://github.com/cis024c/fall2017classwork/tree/master/week8

# **Exercise 1 - Testing your knowledge of External Libraries **
# 
# Answer the below questions
# 
# 1. Name two benefits of using external libraries.
# 2. What are the different ways of including an external library in a Python program?

# << 1. External libraries are written code that can be called to help in the program, it also makes the program shorter>> 
# << 2. use import <lib_name> in the program to include the library, or use a section of the imported library>>

# #### Exercise 2 -  Using the math library
# 
# Import the math library in your program and do the following
# 
# 1. Request the user to enter a number between 1 and 10
# 2. Compute the log (math.log) of the number
# 3. Compute teh factorial (math.factorial) of the number
# 4. Compute the square root (math.sqrt) of the number
# 5. Compute the sine (math.sin) of the number
# 
# Refer to https://docs.python.org/2/library/math.html for more information on the math library
# 

# In[6]:

### YOUR CODE GOES 
import math

userNumber = int(raw_input("Please enter a number between 1 and 10: "))
print "logarithm of the number you entered is:", math.log(userNumber)
print "factorial of the number you entered is:", math.factorial(userNumber)
print "squareroot of the number you entered is:", math.sqrt(userNumber)
print "sine of the number you entered is:", math.sin(userNumber)
### END CODE


# #### Exercise 3 - Random numbers
# 
# Generate a list of 10 random numbers between 1 and 100. Use random.sample function. Write a program to then sort the list of numbers in ascending order.

# In[45]:

### YOUR CODE GOES BELOW
import random

myList = []
 
for i in range (10):
        myList.append(random.randrange(1,101))
myList.sort()       
print myList
### END CODE


# #### Exercise 4 - Creating your own library
# 
# Create a python module **helperfunctions.py** with the following functions.
# 
# 1. add - returns the sum of two numbers
# 2. diff - returns the difference between two numbers
# 3. product - returns the product of two numbers
# 4. greatest - returns the greatest of two numbers.
# 
# Import this module in your python program and use the functions your created on any two numbers and print the result.
# 
# Note: Upload the **helperfunctions.py** module to your github folder along with the notebook file. You can also upload **helperfunctions.py** to Canvas if you are having trouble copying it to Github

# In[46]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 5 - Compressing a file using the zlib library
# 
# Download the story Alice in Wonderland from the link below http://www.gutenberg.org/files/11/11.txt and save it as the file alice.txt
# 
# Write a python program to open this file in your program. Use the zlib library to compress the contents of the file and write it back to another file call alice_compressed.txt
# 
# Now, open the file alice_compressed.txt, decompress using the zlib library and display the results on the screen.
# 
# Refer to Week 8 lecture slides and classwork for information on how to use zlib. 
# 

# In[ ]:

### YOUR CODE GOES BELOW


### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6
# 
# Recall the similarity function to compute the edit distance in homework 7 and classwork 7. 
# 
# Create a Python module using the similarity function. Write a Python program to invoke the similarity function on any word entered by the user.

# In[ ]:

### YOUR CODE GOES BELOW


    
### END CODE


# #### Exercise 7
# 
# Write a Python program using the urrlib2 library to print all the URLs present on the website http://www.cnn.com
# 
# Note that you will need to search for href tags in order to locate links. An easier option is to use an HTML parser module to parse the website and then you can query it for a set of links. 
# 
# 

# In[6]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 8
# 
# Write a Python program to use the Twitter library tweepy to retrieve a set of tweets from the internet.
# 
# More information on how to do this can be found here
# 
# http://docs.tweepy.org/en/v3.5.0/

# In[7]:

### YOUR CODE GOES BELOW


### END CODE


# In[ ]:



