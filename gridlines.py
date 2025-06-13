import numpy as np
import matplotlib.pyplot as plt

x = np.array([20,21,22,23,24,25,26,27,28,29])
y = np.array([130,135,110,125,128,146,123,108,137,143])

plt.plot(x, y)

font1 = {'family':'serif','color':'blue','size':22}
font2 = {'family':'serif','color':'darkred','size':17}

plt.title("Employee statistics",fontdict = font1, loc = 'center')
plt.xlabel("Age of the employee",fontdict = font2, loc = 'center')
plt.ylabel("Number of employed person", fontdict = font2, loc = 'top')

plt.grid(color = 'green', linestyle = '-', linewidth = 0.5)

plt.show()