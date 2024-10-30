
QUOTES = ['"', "'"]
WHITESPACES = [' ', '\t']



def parse(tokens) -> dict:
    tree = {
        "type": "main",
        "content": []
    }
    id = 0
    while id < len(tokens):
        if tokens[id] == 'set':
            output = {
                'type': 'assignment',
                'identifier': tokens[id+1],
                'value': {}
            }

            id += 2

            if tokens[id] != 'to':
                raise SyntaxError(f"Identifier {tokens[id-1]} must be followed with keyword 'to' ")
            

            id += 1
            branches = []
            try:
                while id < len(tokens) and tokens[id] != '\n':
                    branches.append(tokens[id])
                    id += 1
            except IndexError:
                raise SyntaxError("A variable needs a to be set to a valid value")    
            output['value'] = expression_tree(branches)
            id += 1

            tree['content'].append(output)
            continue

        elif tokens[id] == 'out':
            output = {
                'type': 'output',
                'value': {}
            }

            id += 1

            branches = []

            while id < len(tokens) and tokens[id] != '\n':
                branches.append(tokens[id])
                id += 1

            output['value'] = expression_tree(branches)
            id += 1

            tree['content'].append(output)
            continue
        else:
            raise SyntaxError(f"Unidentified token {tokens[id]}")
    return tree


def expression_tree(tokens):
    operation_types = {'+': 'addition', '-': 'subtraction', '/': 'division', '^': 'exponentiation', '*': 'multiplication'}
    
    # Base case: if there's only one token, it must be a single value (number or string)
    if len(tokens) == 1:
        token = tokens[0]
        if is_string(token):
            return {'type': 'string', 'value': token[1: -1]}  # Remove quotes
        elif is_number(token):
            return {'type': 'number', 'value': token}
        else:
            return {'type': 'identifier', 'name': token}
    
    # Otherwise, parse operations
    for id, token in enumerate(tokens):
        if is_operation(token):
            return {
                'type': operation_types[token],
                'val1': expression_tree(tokens[:id]),  # Left side
                'val2': expression_tree(tokens[id + 1:])  # Right side
            }
    
    # Fallback in case of parsing issues
    return {'type': 'unknown', 'value': tokens}

def is_string(token):
    return (token[0] == token[-1] and token[0] in QUOTES)


def is_number(token):
    try:
        float(token)
    except ValueError:
        return False

    return True

def is_operation(token):
    return token in ['+', '-', '/', '^', '*']
