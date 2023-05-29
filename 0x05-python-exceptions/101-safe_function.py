#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        outcome = fct(*args)
    except Exception as info:
        sys.stderr.write("Exception: {}\n".format(info))
        outcome = None

    return (outcome)
