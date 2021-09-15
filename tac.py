"""Implementing the tac shell command in python."""
"""Importing system module"""
import sys
"""importing tac and readfile functions from helper library"""
from lib.helper import tac, readfile
"""initializing TEXT variable with null value"""
TEXT = None
"""initializing a constant ARG_CNT with a length function which calculates the length of the command line
and reduces length by 1 """
ARG_CNT = len(sys.argv) - 1
"""then by using if condition: if value of ARG_CNT is equal to 0 then an input is given which is stored
TEXT variable"""
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
"""if ARG_CNT is equal to 1 then a variable "filename" is created and argv string is stored in filename
 and contents of the filename is stored in TEXT variable """
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
"""if ARG_CNT is greater than 1 then it executes print statement which writes file name and prints the 
statement"""
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
"""it prints tac function with TEXT as argument """
print(tac(TEXT))
