import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,11,1)
y=(x**2+(-3)*x+1)
plt.plot(x,y)
plt.grid(True)
plt.show()
