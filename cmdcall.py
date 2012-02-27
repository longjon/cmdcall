# cmdcall.py: a simple way to call Python functions from the command line,
#  without argparse or the like

import sys

# a map from function name to function and argument processors
_register = {}

def command(*fargs):
    """A decorator indicating that a function can be called
       from the command line. Each argument is first passed through
       the corresponding function in fargs."""

    def registerer(f):
        _register[f.__name__] = (f, fargs)
        return f

    return registerer

def call_from_args(name, args):
    """Call the named function, converting the provided string arguments
       as specified in the register."""

    if name not in _register:
        print 'Unknown function', name
        return

    f, fargs = _register[name]

    if f.func_defaults is not None:
        if len(args) < len(fargs) - len(f.func_defaults):
            print 'Expected at least', len(fargs) - len(f.func_defaults), 'arguments'
            return
        if len(args) > len(fargs):
            print 'Expected at most', len(fargs), 'arguments'
            return
    elif len(args) != len(fargs):
        print 'Expected', len(fargs), 'arguments'
        return

    return f(*[a(b) for a, b in zip(fargs, args)])

def main():
    """Call a function based on command line arguments"""

    call_from_args(sys.argv[1], sys.argv[2:])
