import math
import numpy as np
import timeit

setup = "import numpy as np"

testcode ='''
def test():
    x = np.arange(int(1e10))
    np.sqrt(x)
'''

t = timeit.repeat(setup = setup, stmt=testcode, number = 100, repeat = 1000)
print(np.min(t))
# timeit [math.sqrt(xx) for xx in x]
# print(timeit.timeit('output = 10*5'))