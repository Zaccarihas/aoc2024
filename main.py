#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils
import re
import collections
import functools  # reduce

#DATAFILE = 'AOC-2024-03/test.txt'
DATAFILE = 'AOC-2024-03/input.txt'

def firstStar(pdata):

    # Initiate the first answer
    answer = 0

    p = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
    
    for sec in pdata:
        m = p.finditer(sec)
       
        for match in m:
            answer += int(match.group(1)) * int(match.group(2))

        

    # Print the first answer
    print ("Answer 1: ", answer)


def secondStar(pdata):

    # Initiate the second answer
    answer = 0
    
    p = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don\'t\(\)')
    
    antal = 0
    do = True
    for sec in pdata:
        m = p.finditer(sec)
       
        for hit in m:
            match hit.group(0):
                case "do()":
                    do = True
                case "don't()":
                    do = False
                case _:
                    if do:
                        answer += int(hit.group(1)) * int(hit.group(2))          
    
    # Print the second answer
    print ("Answer 2: ", answer)

    
if __name__ == "__main__":
    # Get input from file
    pdata = utils.fileLines(DATAFILE)

    if pdata != utils.ERROR_INDICATOR:

        # Transform data 

        firstStar(pdata)
        secondStar(pdata)

    else:
        print ("Input data could not be retrived!") 