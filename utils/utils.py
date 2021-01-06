import sys


def parse(**kwargs):
    try:
        return [_arg for _arg in sys.argv if _arg.startswith(kwargs.get('arg'))][0].split('=')[1]
    except IndexError:
        if kwargs.get('default'):
            return kwargs.get('default')
        return False
