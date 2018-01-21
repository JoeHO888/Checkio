#Return length of the longest substring having the same character
#Input: String
#Output: Int

def long_repeat(line):
    i=0
    max = 0
    while i < len(line):
        character = line[i]
        counter = 1
        print (character)
        while  i<len(line)-1 and line[i+1] == character:
            counter = counter + 1
            i=i+1
        if counter >=max:
            max = counter
        i=i+1  
    return max
