cmdcall.py: Call Python functions from the command line
-------------------------------------------------------

This is an easy way to be able to call multiple functions from the same Python
file from the command line. It does not require changes to those functions, or
the use of `argparse` or something similar.

Here is an example.

```python
import cmdcall

@cmdcall.command(float, float)
def add(a, b):
    print a + b

@cmdcall.command(int, int)
def multiply(a, b):
    print a*b

if __name__ == '__main__':
    cmdcall.main()
```

If this script were named `math.py`, you can now do `python math.py add 55.5 66.6`
or `python math.py multiply 7 -2`.

For general use, simply decorate functions with `@cmdcall.command(argument
types...)` and add a call to `cmdcall.main()` in your script.

---

The closest existing thing I could find was
[this code](http://code.activestate.com/recipes/528891-simple-calls-to-python-functions-from-command-line/),
but I think this is cleaner and doesn't require any change to code inside your
functions.
