def value(colors):
    return int(''.join(str(_color_code(color)) for color in colors))


# Re-use code from previous exercise
def _color_code(color):
    return _colors().index(color)


# Re-use code from previous exercise
def _colors():
    return [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
