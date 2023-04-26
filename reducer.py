#!/usr/bin/env python

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into fields
    title, rating = line.split('\t')
    # calculate the length of the title
    length = len(title)
    # emit key-value pair
    print('%d\t%s' % (length, title))
