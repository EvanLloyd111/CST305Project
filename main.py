#import the required libaries
import math

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ya(y,x):
    yaa = (pow(x,2)/2) -((3 * x)/2) + (3/4) - ((3 * pow(math.e, -2 * x))/4)
    return yaa

y0 = 0
x = np.linspace(0, 10, 100)
y = odeint(ya, y0, x)
plt.plot(x, y, 'g+', linewidth=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph using Odeint")
plt.show()
