{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#reducer.py:\n",
    "\n",
    "#!/usr/bin/env python\n",
    "\n",
    "import sys\n",
    "\n",
    "# input comes from STDIN\n",
    "for line in sys.stdin:\n",
    "    # remove leading and trailing whitespace\n",
    "    line = line.strip()\n",
    "    # split the line into fields\n",
    "    title, rating = line.split('\\t')\n",
    "    # calculate the length of the title\n",
    "    length = len(title)\n",
    "    # emit key-value pair\n",
    "    print('%d\\t%s' % (length, title))"
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
