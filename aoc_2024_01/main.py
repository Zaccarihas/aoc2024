#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils
import re
import collections
import functools  # reduce

DATAFOLDER = 'AOC-2024-01/'
#DATAFILE = 'test.txt'
DATAFILE = 'input.txt'
WORDLENGTH = 5

def firstStar(pdata):

    # Initiate the first answer
    answer = 0

    lst_left = []
    lst_right = []

    for pair in pdata:
        lst_left.append(int(pair[:WORDLENGTH]))
        lst_right.append(int(pair[-WORDLENGTH:]))

    lst_left.sort()
    lst_right.sort()

    zipped= zip(lst_left, lst_right)
    
    for pr in zipped:
        dist = abs(pr[0]-pr[1])
        answer += dist
    
    # Print the first answer
    print ("Answer 1: ", answer)


def secondStar(pdata):

    # Initiate the second answer
    answer = 0
    
    lst_left = []
    lst_right = []

    for pair in pdata:
        lst_left.append(int(pair[:WORDLENGTH]))
        lst_right.append(int(pair[-WORDLENGTH:]))

    cnt_r = collections.Counter(lst_right)
    
    for itm in lst_left:
        answer += itm * cnt_r[itm]
    
    # Print the second answer
    print ("Answer 2: ", answer)

    
if __name__ == "__main__":
    # Get input from file
    pdata = utils.fileLines(DATAFOLDER + DATAFILE)

    if pdata != utils.ERROR_INDICATOR:

        # Transform data 

        firstStar(pdata)
        secondStar(pdata)

    else:
        print (f"Input data could not be retrived! {pdata}") 
