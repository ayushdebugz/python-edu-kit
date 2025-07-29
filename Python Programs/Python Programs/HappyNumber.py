"""
Created on Fri Oct 12 20:34:41 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""

# Python program to check a number is a Happy number or not 
# A happy number is a positive integer that eventually reaches 1 when repeatedly replaced by the sum of the squares of its digits. 
# If the process results in an infinite loop that does not include 1, the number is considered unhappy (or sad). 

def numSquareSum(n): 
	squareSum = 0; 
	while(n): 
		squareSum += (n % 10) * (n % 10); 
		n = int(n / 10); 
	return squareSum; 
def isHappynumber(n): 
	slow = n; 
	fast = n; 
	while(True): 
		slow = numSquareSum(slow); 
		fast = numSquareSum(numSquareSum(fast)); 
		if(slow != fast): 
			continue; 
		else: 
			break; 
	return (slow == 1); 
while 0==0:
	n =int(input("Enter n e number :")); 
	if (isHappynumber(n)): 
		print(n , "is a Happy number")
	else:
		print(n , "is not a Happy number"); 

