"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mplayground` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``playground.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``playground.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys

from playground.subtwo.bar import Bar

from playground.greeter.greeter import Greeter
from playground import __version__


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    print(f"Demo {__version__}")
    print(argv)
    if (len(argv) > 1):
        print("{}".format(Greeter().greetings(argv[1])))
    else:
        print("{}".format(Greeter().greetings()))

    #print("{}".format(Bar().let_foo_do_something()))
    Bar().let_sample_do_something()
    print("DONE")
    return 0
