#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into fields
    fields = line.split('\t')
    # extract movie id and title
    movie_id = fields[0]
    title = fields[1]
    # extract rating
    rating = fields[2]
    # emit key-value pair
    if int(rating) >= 10:
        print('%s\t%s' % (title, rating))
  
