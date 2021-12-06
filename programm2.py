import math
import random
import matplotlib.pyplot as plt


random.seed(42)
num_events = 100
num_inside = 0
data_x = []  # x coordinates
data_y = []  # y coordinates
data_c = []  # colors

for i in range(num_events):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    data_x.append(x)
    data_y.append(y)
    if 1 >= math.sqrt(x ** 2 + y ** 2):
        num_inside += 1
        data_c.append('red')
    else:
        data_c.append('blue')
number = 4 * num_inside / num_events

print('Events: {: >9d}, Result: {:.5f}'.format(num_events, number))

plt.figure(figsize=(5.0, 5.0))
plt.scatter(data_x, data_y, s=2, c=data_c, alpha=0.5)
plt.show()

