{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#mapper.py:\n",
    "\n",
    "#!/usr/bin/env python\n",
    "\n",
    "import sys\n",
    "\n",
    "# input comes from STDIN (standard input)\n",
    "for line in sys.stdin:\n",
    "    # remove leading and trailing whitespace\n",
    "    line = line.strip()\n",
    "    # split the line into fields\n",
    "    fields = line.split('\\t')\n",
    "    # extract movie id and title\n",
    "    movie_id = fields[0]\n",
    "    title = fields[1]\n",
    "    # extract rating\n",
    "    rating = fields[2]\n",
    "    # emit key-value pair\n",
    "    if int(rating) >= 10:\n",
    "        print('%s\\t%s' % (title, rating))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
