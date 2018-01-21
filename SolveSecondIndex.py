#Return the index of the second occurrence of a character
#Input: Two strings.
#Output: Int or None

def second_index(text: str, symbol: str):

    if symbol not in text:
        return None
    else:
        if symbol not in text[text.find(symbol)+1:]:
            return None
        else:
            return ((text[text.find(symbol)+len(symbol):].find(symbol)+text.find(symbol)+len(symbol)))
