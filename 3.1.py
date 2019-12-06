import numpy as np
def f(x):
    return x**2
print(f(2))
def even(x):
    return x%2==0
print(even(3))
print(map(even,np.arange(10)))
print(map(lambda x:x**2,np.arange(10)))