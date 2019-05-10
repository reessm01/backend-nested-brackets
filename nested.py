#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: This program evaluates a file for valid nested brackets.
Included brackets:
(  )
[  ]
{  }
<  >
(*  *)
"""
__author__ = "Scott Reese"

import sys


def reset_counts(counts):
    for key in counts.keys():
        counts[key] = [0, 0]
    return counts


def main(text):
    counts = {"paran": [0, 0], "squares": [0, 0], "curlies": [
        0, 0], "brackets": [0, 0], "eyes": [0, 0]}
    closures = {'(': "paran", ')': "paran", '[': "squares", ']': "squares",
                '{': "curlies", '}': "curlies", '<': "brackets", '>': "brackets", "*": "eyes"}

    with open(text, 'r') as f:
        line = f.readline()
        while len(line) > 0:

            skip = False
            counts = reset_counts(counts)
            index = 0
            stop = False
            for char in line:

                if char in closures.keys():

                    if char is "(" and line[index + 1] == "*":
                        counts["eyes"][0] += 1
                        counts["eyes"][1] = index
                        counts["paran"][0] += 1
                        counts["paran"][1] = index

                    elif char is "*" and line[index + 1] == ")":
                        counts["eyes"][0] -= 1
                        counts["eyes"][1] = index
                        counts["paran"][0] -= 1
                        counts["paran"][1] = index

                    elif char in ['(', '[', '{', '<']:
                        counts[closures[char]][0] += 1
                        counts[closures[char]][1] = index

                    else:
                        counts[closures[char]][0] -= 1
                        counts[closures[char]][1] = index
                index += 1
            values = counts.values()
            for value in values:
                print(value)
                if value[0] != 0:
                    with open("output.txt", "a") as file:
                            string = "NO " + str(value[1]) + "\n"
                            file.write(string)
                    break
                else:
                    with open("output.txt", "a") as file:
                        string = "YES" + str(counts) + "\n"
                        file.write(string)
                        break
            line = f.readline()


if __name__ == '__main__':
    # main(sys.argv)
    main("input.txt")
