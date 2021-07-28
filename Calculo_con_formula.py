import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return 2*x**7 - x**4 + 3*x**2 + 4

x = np.linspace(-100.0, 100.0)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')