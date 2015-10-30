#! /usr/bin/env python
import sys


import os
# Simple helper to explain how to use the script.
def fib_help():
    print('{}'.format('*' * 62))
    print('* Provide an integer index for the nth Fibonacci number.%s*' % (' ' * 5))
    print('* Example: python bad_fibonacci.py 8%s*' % (' ' * 29))
    print('* Yields: 21%s*' % (' ' * 49))
    print('{}'.format('*' * 62))
    sys.exit()

def powLF(fib_index):
    """
    Using the matrix approach to find the Lucas numbers
    :param fib_index: Integer index
    :return: Lucas Numbers for calculating Fibonacci number
    """
    if fib_index == 1: return 1, 1
    L, f = powLF(fib_index // 2)
    L, f = (L**2 +5 * f ** 2) >> 1, L*f
    if fib_index & 1: return (L+5*f) >> 1, (L+ f) >> 1
    return L, f




# Using the Lucas numbers to calculate the nth Fibonacci number.
def Fib(FibIndex):
    if FibIndex & 1:
        print(powLF(FibIndex)[1])
        return

    l, f = powLF(FibIndex // 2)
    print(l * f)


if __name__ == '__main__':
    os.system(['clear', 'cls'][os.name == 'nt'])
    if len(sys.argv) != 2: fib_help()



    try:
        index = int( sys.argv[1])
        Fib(index)
    except ValueError:
        fib_help()
