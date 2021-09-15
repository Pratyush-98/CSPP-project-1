"""The python code helps to read the command line input for curl method."""
"""Importing system module"""
import sys
"""importing curl function from helper library"""
from lib.helper import curl
"""initializing URL variable with null value"""
URL = None
"""initializing a constant ARG_CNT with a length function which calculates the length of the command line
and reduces length by 1 """
ARG_CNT = len(sys.argv) - 1
"""then by using if condition: if value of ARG_CNT is not equal to 1 then print the print statement"""
if ARG_CNT != 1:
    print('Usage: curl [URL]...')
"""if value of ARG_CNT is equal to 1 then a variable "URL" is created and user speacified url is stored 
in URL"""
if ARG_CNT == 1:
    URL = sys.argv[1]
    """then if the URL variable doesnt have 'http' then it appends http:// to the start of the URL and 
stores in URL variable otherwirse it prints curl function with URL As argument"""
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    print(curl(URL))
