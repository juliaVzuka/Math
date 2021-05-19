%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 12, 200)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(5*x))
