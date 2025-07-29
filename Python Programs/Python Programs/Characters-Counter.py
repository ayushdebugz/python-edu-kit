"""
Created on Fri Oct 12 21:03:54 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""
# Program "Counting Digits & Alphabets"

x=input("Enter Input:")
count1=0
count2=0
count3=0
for i in x:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The Number Of Digits Is>>>")
print(count1)
print("The Number Of Characters Is>>>")
print(count2)