"""
Created on Fri Oct 12 20:34:41 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""

# Program To Calculate Area Of Circle


x=float(input("Enter The Radius Of The Circle:"))
print(x)
if(x<=0):
    print("HeY WaiT!..")
    print("Error Command Radius: Radius Won'T B NegativE!",x)
    print("NO Thanks!")
else:
    print("Ok...")
    a=3.14*x*x
    print("Area Of Circle With Radius Given Is:")
    print(a)
    print("Thanks!:")
