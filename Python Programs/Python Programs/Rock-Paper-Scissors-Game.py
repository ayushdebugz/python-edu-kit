############################################################### --|Programme By Ayush Jha (XII-A)|
"""@author: AyusH Jha
Github: https://github.com/ayushdebugz """

import time
from time import sleep
import random


# ROCK PAPER SCISSORS GAME
########## --Game Characters :Creation/Value Declrn.

sus="-"*69
gchrtr=["ROCK","PAPER","SCISSORS"]
p = 0   ########### --Player's Score
s = 0   ########### --CPU's Score

z=str(input("ENTER PLAYER NAME:"))    ######### --Input From User As Name
print('OK ,',z)
while True:
    x=input("ROCK,PAPER,SCISSORS ?:")    ############## --Entering Ur Character
   
    if x not in gchrtr:
        print("INVALID CHARACTER ,BUDDY!" )    ######### --In Case If Not From Gchrtr 
        continue

############################################################### -- Guessing All of The Possiblities
############################################################### -- Game Points Mechanism
    pc=random.choice(gchrtr)
    sleep(0.1)                   ######## -- Sleep Time (LOW) For Instant Results 
    print(("Computer Picked {}.").format(pc))
    if x==pc:
        sleep(0.1)
        print(('\nIts A Draw.\n{}').format(sus))
        print(z,",Your Score:",p,"Pcscore:",s  )
    elif x=="ROCK" and pc=="SCISSORS":
        sleep(0.1)
        print(('\nYou win,ROCK beats SCISSORS\n{}').format(sus))
        p =+1
        print(z,",Your Score:",p,"|Pcscore:",s  )
    elif x=='PAPER' and pc=='ROCK' :
        sleep(0.1)
        print(('\nYou win.PAPER beats ROCK\n{}').format(sus))
        p =+1
        print(z,",Your Score:",p,"|Pcscore:",s  )
    elif x=="SCISSORS" and pc=="PAPER":
        sleep(0.1)
        print(('\nYou win.SCISSORS beats PAPER\n{}').format(sus))
        p =+1
        print(z,",Your Score:",p,"|Pcscore:",s  )
    else:
        sleep(0.1)
        print(('\nYOU lose. {} beats {} \n{}').format(pc,x,sus))
        s =+1
        print(z,",Your Score:",p,"|Pcscore:",s  )

########################################################################## --To Terminate Or Continue
def play(a):
      if(p,s == 10,10):
          a=input("Continue ? Press 'Y' , Or, 'y'")
      if(a=='Y','y'):
          print("LOADING GAME ,PLEASE WAIT ......")
          sleep(0.1)
          return True
      else:
          print("THANKS FOR PLAYIN' ," ,z, "HAVE A NICE DAY!")
    


        


#Player ID:
#5487002943
#Nickname:
   
