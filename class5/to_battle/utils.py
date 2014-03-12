

def pretty_print(obj, indents=0):
    if isinstance(obj, (list, tuple)):
        opening = '{}['
        closing = '{}]'
        if isinstance(obj, tuple):
            opening = '{}('
            closing = '{})'
        print(opening.format(' ' * 4 * indents))

        for item in obj:
            pretty_print(item, 1)

        print(closing.format(' ' * 4 * indents))

    elif isinstance(obj, dict):
        print('{}{{'.format(' ' * 4 * indents))
        for key, val in obj.items():
            if isinstance(val, dict):
                print('{}{}: {'.format(' ' * 4 * (indents + 1), key))
                pretty_print(val, indents + 1)
            else:
                print('{}{}: {}'.format(' ' * 4 * (indents + 1), key, val))
        closing = '{}}},'
        if indents == 0:
            closing = '{}}}'
        print(closing.format(' ' * 4 * indents))
