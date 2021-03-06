# Return a character with highest occurrence in a string
#Input: A text for analysis as a string.
#Output: The most frequent letter in lower case as a string.
from collections import Counter

def checkio(text):
    text=text.lower()
    for e in text:
        if e not in "abcdefghijklmnopqrstuvwxyz":
            text=text.replace(e,"")
    text_list=[e for e in text]
    max_occurence=Counter(text_list).most_common(1)[0][1]
    final_list = sorted([e for e in Counter(text_list) if Counter(text_list)[e] == max_occurence])
    return ( final_list[0])

#print(checkio("Hello World!")) == "l"
