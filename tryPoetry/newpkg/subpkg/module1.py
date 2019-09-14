import sys
import imp

def test():
    print("Hello new package")
    print("sys.path=", sys.path)
    print()
    print("numpy module file=", imp.find_module("numpy"))
