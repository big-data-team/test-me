import numpy as np
import pandas as pd

password=sys.environ["PASS"]

def main(name):
    print("hello,", name)
    for i in range(50):
        print(i)
    print("salut!")

if __name__ == "__main__":
    main("Evgeny")
    exit(0)
