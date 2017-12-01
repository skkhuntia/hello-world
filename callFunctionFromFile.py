#!/usr/bin/python

import sys
import printArgs

returnVal = printArgs.printArguments(sys.argv[1], sys.argv[2], sys.argv[3])
if returnVal==true:
    print("Success")
else:
    print("False")
## Configure SMTP on Jenkins to Test Email Notification
