QUOTES = ['"', "'"]
WHITESPACES = [' ', '\t']
OPERATIONS = ['+', '-', '/', '*', '^']

def tokenize(input):

    characterised = []
    for char in input:
        characterised.append(char)

    tokens = []
    currentToken = ''
    string = False

    for index, character in enumerate(characterised):
    
        
        if character in WHITESPACES and not string:
        
            if currentToken != '':
                tokens.append(currentToken)
            currentToken = ''
            continue
        
        elif character == ';' or character == '\n':
            if currentToken != '':
                tokens.append(currentToken)
            tokens.append('\n')
            
            currentToken = ''
            continue
        
        elif character in QUOTES and string in [False, character]:
            
            if string == character:
                currentToken += character
                tokens.append(currentToken)
                string = False
                currentToken = ''
                continue
            else:
                string = character
                if currentToken != "":
                    tokens.append(currentToken)
                currentToken = character

        elif index == (len(characterised) - 1):
            currentToken += character
            tokens.append(currentToken)

        elif character in OPERATIONS:
            if currentToken != '':
                tokens.append(currentToken)
                currentToken = ''
            
            tokens.append(character)
            continue
            

        else:
            currentToken += character


    return tokens


if __name__ == "__main__":
    result = tokenize(input("> "))
    for item in result:
        print(item)
