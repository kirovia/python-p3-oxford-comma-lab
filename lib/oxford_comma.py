def oxford_comma(items):
    if len(items) == 0:
        return 'Please input a valid list'
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        return ', '.join(items[0:-1]) + f', and {items[-1]}'
