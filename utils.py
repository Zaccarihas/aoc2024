#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ERROR_INDICATOR = -1

def strList2IntList(strList):
    """
    Convert a given list of strings to a list of integers
    """
    return [int(i) for i in strList]


def cleanItem(wrd, letterset):
    """
    Filter out only letters in a given word and return it in lower case
    """
    return ''.join(character for character in wrd.lower() if character in letterset)

def getFileInput(filename):
    """
    Filter out only letters in a given word and return it in lower case
    """
    try:
        # Open the file
        with open(filename) as fhandle:
            return fhandle.read()

    except IOError:
        return ERROR_INDICATOR

def fileLines(filename, clear = False):
    """
    Return all the lines of a given file as a list
    """
    content = getFileInput(filename)

    if content != ERROR_INDICATOR:

        # Convert the content to a list of lines
        if clear:
            return [line for line in content.splitlines() if line != '']
        else:
            return [line for line in content.splitlines()]

    return ERROR_INDICATOR

def fileWords(filename):
    """
    Return all the words of a given file as a list
    """
    content = getFileInput(filename)

    if content != ERROR_INDICATOR:

        # Convert the content to a list of words
        return content.split()
    
    return ERROR_INDICATOR

def fileChars(filename):
    """
    Return all the characters of a given file as a list
    """
    content = getFileInput(filename)

    if content != ERROR_INDICATOR:

        # Convert the content to a list of words
        return list(content)
    
    return ERROR_INDICATOR

def frequency(dataset):
    """
    Make a frequency list for the dataset
    """
   
    # Initiate by creating a dictonary
    itemDict = dict()
       
    # Count each item in the dictonary
    for item in dataset:
        # item = cleanItem(item)
        itemDict[item] = itemDict.get(item, 0) + 1

    # Sort the dictonary
    resultList = list()
    for item, count in itemDict.items():
        resultList.append((count, item))
    resultList.sort(reverse=True)
    
    # Extract the top ten items
    # resultList = resultList[:10]
        
    # Return the result
    return resultList
