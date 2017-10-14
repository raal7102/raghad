
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 5
# 
# Homework 5 covers exercises that involve working with files
# 
# The below sites have some interesting and useful information on working with files
# 
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw5.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# <h3><font color='red'>
# ALL THE WORK THAT WE DID IN CLASS DURING WEEK 5 IS NOW IN GITHUB AT THE BELOW LINK
# </font></h3>
# 
# https://github.com/cis024c/fall2017classwork/blob/master/week5/working_with_files.ipynb
# 
# ** Slides ** for Week 5 can be found at 
# 
# https://docs.google.com/presentation/d/16cRqqIoZl15gX5QC2oEvS8NuUiPrhzOyC5UerGpuWOM/edit?usp=sharing
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


# #### Sample Exercises with conditionals and repetitions
# 
# Refer to Week 5 classwork for sample exercises - 
# 
# https://github.com/cis024c/fall2017classwork/tree/master/week5

# **Exercise 1 - Testing your knowledge of files **
# 
# Answer the below questions
# 
# 1. In your own words, describe what a **file** is?
# 2. Why is it important to close a file after we are done using it?

# << a file is used to stor information, it's important to close a file soit doesn't get overwritten the next time its opened for reading  >>

# #### Exercise 2 -  Write to a file
# 
# Write a python program to write the below lines to a file
# 
# - Name, Age, Gender, Profession
# - Harry, 23, Male, Software Engineer
# - Sam, 25, Male, Lawyer
# - Lisa, 29, Female, Computer Scientist
# - Mary, 22, Female, Doctor
# 
# Below are a set of recommended steps to accomplish this
# 1. open a file in write mode. This will return a handle to the file
# 2. use the write method to write each line to the file using the file handle returned in the open call
# 3. close the file when done
# 
# Once done, go to the folder where the file is and open it to make sure that this is written.
# 
# Refer to class exercises especially "In [22]" in https://github.com/cis024c/fall2017classwork/blob/master/week5/working_with_files.ipynb

# In[20]:

### YOUR CODE GOES 
writeFile = open("users_info.txt","w")

writeFile.write("Name,Age,Gender,Profession\n")
writeFile.write("Harry,23,Male,Software Engineer\n")
writeFile.write("Sam,25,Male,Lawyer\n")
writeFile.write("Lisa,29,Female,Computer Scientist\n")
writeFile.write("Mary,22,Female,Doctor\n")

writeFile.close()
### END CODE


# #### Exercise 3 - Reading from a file
# 
# Read and display the data from the file you had just written to.
# 
# Below are a set of recommended steps to accomplish this
# 1. open the file in read mode. This will return a handle to the file.
# 2. You can now iterate through each line in the file  and then use readline to read each line.
# 3. Display each line as you read it in
# 
# Note that you can also use the **read** method to read in all lines or the **readlines** method to read all lines into a list.

# In[21]:

### YOUR CODE GOES BELOW
fileRead = open("users_info.txt")

for line in fileRead:
    print line

### END CODE


# #### Exercise 4 - Finding the average age of users in a file
# 
# Write a python program to find the average age of users in the file you just created.
# 
# Below are a set of recommended steps to accomplish this
# 1. Open the file in read mode
# 2. Read in each line of the file
# 3. Split each line in the file to get the age
# 4. Find the average age and display it

# In[49]:

## YOUR CODE GOES BELOW
fileRead = open("users_info.txt")

userAge = 0
sumAge = 0
loopcount = 0

for line in fileRead:
    if loopcount != 0:
        lineField = line.split(",")
        userAge = userAge + int(lineField[1])
    loopcount = loopcount + 1
avgAge = userAge/(loopcount-1)
print "Averge Age is: ", avgAge
### END CODE


# #### Exercise 5 - Appending to a file
# 
# Write a python program to append information provided by users to an existing file. 
# 
# You will need to 
# 1.  ask the user to enter their name, age, gender and profession using the **raw_input** method (for Python 3 users, you will use the **input** method).
# 2.  open the file you just created in the above exercies in append mode and write this information to the file.
# 
# Remember to make sure that the information you append is entered in the same format where each field is separated by commas.
# 
# 

# In[55]:

### YOUR CODE GOES BELOW
userInfo = raw_input("Please Enter your name,age,gender and profession: ")

openFile = open("users_info.txt","a+")
openFile.write(userInfo)
openFile.close()

### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### NOTE 
# 
# For this program you will need to download the full text of Alice in Wonderland. This is available at this link http://www.gutenberg.org/files/11/11-0.txt
# 
# For MAC users, you can download this directly from Jupyter by executing the below cell. Windows users might need to click on the link and download the file and save it to your computer. 

# In[21]:

# download alice text
get_ipython().system(u"curl 'http://www.gutenberg.org/files/11/11-0.txt' -o aliceText.txt")


# #### Exercise 6
# 
# Write a program to read the file aliceText.txt and count the number of times that the word "house" occurs in the text.

# In[22]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 7
# 
# Write a python program to read the file aliceText.txt and find 
# 
# * the number of characters in the file
# * the number of words in the file
# * the number of lines in the file
# 
# Display the result

# In[24]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 8
# 
# Write a Python program to read the file aliceText.txt and find the top 10 most frequent words in the file. Display the result
# 
# Below are recommended steps for this program
# 
# * Read the contents of the file
# * Initialize a dictionary to maintain the counts of each word
# * Loop through each word in the file
#     - If the word is new, then add to dictionary and initialize count to 1 for this word
#     - If the word is already in the dictionary, then increment the count of that word by 1
# * Use the **sorted** method to sort all values in descending order  - See the **example** code at the end of this assignment for an example on sorting a dictionary in reverse order by value

# In[25]:

### YOUR CODE GOES BELOW


### END CODE


# #### Example code for sorting a dictionary by value in reverse order

# In[26]:

myDict = {'seven': 7, 'four': 4, 'one': 1, 'two': 2, 'five': 5, 'eight': 8} 
sortedDict = sorted(myDict, key=myDict.get, reverse=True)

for key in sortedDict:
    print key,myDict[key]


# In[ ]:



