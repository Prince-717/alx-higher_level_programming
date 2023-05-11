#!/usr/bin/python3
"""My addition function

   Args:
        a: first integer
        b: second integer

   Returns:
        The return value. a + b
"""

if __name__ == "__main__":
    import add_0

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
