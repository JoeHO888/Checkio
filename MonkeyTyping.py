#Return an integer of target words' occurrence in a string
#Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
#Output: The number of words in the text as an integer.

def count_words(text, words):
    num = 0
    text=text.lower()
    for e in words:
        if e in text:
          num=num+1
    return num
