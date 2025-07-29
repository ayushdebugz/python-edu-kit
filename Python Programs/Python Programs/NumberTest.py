"""
Created on Fri Oct 12 20:34:41 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""
#Program To Determine Minimum, Average & Maximum NUM

A=int(input("Enter A Number:"))
B=int(input("Enter A Number:"))
C=int(input("Enter A Number:"))
if A>B:
    if A>C:
        HIGH=A
        if B>C:
            MID=B
            SMALL=C
        else:
            MID=C
            SMALL=B
    else:
        HIGH=C
        MID=A
        SMALL=B
else:
 if B>C:
       HIGH=B
       if A>C:
           MID=A
           SMALL=C
       else:
           SMALL=A
           MID=C
 else:
      HIGH=C
      SMALL=A
      MID=B
print("\n SmallesT NumbeR:\n",SMALL)
print("\n NexT HigheR NumbeR:\n",MID)
print("\n HighesT NumbeR:\n",HIGH)

print("\nThanks!!!!!\n")



      
    