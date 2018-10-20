import numpy as np
import matplotlib.pyplot as plt
a=int(input("podaj a: "))
b=int(input("podaj b: "))
x=np.arange(-10,11,1)
y=((a*x)+b)
plt.plot(x,y)
plt.grid(True)
plt.show()
