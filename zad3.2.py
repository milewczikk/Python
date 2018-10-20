import numpy as np
import matplotlib.pyplot as plt
a=int(input("podaj a: "))
x1=np.arange(-10,0.5,1)
x2=np.arange(0,11,1)
y1=(x1/(-3)+a)
y2=(x2*x2/3)
plt.plot(x1,y1,'r',x2,y2,'g')
plt.grid(True)
plt.show()
