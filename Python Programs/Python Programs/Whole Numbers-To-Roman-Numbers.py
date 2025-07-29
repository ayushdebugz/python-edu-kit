"""
Created on Fri Oct 12 20:34:41 2018

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""

# Program To Convert Whole Number [0-n] To Roman Values

class py_solution:
    def int_to_Roman(self, x):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        x=int(input("Enter Any Number[1-9999]:"))
        while  x > 0:
            for _ in range(x // val[i]):
                roman_num += syb[i]
                x -= val[i]
            i += 1
        return roman_num
print("CovertED 2 RomanIC:\n",py_solution().int_to_Roman(0))
print("ConverteD 2 Romanic:\n",py_solution().int_to_Roman(0))
print("Program Executed Successfully!\n")

  
    
    
