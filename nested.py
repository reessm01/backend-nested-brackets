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
__author__ = "Scott Reese /w from an amazing instructor"

import sys
openers = ['(', '[', '{', '<', '(*']
closers = [')', ']', '}', '>', '*)']

def reset_counts(counts):
    for key in counts.keys():
        counts[key] = [0, 0]
    return counts

def test_string(line):
    index = 0
    stack = []
    while line:
        char = line[0]
        if line.startswith("(*"):
            char = "(*"
        elif line.startswith("*)"):
            char = "*)"

        index += 1

        if char in openers:
            stack.append(char)
        elif char in closers:
            opener_friend = openers[closers.index(char)]
            if stack.pop() != opener_friend:
                return ("NO", index)

        line = line[len(char):]

    if stack:
        return ("NO", index)
    else:
        return ("YES")

def main(args):
    with open(args[1]) as f:
        for line in f:
            result = test_string(line)
            with open("output.txt", "a") as of:
                of.write(str(result) + "\n")


if __name__ == '__main__':
    main(sys.argv)
