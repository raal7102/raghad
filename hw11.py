
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 11
# 
# Homework 11 covers plotting with matplotlib/pyplot
# 
# The below sites have some interesting and useful information on working with plots
# 
# * D3 Gallery - https://github.com/d3/d3/wiki/Gallery
# * Minard's Visualizaion of Napolean's 1812 March - https://robots.thoughtbot.com/analyzing-minards-visualization-of-napoleons-1812-march
# * Matplotlib Overview - https://matplotlib.org/users/intro.html
# 
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw10.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# ** Slides ** for Week 11 can be found at 
# 
# https://docs.google.com/presentation/d/1Lz6li1lw7D5_abcG6W68E2rHrtCMgI-cJSA9VokKSi4/edit?usp=sharing
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


# #### Class work
# 
# Week 11 Class Work can be found here
# 
# https://github.com/cis024c/fall2017classwork/tree/master/week11
# 
# The main classwork file is https://github.com/cis024c/fall2017classwork/blob/master/week11/week11_classwork.ipynb

# **Exercise 1 - Testing your knowledge of plots**
# 
# Answer the below questions
# 
# 1. What is the goal of data visualization?
# 2. Why is it critical to ensure that every bit of ink in a visualization contributes to the intended goal?
# 3. What is the difference between a histogram and a barplot?
# 4. Name four types of charts

# << 1. to present the data in graphical format to help in summerizing results, finding trends, also usful incomparing           2. due to cost of ink, it's critical to insure every bit of ink in a visualization contributes to the intended goal
# 3.histogram represents distribution of the numerical data, bar charts rpresents categorical data with rectangular bars proportional to the values they represent
# 4.line chart, bar chart, historgram, pie chart >>

# ** Exercise 2 - Line chart **
# 
# Consider the following dataset of the weights of 7 cars and their corresponding fuel consumption
# 
# ```
# weight = [3170,3455,3222,3983,2441,2500,2390]
# fuel_consumption = [26,30,28,23,36,33,38]
# ```
# 
# 1. Create a line chart that plots the weight of cars against their fuel consumption.
# 2. Comment on your findings. How does fuel consumption change as the weight of the car increases?
# 
# Make sure to add labels and a title to your chart

# In[18]:

### YOUR CODE GOES BELOW
import matplotlib.pyplot as plt

weight = [3170,3455,3222,3983,2441,2500,2390]
fuel_consumption = [26,30,28,23,36,33,38]

plt.xlabel("weight")
plt.ylabel("fuel_consumption")
plt.title("Car weight and it's fuel consumption")

plt.plot(weight,fuel_consumption)
plt.show()

#2. plotting the data is done sequentially, irrespective of the value


### END CODE


# #### Exercise 3 - Scatter Plot
# 
# Consider the following dataset of the weights of individuals and the number of times they used the remote contorl in a period of one hour
# 
# ```
# weight = [121,127,128,131,130,131,133,141,161,167,169,171,173,175,177,181]
# remote_use = [4,3,7,5,3,8,3,4,22,21,17,23,19,22,18,23]
# ```
# 
# 1. Create a scatterplot with the weight on the y-axis and the remote_use variable on the x_axis.
# 2. What can you conclude from the weight the points are distributed on the graph? Does a particular pattern standout?
# 
# Make sure to add labels and a title to your chart
# 

# In[10]:

### YOUR CODE GOES BELOW
#1.

import matplotlib.pyplot as plt

weight = [121,127,128,131,130,131,133,141,161,167,169,171,173,175,177,181]
remote_use = [4,3,7,5,3,8,3,4,22,21,17,23,19,22,18,23]

plt.xlabel("remote_use")
plt.ylabel("weight")
plt.title("Individuals weight relation to frequency of their use of remote control in a period of 1 hour")

plt.scatter(remote_use,weight)
plt.show()

# 2. Individuals with greater weight use the remote control more in a period of 1 hour 


### END CODE


# #### Exercise 4 - Bar Charts
# 
# Consider the following dataset that show the excuses for being late in class and the number of times the excuse was used.
# 
# ```
# excuse = ['No clean pants to wear','thought it was Saturday','forgot to set alarm','too dark, thought it was night','stuck in traffic']
# frequency_of_use = [12,8,26,5,14]
# ```
# 
# Create a bar chart with the excuse on the y axis and the frequency of use on the x axis. Make sure the add labels and a title to the chart.

