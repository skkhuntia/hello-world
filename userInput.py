#!/usr/bin/python

var = raw_input("Please enter something: ")
print "you entered", var
limit = int(var)
s = 0
for i in range(limit):
    s +=i
print("Sum: " + str(s))
