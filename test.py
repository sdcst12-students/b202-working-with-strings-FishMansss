
def replaceDog(input):
    '''
    parameters:
    str input - string to search and replace occurrences of dog with kitty

    return
    str - the modified string
    '''
    
    modifiedString = input
    #x = modifiedString.index("dog")
    modifiedString.replace('cat','dog')
    print(modifiedString)
    return modifiedString


replaceDog("my dog has fleas")