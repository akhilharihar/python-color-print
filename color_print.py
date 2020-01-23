def cprint(*objects, **kwargs):
    """Apply Color formatting to output in terminal.
    Same as builtin print function with added 'color' keyword argument.
    eg: cprint("data to print", color="red", sep="|")
    available colors:
    black
    red
    green
    yellow
    blue
    pink
    cyan
    white
    no-color
    """
    
    colors = {
        "black": "\033[0;30m",
        "red": "\033[0;31m",
        "green": "\033[0;92m",
        "yellow": "\033[0;93m",
        "blue": "\033[0;34m",
        "pink": "\033[0;95m",
        "cyan": "\033[0;36m",
        "white": "\033[0;37m",
        "no-color": "\033[0m"
    }

    color = kwargs.pop('color', 'no-color')

    return print(colors[color], *objects, colors['no-color'], **kwargs)