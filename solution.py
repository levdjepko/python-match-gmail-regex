#!/bin/python3

import math
import os
import random
import re
import sys

def useRegex(input):
    # regex pattern
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@gmail.com')
    return pattern.match(input, re.IGNORECASE)

if __name__ == '__main__':
    N = int(input().strip())
    setOfNames = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]        
        emailID = first_multiple_input[1]
        if(useRegex(emailID)):
            setOfNames.append(firstName)
    setOfNames.sort()
    for i in range(len(setOfNames)):
        print (setOfNames[i])       
        
