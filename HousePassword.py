#Return Boolean value for a given password string
#Input: A string
#Output: Boolean value

def checkio(data):
    list_of_integer=[0,1,2,3,4,5,6,7,8,9]
    string_of_lower_case='abcdefghijklmnopqrstuvwxyz'
    if len(data) >= 10:
        for e in string_of_lower_case:
            if e in data:
                for i in string_of_lower_case.upper():
                    if i in data:
                        for j in list_of_integer:
                            if str(j) in data:
                                return True
    return False
