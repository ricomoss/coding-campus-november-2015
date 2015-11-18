#! /usr/bin/env python
import sys
import os


def fib_help():
    """
    Simple helper to explain how to use the script.
    """
    print('{}'.format('*' * 62))
    print('* Provide an integer index to get the nth Fibonacci number.{}*'.format(' ' * 2))
    print('* Example: python fibonacci.py 8{}*'.format(' ' * 29))
    print('* Yields: 21{}*'.format(' ' * 49))
    print('{}'.format('*' * 62))
    sys.exit()


def pow_lf(fib_index):
    """
    Using the matrix approach to find the Lucas numbers
    :param fib_index: Integer index
    :return: Lucas Numbers for calculating Fibonacci number
    """
    if fib_index == 1:
        return 1, 1

    l, f = pow_lf(fib_index // 2)
    l, f = (l ** 2 + 5 * f ** 2) >> 1, l * f

    if fib_index & 1:
        return (l + 5 * f) >> 1, (l + f) >> 1
    return l, f


def fib(fib_index):
    """
    Using the Lucas numbers to calculate the nth Fibonacci number.
    :param fib_index: Integer index
    :return: Fibonacci number
    """
    if fib_index & 1:
        print(pow_lf(fib_index)[1])
        return

    l, f = pow_lf(fib_index // 2)
    print(l * f)


if __name__ == '__main__':
    # Clear the console to make the results more readable.
    os.system(['clear', 'cls'][os.name == 'nt'])

    # Simple approach to ensure the correct parameters are passed.
    if len(sys.argv) != 2:
        fib_help()

    # If an integer parameter is passed use the algorithms to find the Fibonacci number.
    try:
        index = int(sys.argv[1])
        fib(index)

    # If a non-integer parameter is passed we'll help the user out.
    except ValueError:
        fib_help()
