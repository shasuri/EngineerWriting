import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

import matplotlib.pyplot as plot
plot.figure(figsize=(8,5)) # 인치

Weight = [ (1, 67.3),  (2,67.1),  (4,66.4),  (8,65.7), (10, 64.9),
           (11, 65.3), (13,63.9), (14,64.1), (18,64.7), (20, 64.1),
           (25, 64.5), (26,63.4), (27,63.6), (31,62.7), (32, 62.5)
         ]

for w in Weight :
    day = w[0]
    weight= w[1]
    print(f'day= {day:2}  W={weight:5}')

days = [d[0] for d in Weight]
weights = [w[1] for w in Weight]

plot.title("Problem 07, Weight Regression:")
def func(x, a, b, c, d):
  return a * (x ** 3) + b * (x ** 2)  + c * x + d

optimizedParameters, pcov = opt.curve_fit(func, days, weights)

funcX = np.linspace(max(days), min(days), 1000)
funcY = func(np.array(funcX), optimizedParameters[0],
                              optimizedParameters[1],
                              optimizedParameters[2],
                              optimizedParameters[3])

plt.plot(days, weights, 'bo', funcX, funcY, 'r--')
plt.show()