# In[7]:

### YOUR CODE GOES BELOW
import matplotlib.pyplot as plt
import numpy as np 

plt.close('all')

excuse = ['No clean pants to wear','thought it was Saturday','forgot to set alarm','too dark, thought it was night','stuck in traffic']
strExcuse = np.arange(len(excuse))

frequency_of_use = [12,8,26,5,14]

plt.xlabel("frequency_of_use")
plt.ylabel("excuse")
plt.title("Individuals excuse for being late to a class and the frequnecy")

plt.bar(frequency_of_use,strExcuse)
plt.yticks(strExcuse,excuse)
plt.show()
### END CODE


# #### Exercise 5 -  Creating subplots
# 
# Consider the below data that shows the relationship between scores obtained and hours spent studying a week.
# 
# ```
# hours = [1,2,3,4,5,6,7,8,9,10]
# score = [40,45,50,55,60,65,70,80,90,100]
# ```
# 
# Create 4 subplots in a 2x2 grid, consisting of below four plots
# 
# 1. Histogram of scores.
# 2. Line chart plotting hours on the x_axis and the score on the y_axis
# 3. Bar chart plotting the hours on the x_axis and the score on the y_axis
# 4. A scatter plot with the hours on the x_axis and the score on the y_axis
# 
# Make sure to add labels and a title to each of the charts.

# In[27]:

### YOUR CODE GOES 
import matplotlib.pyplot as plt
import numpy as np 

plt.close('all')

hours = [1,2,3,4,5,6,7,8,9,10]
score = [40,45,50,55,60,65,70,80,90,100]

plt.figure(figsize=(5,5))

#f, axarr = plt.subplots(4)
#axarr[0].hist(score)
#axarr[0].set_title('score to hours of study')
#axarr[1].plot(hours,score)
#axarr[2].bar(hours,score)
#axarr[3].scatter(hours,score)

f, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
ax1.hist(score)
ax1.set_title('hours of study relation to score')
ax2.plot(hours,score,color='r')
ax3.bar(hours,score,color='y')
ax4.scatter(hours,score,color='g')
plt.show()

### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6 -  Pie Plots
# 
# Consider the following distribution of populations of 10 countries in the European Union in 2016 (See https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population)
# 
# ```
# 1	 Germany	82,301,678	
# 2	 France	66,991,000	
# 3	 Italy	60,795,612	
# 4	 Spain	46,468,102	
# 5	 Poland	38,567,614	
# 6	 Romania	19,861,408	
# 7	 Netherlands	17,100,475	
# 8	 Belgium	11,258,434	
# 9	 Greece	10,812,46
# 10	 Czech Republic	10,538,275
# ```
# 
# 1. Create a pie-chart that shows the distribution of populations across the 10 countries
# 2. Comment on your findings
# 3. Why could a pie-chart be problematic when trying to visualize the results

# In[50]:

### YOUR CODE GOES 
#1.
import matplotlib.pyplot as plt
import numpy as np

country = ['Germany','France','Italy','Spain','Poland','Romania','Netherlands','Belgium','Greece','Czech Republic']

population = [82301678, 66991000, 60795612, 46468102, 38567614, 19861408, 17100475, 11258434, 1081246, 10538275]

colors = ['r','g','b','y','aqua','gold','lavender','lime','black','lightcoral']

plt.title("Distribution of populations of 10 countries in the European Union in 2016")

plt.pie(population,labels=country,colors=colors)
plt.show()

# 2. population higher in bigger countries
# 3. pie charts may not be very clear in representing the data which could be confusing sometimes 


### END CODE


# #### Exercise 7 -  Large data sets and sub Plots
# 
# For this exercise you will download historical stock data from the internet from the below link. The data is available at - https://github.com/cis024c/fall2017hw/raw/master/hw11/all_stocks_1yr.csv. The data has the following fields - Date, Open, High, Low, Close, Volume, Name. The Name is the stock ticker or stock symbol.
# 
# Your subplot will involve two plots in a 1X2 grid (1 row and two columns)
# 
# * The first column will show a plot of date versus the price at close
# * The second column show show a plot of date versus the volume
# 
# You will create an interactive way for the user to enter the ticker symbol and then look up for the data corresponding to that symbol and show the corresponding plot for that chart.

# In[ ]:



