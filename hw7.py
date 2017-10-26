
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 7
# 
# Homework 7 covers exercises that involve Exception Handling
# 
# The below sites have some interesting and useful information on working with files
# 
# * Errors and Exceptions: https://docs.python.org/2/tutorial/errors.html
# * Built-in Exceptions: https://docs.python.org/2/library/exceptions.html
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw7.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# ** Slides ** for Week 7 can be found at 
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
# Week 7 Class Work can be found here https://github.com/cis024c/fall2017classwork/tree/master/week7

# **Exercise 1 - Testing your knowledge of Exceptions **
# 
# Answer the below questions
# 
# 1. What is the difference between a Syntax Error and a Runtime Error?
# 2. Are exceptions Syntax Errors or Runtime Errors?
# 3. How do exceptions help a programmer?
# 4. Which exception is raised when the user tries to use a variable that has not been defined?

# <<1. syntax error is a typo error when writing the code, it is detected before the program is excuted, 
# Runtime error is detected during program excution and it terminates the program 
# 2. Exceptions are Runtime Errors
# 3. Exceptions help to detect errors in the program and prevent it from crashing 
# 4. NemeError Exception is raised when the user tries to use a variable that has not been defined>>

# #### Exercise 2 -  Raising Exceptions
# 
# Write python programs that raise the following exceptions.
# 
# 1. ValueError
# 2. TypeError
# 3. IndexError
# 4. KeyError

# In[2]:

### YOUR CODE GOES 
# 1. ValueError
userName = raw_input("please enter your name: ")

print int(userName)
### END CODE


# In[3]:

### YOUR CODE GOES 
# 2.TypeError
grade = "third"

print grade+1
### END CODE


# In[7]:

### YOUR CODE GOES 
# 3. IndexError
myDict = {"one":"Mary","Two":"John","Three":"Mike"}

while True:
    try:
        userEnter = int(raw_input("please enter your index: "))
        break
    except IndexError as err:
        print "IndexError encountered"
        continue       
### END CODE


# #### Exercise 3 - Handling Exceptions
# 
# Write a Python program that asks the user to enter a GPA (integer values - 0,1,2,3 or 4). Convert the input from the user into an integer. Write an exception handler to handle the ValueError exception and display the message "ValueError occurred. Please try again". If the value entered by the user is not compatible with integer values the program will raise a ValueError exception and display the message from within the exception handler.

# In[ ]:

### YOUR CODE GOES BELOW

while True:
    try:
        userGPA = int(raw_input("Please Enter your GPA: "))
        break
    except ValueError as err:
        print "ValueErr occured. Please try again"
        continue
### END CODE


# #### Exercise 4 - Displaying the error description in an Exception
# 
# Create a list of **5** items in a grocery cart. For example, your list can be something like the below
# 
# **Example of a list with 2 items:**
# groceryList = ["suger","rice"]
# 
# Write an exception handler to handle an IndexError exceptio and store the details of the exception in a variable called **details**. If the exception occurs, print out a message saying "Exception Occurred" along with the details (from **details** variable). 
# 
# In your program attempt to access the 6th item in the list. 
# 
# Since there are only 5 elements, the exception handler should be triggered and the message printed inside the exception should be printed.

# In[5]:

### YOUR CODE GOES BELOW
details = "Exception Occurred: you are trying to get an item that does not exist in the list, Please try again"

try:
    groceryList =["milk","sugar","rice","cheese","bread"]
    #print groceryList[3]
    print groceryList[6]
    
except IndexError as err:
    print details
### END CODE


# #### Exercise 5 - Using loops to wait for a user to enter a valid value
# 
# **This is a partial repeat of problem 1. You should be able to reuse that code**
# 
# Write a Python program that asks the user to enter a GPA (integer values - 0,1,2,3 or 4). Convert the input from the user into an integer. Write an exception handler to handle the ValueError exception and display the message "ValueError occurred. Please try again". If the value entered by the user is not compatible with integer values the program will raise a ValueError exception and display the message from within the exception handler.
# 
# Place the above code to get user input inside a **while** loop. As long as the user is entering an invalid numeric value, the program should **continue** to prompt the user to enter the GPA. When the user enters a correct value, the program should **break** out of the while loop and print the GPA.
# 
# **Please see classwork for similar examples**

# In[8]:

### YOUR CODE GOES BELOW
while True:
    try:
        userGPA = int(raw_input("Please Enter your GPA: "))
        print "User GPA is:", userGPA
        break
    except ValueError as err:
        print "ValueErr occured. Please try again"
        continue
### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6
# 
# Write a python program to build a simple chatbot. The chatbot will accept input from the user, check the input against a dictionary and display the corresponding value. 
# 
# Below is the dictionary that the chatbot will use.
# 
# ```
# conversationsDict = {
# 'how are you':'I am fine, thank you.How are you today',
# 'i am well':'Cool! How can I help you today',
# 'can you tell me what the weather is like today':'Sure. It looks mostly sunny with a high of 80 degrees',
# 'thank you very much':'You are welcome. Have a nice day'
# }
# ```
# 
# Note that the dictionary **key** is the value entered by the user and the **value** is the response from the chatbot. The chatbot must use the user input to look up the dictionary for a response. If a response is found, then the chatbot must print the response. If the key is Invalid, then a KeyError exception handler must handle the exception displaying the messsage "Sorry, I did not get that". It must then allow the user to repeat the question.

# In[ ]:

### YOUR CODE GOES BELOW


    
### END CODE


# #### Exercise 7
# 
# Write two Python  to compute the average of a list of numbers. The inputs to the function is a python **List**. The output is the average. The function must have an Exception handler to handle the **ZeroDivisionError exception**. 
# 
# Verify that the ZeroDivisionError handler works by passing in an empty list.

# In[7]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 8
# 
# Write a python program that accepts a sequence of words, some of them numbers. Attempt to perform an integer add on all the words that were entered. If a word that is not a number is encountered, use the ValueError to skip the next word. Display the resulting sum of all the numbers.

# In[13]:

### YOUR CODE GOES BELOW


### END CODE

