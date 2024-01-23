#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s_split = s.split(":")
    print(s_split)
    i = s_split[-1][2:]
    print(i)
    
    if i == "PM":
        # adding 12 to hours
        if s_split[0] == '12':
            s_split[0] = '12'
            
        else:
            s_split[0] = str(int(s_split[0]) + 12)        
        
        # removing the AM and PM 
        s_split[-1] = s_split[-1][0:2]
    
        print(s_split)
        
        
    else:
        # removing the AM and PM 
        s_split[-1] = s_split[-1][0:2]
        # if its 24 then it needs to flip to 0.
        if s_split[0] == '12':
            s_split[0] = '00'
    
    new_value = ":".join(s_split)
    
    print(new_value)
    
    return new_value    

s = "12:01:45AM"

timeConversion(s)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()
