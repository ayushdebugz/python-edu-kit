
"""
Created on Fri Oct 12 21:47:41 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""
# Program Converting Inches To Cms And vice-versa

print(" 1 - Inches2Cms  >>>")
print("OR")
print(" 2 - Cms2Inches >>>")
c = int(input("Enter Yo Choice :) "))
n = float(input("Enter The Length :"))
          
if(c == 1):
    b = n / 2.54
    print(b, "Inches")

if(c ==2):
    b = n * 2.54
    print(b, "Cms.")


