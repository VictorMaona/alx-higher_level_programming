#!/usr/bin/python3

if __name__ == "__main__":
    """Print every name listed in hidden 4 module"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
