

def pretty_print(obj, indents=0):
    if isinstance(obj, (list, tuple)):
        for item in obj:
            return pretty_print(item)
    elif isinstance(obj, dict):
        if indents == 0:
            print('{')
        for key, val in obj.items():
            if isinstance(val, dict):
                print('{}{}: {{'.format(' ' * 4 * (indents + 1), key))
                pretty_print(val, indents + 1)
            else:
                print('{}{}: {}'.format(' ' * 4 * (indents + 1), key, val))
        print('{}}},'.format(' ' * 4 * indents))
