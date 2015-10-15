import sys
#pythonpath is the default path.
 
sys.path.append("../project/src/") #changes the path so new directories can be added

from functions import *


"""
Author: Silver Bullets
Date:10/03/2015
Description: Tests the sugar Calculator add method for possible vulnerabilites   

"""
def test4():
    
    # X and Y are the test case to be tested in the add method 		
	x=0
	y=7
	
    # Calculates the results of the add method.
	try:
		
		result= add(x, y)
	
		return result
            
            
	except TypeError:
		result= "TypeError"
		
		return result
  
test4()

def main():

	c=test1()
	print(c)


main()
