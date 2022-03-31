# bring in matplotlib
import matplotlib.pyplot as plt

# x-axis vals
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# y-axis vals
y = [10, 40, 32, 86, 61, 90, 77]

# plotting the points
plt.plot(x, y)

# name x-axis
plt.xlabel('Day Purchased')

# name y-axis
plt.ylabel('Cupcakes Purchased')

plt.title('Cupcake Sales')

plt.show()


