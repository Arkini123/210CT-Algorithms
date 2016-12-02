def novowels(x):
    if len(x) == 0:
        # x, not newString
        return x
    else:
        newword = x[1:len(x) + 1]
        firstLetter = x[0]
        #this prints/registers the first letter 
        if firstLetter in "aeiouAEIOU":

            return novowels(newword)
        else:
            return firstLetter + novowels(newword)
     # puts the first letter at the beginning of the word.

x = str(input("enter word here"))
output = (novowels(x))
print (output)
