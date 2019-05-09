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
        counts[key] = 0
    return counts


def main(args):
    counts = {"paran": 0, "squares": 0, "curlies": 0, "brackets": 0, "eyes": 0}
    closures = {'(': "paran", ')': "paran", '[': "squares", ']': "squares",
                '{': "curlies", '}': "curlies", '<': "brackets", '>': "brackets"}

    with open(args[1], 'r') as f:
        line = f.readline()
        while len(line) > 0:
            counts = reset_counts(counts)
            index = 0
            stop = False
            for char in line:
                if char in closures.keys():
                    if char is "(" and line[index + 1] == "*":
                        counts["eyes"] += 1
                    elif char is "*" and line[index + 1] == ")":
                        counts["eyes"] -= 1
                    elif char in ['(', '[', '{', '<']:
                        counts[closures[char]] += 1
                    else:
                        counts[closures[char]] -= 1
                for value in counts.values():
                    if value < 0:
                        stop = True
                        with open("output.txt", "a") as file:
                            string = "NO " + str(index) + "\n"
                            file.write(string)
                        break
                if stop:
                    break
                index += 1
            if not stop:
                with open("output.txt", "a") as file:
                    string = "YES" + "\n"
                    file.write(string)
            line = f.readline()


if __name__ == '__main__':
    main(sys.argv)
