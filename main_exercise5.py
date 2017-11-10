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

