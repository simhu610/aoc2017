import sys
import os.path
import math
import numpy
import matplotlib.pyplot as plt


if __name__ == '__main__':
    with open("input5.txt", "r") as f:
        lines = f.readlines()

    instructions = [int(i) for i in lines]
    print len(instructions)

    i = 0
    steps = 0

    while i >= 0 and i < len(instructions):
        old_i = i
        i += instructions[i]
        if instructions[old_i] >= 3:
            instructions[old_i] -= 1
        else:
            instructions[old_i] += 1
        steps += 1

    print steps