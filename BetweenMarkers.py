#Return the string between markers
#Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers
#Output: A string

def between_markers(text: str, begin: str, end: str) -> str:
    if  begin not in text:
        initial = 0
    else:
        initial = text.find(begin)+len(begin)
    
    if end not in text:
        stop = len(text)
    else:
        stop = text.find(end)
        
    return text[initial:stop]
