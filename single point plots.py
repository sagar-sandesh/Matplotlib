import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints, marker='o')
# plt.plot(ypoints, marker='x')

# plt.plot(ypoints, 'o:r')

plt.plot(ypoints, marker ='o', ms = 20)

# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')

plt.show()