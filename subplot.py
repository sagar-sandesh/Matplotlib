import matplotlib.pyplot as plt
import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 1)
# plt.plot(x,y)
#
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 2)
# plt.plot(x,y)
#
# # plot 3:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 3)
# plt.plot(x,y)
#
# # plot 4:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 4)
# plt.plot(x,y)
#
# # plot 5:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 5)
# plt.plot(x,y)
#
# # plot 6:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 6)
# plt.plot(x,y)

#plot 1:

x = np.array([ 1720, 1820, 1537, 1640, 1950, 1680, 1730, 1580, 1390,1250, 1630, 1480])
y = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.scatter(x,y)
plt.title("Income", color='Green')

#plot 2:
x = np.array([ 1250, 1120, 1280, 1150, 1220, 1180, 1230, 1100, 1270,1250, 1190, 1260])
y = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.scatter(x,y)
plt.title("Expenses", color="Green")

plt.suptitle("My monthly expenses", color='red')

plt.show()