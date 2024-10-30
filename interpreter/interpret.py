def interpret(node, environment={}):
    if node['type'] == 'main':
        for line in node['content']:
            interpret(line, environment)

    elif node["type"] == 'output':
        print(interpret(node['value'], environment))

    elif node['type'] == 'addition':
        if 'string' in [node['val1']['type'], node['val2']['type']]:
            return str(interpret(node['val1'], environment)) + str(interpret(node['val2'], environment))
        else:
            return float(interpret(node['val1'], environment)) + float(interpret(node['val2'], environment))

    elif node['type'] == 'subtraction':
        return float(interpret(node['val1'], environment)) - float(interpret(node['val2'], environment))
    
    elif node['type'] == 'multiplication':
        return float(interpret(node['val1'], environment)) * float(interpret(node['val2'], environment))
    
    elif node['type'] == 'exponentiation':
        return float(interpret(node['val1'], environment)) ** float(interpret(node['val2'], environment))
    
    elif node['type'] == 'division':
        return float(interpret(node['val1'], environment)) / float(interpret(node['val2'], environment))
    
    elif node['type'] == 'assignment':
        environment[node['identifier']] = interpret(node['value'], environment)

    elif node['type'] in ['number', 'string']:
        return node['value']

    elif node['type'] == 'identifier':
        get_variable = environment.get(node['name'], False)
        if not get_variable:
            raise ValueError(f"Variable {node['name']} is not defined")
        return get_variable





