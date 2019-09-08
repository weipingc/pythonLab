import numpy as np

class Application():
    def __init__(self):
        print("[Application.__init__]")

    def run(self):
        print("[Application.run] Hi App by Poetry!")
        fiveZeros = np.zeros(5)
        print("fiveZeros=", fiveZeros)

