"""
Created on Friday Feb 22 10:27:18 2019

@author: AyusH Jha
Github: https://github.com/ayushdebugz
"""
# Program "Generating Alpha-Numeric Strings Based On User Entered Data"

class py_solution:
    def alphanumeric(self, x):
        val = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        syb = ["4", "8", "C", "D", "ɛ", "F", "6", "H", "!", "7", "K", "1",
               "M", "N", "0", "P", "Q", "R", "5", "T", "µ", "V", "W", "X", "Y", "Z"]

        # Take input as a string from the user
        a = input("Enter The String: ").upper()

        result = ''
        for char in a:
            if char in val:
                index = val.index(char)
                result += syb[index]
            else:
                result += char  # leave as is if not in A-Z (like space or punctuation)

        return result


# Running the function
print("Converted to AlphaNumeric:\n", py_solution().alphanumeric(0))
