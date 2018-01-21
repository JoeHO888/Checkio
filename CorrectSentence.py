#Change the first letter to capital if necessary 
#Input: A string
#Output: A string

def correct_sentence(string):
    if string[len(string)-1] != ".":
        string=string+"."
    
    return string[0].upper()+string[1:]
