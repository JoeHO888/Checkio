
# Return repeated integers
#Input:A list of integers.
# Output: The list of integers.
def checkio(data):
    result=[]
    for e in data:
        if data.count(e)>1:
            result.append(e)
    return result
