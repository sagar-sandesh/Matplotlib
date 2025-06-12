import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,10])
ypoints = np.array([0,250])
zpoints = np.array([0,220])

plt.plot(xpoints, ypoints, zpoints)
plt.show()

# Plotting without the lines
# xpoints = np.array([0,10])
# ypoints = np.array([0,20])
#
# plt.plot(xpoints, ypoints, 'o')
# plt.show()