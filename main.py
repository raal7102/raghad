import sys
import helper

#print "Number of arguments: ", len(sys.argv), 'arguments'
#print "Argument List:", str(sys.argv)

userNumber1 = int(sys.argv[1])
userNumber2 = int(sys.argv[2])
sum = userNumber1+userNumber2

print "The sum of the two numbers you entered is:", helper.add(userNumber1,userNumber2)