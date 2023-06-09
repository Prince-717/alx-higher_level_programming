#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    len_args = len(sys.argv)
    
    if len_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '/' and sys.argv[2] != '*':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], calc.add(int(sys.argv[1]), int(sys.argv[3]))))

    if sys.argv[2] == '-':
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], calc.sub(int(sys.argv[1]), int(sys.argv[3]))))

    if sys.argv[2] == '*':
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], calc.mul(int(sys.argv[1]), int(sys.argv[3]))))

    if sys.argv[2] == '/':
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], calc.add(int(sys.argv[1]), int(sys.argv[3]))))

    
    
