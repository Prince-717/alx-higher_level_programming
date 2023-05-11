#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names_module = dir(hidden_4)
    for name in names_module:
        if name[:2] != "__":
            print(name)
