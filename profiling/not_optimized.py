#! /usr/bin/env python
import sys
import os


def fib_help():
    """
    Simple helper to explain how to use the script.
    """
    print('{}'.format('*' * 62))
    print('* Provide an integer index to get the nth Fibonacci number.{}*'.format(' ' * 2))
    print('* Example: python not_optimized.py 8{}*'.format(' ' * 25))
    print('* Yields: 21{}*'.format(' ' * 49))
    print('{}'.format('*' * 62))
    sys.exit()


def fib_generator(fib_index):
    a, b = 0, 1
    count = 0
    while count < fib_index:
        a, b = b, a + b
        count += 1
        yield a


def fib(fib_index):
    fib_values = [fib_num for fib_num in fib_generator(fib_index)]
    print(fib_values[-1])



if __name__ == '__main__':
    # Clear the console to make the results more readable.
    os.system(['clear', 'cls'][os.name == 'nt'])

    # Simple approach to ensure the correct parameters are passed.
    if len(sys.argv) != 2:
        fib_help()

    # If an integer parameter is passed use the algorithms to find the Fibonacci number.
    try:
        index = int(sys.argv[1])

        # Let's do some profiling
        # Warning - do not use too large of a number when profiling!
        # Shoot for between 3-5 seconds of "calculating" to get a solid case.
        import cProfile
        cProfile.run('fib(index)')

    # If a non-integer parameter is passed we'll help the user out.
    except ValueError:
        fib_help()
