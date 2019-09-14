import imp
import sys
import numpy as np

class Application():
    def __init__(self):
        print("[Application.__init__]")

    def run(self):
        print("[Application.run] Hi App by Poetry!")
        print("sys.path=", sys.path)
        print()
        print("numpy module file=", imp.find_module("numpy"))
        fiveZeros = np.zeros(5)
        print("fiveZeros=", fiveZeros)

