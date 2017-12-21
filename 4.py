import sys
import os.path
import math
import numpy
#import matplotlib.pyplot as plt

def isAnagram(addedWord, word):
    return sorted(addedWord) == sorted(word)

def containsAnagram(added, word):
    for addedWord in added:
        if isAnagram(addedWord, word):
            return True
    return False

if __name__ == '__main__':
    with open("f", "r") as f:
        lines = f.readlines()

    valid = 0

    for line in lines:
        words = line.split()
        added = []
        lineValid = True
        for word in words:
            # if word in added:
            if containsAnagram(added, word):
                lineValid = False
                break
            else:
                added.append(word)
        if lineValid:
            valid += 1

    print(valid)