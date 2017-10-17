tf-idf
======

Implementation of td-idf algorithm

Pre-requisites
--------------

Python3 >= 3.6.2


Usage
-----

`tf-idf.py [-l] [-n] -f [...]`

- -l is optional and it is for the “stop words” file.
- -n is optional and it is for the number of meaningful words to display, if none is given it will display 3 by default.
- -f est mandatory and it is for the files to calculate tf-idf.

Example : `python3 tf-idf.py -l english -f text1 text2 text3`
