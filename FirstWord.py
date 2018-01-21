
#Return the first letter of a string
#Input: A string
#Output: A string

def first_word(text):
    for e in [",", "."]:
        text=text.replace(e," ")
    text=text.strip()
    if " " in text:
        num=text.find(" ")
    else:
        num=len(text)
    print(num)
    return text[:num]
