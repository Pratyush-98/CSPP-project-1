"""Implementing the head shell command in python."""
"""Importing system module"""
import sys
"""importing head and readfile functions from helper library"""
from lib.helper import head, readfile
"""initializing TEXT variable with null value"""
TEXT = None
"""initializing a constant ARG_CNT with a length function which calculates the length of the command line
and reduces length by 1 """
ARG_CNT = len(sys.argv) - 1
"""then by using if condition: if value of ARG_CNT is equal to 0 then an input is given which is stored
TEXT variable"""
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
"""if value of ARG_CNT is equal to 1 then a variable "filename" is created and argv string is stored in 
filename and contents of the filename is stored in TEXT variable """
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
"""if ARG_CNT is greater than 1 then it executes print statement """
if ARG_CNT > 1:
    print("Usage: head.py <file>")
"""it prints head function with TEXT as argument """
print(head(TEXT))
