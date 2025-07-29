"""
Created on Sat Feb 23 10:27:18 2019

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""


# PrograM Sorting Elements By 'ID' Using Tuples 


tup=[(103,'Ritika',3001),(104,'John',2819),(101,'Razia',3451),(105,'Tarandeep',2971)]
print("B 4 SortinG:",tup)
for i in range (len(tup)):
    for j in range(0,len(tup)-i-1):
        if tup[j][2]<tup[j+1][2]:
            tup[j],tup[j+1]=tup[j+1],tup[j]
print("After SortinG:",tup)
