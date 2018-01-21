#Return Roman numeral from a given integer
#Input: A number as an integer.
#Output: The Roman numeral as a string.

def checkio(number):
    ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))
    result=""
    for pair in ROMANS:
        while number >= pair[1]:
            number = number - pair[1]
            result = result+pair[0]
    return result
