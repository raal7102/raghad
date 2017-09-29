
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 3
# 
# Homework 3 covers exercises in String Manipulation. 
# 
# For a list of features supported in the string module, please refer to this URL https://docs.python.org/2/library/string.html
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw3.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# <h3><font color='red'>
# ALL THE WORK THAT WE DID IN CLASS DURING WEEK 3 IS NOW IN GITHUB AT THE BELOW LINK
# </font></h3>
# 
# https://github.com/cis024c/fall2017classwork/blob/master/week3/week3_classwork.ipynb
# 
# ** Slides ** for Week 3 can be found at https://docs.google.com/presentation/d/16z1-Ln71MiXMRfgnZJB60mnXWnwCiUn0gHURe9KMMWg/edit?usp=sharing
# 
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

# In[ ]:

get_ipython().system(u'python --version')


# #### Sample Exercises with conditionals and repetitions
# 
# Refer to Week 2 classwork 2 for sample exercises - https://github.com/cis024c/fall2017classwork/blob/master/week2/week2.ipynb

# #### Exercise 1 -  Using logical operators - and, or and not
# 
# Get the ages of three persons Harry, Sally and Mary from the user. Check the below conditions and display the results
# 
# 1. If Harry and Sally are both less than 20 years old, display the message saying "Harry and Sally are less than 20 years old"
# 2. If either Sally or Mary is older than 30, then display the message saying "Either Sally or Mary is older than 30"
# 
# Remember that to do this you will need to use different variables to store the respective ages and then evaluate those ages using the if statement and logical operators.

# In[ ]:

### YOUR CODE GOES 
userAge1 = int(raw_input("Enter your Age Harry: "))
userAge2 = int(raw_input("Enter your Age Sally: "))
userAge3 = int(raw_input("Enter your Age Mary: "))

if userAge1 and userAge2 < 20:
    print "Harry and Sally are less than 20 years old"
else:
    if userAge2 or userAge3 > 30:
        print "Either Sallyor Mary is older than 30"
### END CODE


# #### Exercise 2 - Find the length of a given string
# 
# Ask the user to enter their first name. Compute the number of characters in the first name and print the result. 
# 
# Note that you will need to use the ** len ** function to obtain the number of characters in the string.

# In[ ]:

### YOUR CODE GOES BELOW
userFirstName = raw_input("Enter your first name: ")
print "Your first name has %s characters" % (len(userFirstName))
### END CODE


# #### Exercise 3 - Reversing a String
# 
# Ask the user to enter the name of their favorite movie. Reverse the name of the movie and print it out.

# In[ ]:

### YOUR CODE GOES BELOW
userMovie = raw_input("Enter your favourite movie:")

print "Your favourite movie name reversed is", userMovie[::-1]
### END CODE


# #### Exercise 4 - Converting an input string to lower case and looking for a match
# 
# Ask the user to enter a **line of text** and a **search string**. Convert the line of text that the user entered to lower case. Search the resulting text for the search string. Print "Search String Found" if the search string was found, otherwise, print "Search String not found"
# 
# For example, the user could enter "Jack and Jill went up the Hill" and the search string "jill". You first need to convert the input string to lower case like so - "jack and jill went up the hill". 
# 
# Next you will need to look for the search string in the input string. You can use the "if searchString in text" form of query to determine if the text contains the search string. See week 3 classowork for an example

# In[ ]:

### YOUR CODE GOES BELOW
userText = raw_input("Enter your text: ")
searchString = raw_input("Enter search string: ")

userTextLower = userText.lower()

if searchString in userTextLower:
    print "Search String Found"
else:
    print "Search String not found"
### END CODE


# #### Exercise 5 - Parsing a comma separated set of values
# 
# Ask the user to type in a grocery list. Ensure that each item in the grocery list is separated by a comma. Use the **split** command to extract each token (item) in the grocery list. Print the last item in the list.
# 
# For example, if the user enters "milk,bananas,sugar,eggs,cheese", you will need to read this into a variable, parse the contents using the **split** command and print "cheese"

# In[2]:

### YOUR CODE GOES BELOW
groceryList = raw_input("Enter your comma separated grocery list: ")

items = groceryList.split(",")

print "Last item in the list is: ",items[-1]

### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6
# 
# Ask the user to type in a grocery list and a search item. Ensure that each item in the grocery list is separated by a comma and an arbitrary number of spaces. Use the **split** command to search for the search item in this list. 
# 
# For example, let us say that the user enters ""milk ,  bananas,  sugar,  eggs,  cheese  " (notice the arbitrary spaces between items) and the search term is "eggs". You will need to look for "eggs" in the grocery list and if found, print the message "Item found", otherwise, print "Item not found"

# In[16]:

### YOUR CODE GOES BELOW
groceryList = raw_input("Please enter your comma separated grocery list: ")

searchItem = raw_input("Please enter search item: ")

newGroceryList = groceryList.replace(" ","")
items = newGroceryList.split(",")

if searchItem in  items:
    print "Item found"
else:
    print "Item not found"
### END CODE


# #### Exercise 7
# 
# Write a python program that takes in a list of words from the user and prints the shortest word in the list. If two words are equal short, just pick the first one that you see.
# 

# In[ ]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 8
# 
# Accept a line of text from the user with some repeating words. Ask the user to enter a search term (one of the repeating words). Count the number of times the search term repeats in the text.
# 
# For example, if the sentence is - "She sells sea shells on the sea shore" and the search term is "sea", then the program should print the result 2, indicating that two occurrences of the word "sea" were found in the text
# 

# In[18]:

### YOUR CODE GOES BELOW

### END CODE


# #### Exercise 9
# 
# Write a python program to get text from the user. Create a new text from the original text with the word " stranger " inserted in the middle of the text. Print the resulting new text.

# In[ ]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 10
# 
# Write a python program to get a line of text from the user. Sort each word in the text alphabetically and print it out. 
# 
# For example, if the user enters "Jack and Jill went up the hill", the result should be "and Jack Jill hill the up went"
# 

# In[ ]:

### YOUR CODE GOES BELOW


### END CODE

