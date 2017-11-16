
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 10
# 
# Homework 10 covers object oriented programming in Python
# 
# The below sites have some interesting and useful information on working with files
# 
# https://drive.google.com/open?id=1OrcpXEmhvgcJxSlchIBsvmXST0lG_uKx
# http://www.tutorialspoint.com/python/python_classes_objects.htm
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw10.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# ** Slides ** for Week 10 can be found at 
# 
# https://docs.google.com/presentation/d/1AigvCKV1yb3PrrcT5xt3IqyAwGpv6IKMNWYUiQ2Oy6k/edit?usp=sharing
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
# Week 10 Class Work can be found here
# 
# https://github.com/cis024c/fall2017classwork/blob/master/week10/week10_classwork.ipynb

# **Exercise 1 - Testing your knowledge of object oriented programming concepts **
# 
# Answer the below questions
# 
# 1. Why do we need classes?
# 2. What is encapsulation?

# <<1.Classes are needed to define and group data and functions and be able to re-use it,add to it 
# 2. Encapsulation is combining all objects into a single class instead of creating ultiple lists and functions >>

# ** Exercise 2 - Class creation **
# 
# Create a Python class named **Employee** with the following attributes and methods
# 
# Data members
# ```
# 1. employeeName  - type string
# 2. employeeAge  - type int
# 3. employeeSalary - type float
# ```
# 
# Methods:
# ```
# 1. getEmployee - returns employee name
# 2. getEmployeeAge - gets the employee age
# 3. getEmployeeSalary - returns the employee salary
# 4. __init__ - initialize method accepts the name, age and salary of the employee
# ```
# 
# Create an object of type Employee and initialize with arbitrary values. Invoke the get methods and display the result.

# In[58]:

### YOUR CODE GOES BELOW
class Employee:

        def __init__(self,employeeName,employeeAge,employeeSalary):
            self.employeeName = employeeName
            self.employeeAge = employeeAge
            self.employeeSalary = employeeSalary

        def getEmployee(self):
            print self.employeeName
            #return self.employeeName
        
        def getEmployeeAge(self):
            print self.employeeAge
            #return self.employeeAge
        
        def getEmployeeSalary(self):
            print self.employeeSalary
            #return self.employeeSalary 
### END CODE


# In[66]:

emp1 = Employee("May",35,"55000")
emp1.getEmployee()
emp1.getEmployeeSalary()
emp1.getEmployeeAge()


# #### Exercise 3 - Private members
# 
# In the above **Employee** class make the employeeName, employeeAge and employeeSalary private so that their access is restricted to only within the class.

# In[73]:

### YOUR CODE GOES BELOW
class Employee:

        def __init__(self,employeeName,employeeAge,employeeSalary):
            self.__employeeName = employeeName
            self.__employeeAge = employeeAge
            self.__employeeSalary = employeeSalary

        def getEmployee(self):
            print self.__employeeName
        
        def getEmployeeAge(self):
            print self.__employeeAge
        
        def getEmployeeSalary(self):
            print self.__employeeSalary
            
emp2 = Employee("John",44,57000)
emp2.getEmployee()
emp2.getEmployeeAge()
emp2.getEmployeeSalary()

### END CODE


# #### Exercise 4 - Adding setters and working with a list of Employees
# 
# In the **Employee** class add the following methods
# 
# ```
# 1. setEmployeeAge - accepts age and sets it in the object
# 2. setEmployeeName - accepts employee name and sets it in the object
# 3. setEmployeeSalary - accepts employee salary and sets it i nthe object
# ```
# 
# Create a list of employees called employeeList. Initialize the list with three objects of type Employee. Initialize the object with the values "None" for employeeName, 0 for employeeAge and 0 for employeeSalary.
# 
# Loop  through each employee in the employeeList. Each time, request the user to enter the name, age and salary of a different employee. Use the set methods to set the name, age and salary for each employee in the employeeList.
# 
# Loop through each employee in the employeeList. Display the name, age and salary of each employee.

# In[2]:

### YOUR CODE GOES BELOW
employeeList = []

class Employee:
    
        def __init__(self,employeeName,employeeAge,employeeSalary):
            self.employeeName = employeeName
            self.employeeAge = employeeAge
            self.employeeSalary = employeeSalary

        def setEmployee(self,employeeName):
            self.employeeName = employeeName
            print self.employeeName
        
        def setEmployeeAge(self,employeeAge):
            self.employeeAge = employeeAge
            print self.employeeAge
        
        def setEmployeeSalary(self, employeeSalary):
            self.employeeSalary = employeeSalary
            print self.employeeSalary

employeeList = [Employee(None,0,0),Employee(None,0,0),Employee(None,0,0)]  

for i in employeeList:
    print i.employeeName, i.employeeAge,  i.employeeAge
    a = raw_input("please employee name: ")
    b = raw_input("please employee age: ")
    c = raw_input("please employee salary: ")
    i.setEmployee(a)
    i.setEmployeeAge(b)
    i.setEmployeeSalary(c)
    print "Employee Name is: ", i.employeeName, "Employee Age is: ", i.employeeAge, "Employee Salary is: ", i.employeeSalary
### END CODE


# #### Exercise 5 -  Creating a Python calculator class
# 
# Create a Python class called Calculator. 
# 
# The class has the following data members
# 
# ```
# 1. number1 - type float
# 2. number2 - type float
# ```
# 
# The class must have the below methods
# 
# ```
# 1. add - adds two numbers and returns the result
# 2. subtract - subtracts the first number from the second number and returns the result
# 3. multiply - multiply two numbers and returns the result
# 4. divide - divide the first number by the second number and returns the result
# 5. __init__ - accepts two numbers and uses those numbers to initialize number1 and number2 respectively
# ```
# 
# Create an object of the Calculator class. Initialize it with any two arbitrary numbers. Invoke the methods add, subtract, multiple and divide and display the result
# 
# 
# 

# In[8]:

### YOUR CODE GOES 
class Calculator:

    def __init__(self,number1,number2):
        self.number1 =float(number1)
        self.number2 =float(number2)
    
    def add(self):
        print self.number1 + self.number2
    
    def subtract(self):
        print self.number1 - self.number2
    
    def multiply(self):
        print self.number1 * self.number2
    
    def divide(self):
        print self.number1 / self.number2
    
num1 = Calculator(2.7,3.1)
num1.add()
num1.subtract()
num1.multiply()
num1.divide()
### END CODE


# In[ ]:



