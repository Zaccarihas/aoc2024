#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils
import re
import collections
import functools  # reduce

#DATAFILE = 'AOC-2024-02/test.txt'
DATAFILE = 'AOC-2024-02/input.txt'

def safe(report):
    if (report[0] < report[1]):
        report.reverse()

    pairs = zip(report[:-1],report[1:])

    checks = map(lambda p: (p[0]-p[1]) >=1 and (p[0]-p[1]) <=3, pairs)
    return functools.reduce(lambda x,y: x and y, checks)

def firstStar(pdata):

    # Initiate the first answer
    answer = 0

    for report in pdata:

        if safe(report):
            answer += 1

    # SOLVE    
    
    # Print the first answer
    print ("Answer 1: ", answer)

def secondStar(pdata):

    # Initiate the second answer
    answer = 0
    
    for report in pdata:
    
        # Decrease normal riktning


        if safe(report):
            answer += 1
        else:
            print("Not safe report - testing to remove levels")
            for idx in range(len(report)):
                print(f"Remove level {idx}")
                testreport = report[:]
                print(f"Report copy: {testreport}")
                testreport.pop(idx)
                if safe(testreport):
                    answer += 1
                    break

    
    # Print the second answer
    print ("Answer 2: ", answer)

    
if __name__ == "__main__":
    # Get input from file
    pdata = utils.fileLines(DATAFILE)

    if pdata != utils.ERROR_INDICATOR:

        # Transform data 
        
        intdata =  [rep.split(" ") for rep in pdata]
        pdata = [list(map(int, x)) for x in intdata]


        #firstStar(pdata)
        secondStar(pdata)

    else:
        print ("Input data could not be retrived!") 