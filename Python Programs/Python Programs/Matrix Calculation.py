"""
Created on Fri Oct 12 20:34:41 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""
#Program To Calculate Matrices Multiplications

br='\n' 
import time 
from time import sleep 

print("Hello, Voila! AMIGO!," + br +"Presenting Matrix Calculator By AYUSH JHA! ")
sleep(1)
n = int(input('Enter Order Of Matrix:' ))
  
print('Ok')

print('Start Entering Elements Of Matrices:')

  
def twt(n):
    print('1st Matrix>>>')
    E11 =int(input(''))
    E12 =int(input(''))
    E21 =int(input(''))
    E22 =int(input(''))

    if(E11,E12,E21,E22 == '','','','' ):
        print('This Is 1st Matrix:')
        print('[ ',(E11),(E12),' ]') 
        print('[ ',E21, E22,' ]')
    else:
        print('Enter All Elements:')

    print('2nd Matrix>>>')
    F11 =int(input(''))
    F12 =int(input(''))
    F21 =int(input(''))
    F22 =int(input(''))

    if(F11,F12,F21,F22== '','','',''):
        print('This Is 2nd Matrix:')
        print('[ ',F11, F12,' ]') 
        print('[ ',F21,F22,' ]')
    else:
        print('Enter All Elements:')
        
    print('Hold On eh.. ')   
    sleep(2)
    print('Now Multiplying:')
    sleep(2)


    G11 = (E11*F11) + (E12*F21)
    G12 = (E11*F12) + (E12*F22)
    G21 = (E21*F11) + (E22*F21)
    G22 = (E21*F12) + (E22*F22)

    print('Therefore, Required Matrix Is:')

    print(G11, G12)
    print(G21, G22)

    print('Done    !')
    return ('Huh!, Solved!', n)
if(n== 2):
  print(twt(n))

