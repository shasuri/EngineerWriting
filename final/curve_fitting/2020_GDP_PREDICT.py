import matplotlib.pyplot as plot
import numpy as np
from sklearn.ensemble import RandomForestRegressor

X = np.array([1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
Y = np.array([6.2, 6.8, 9.2, 9.6, 7.6, 5.9, -5.5, 11.5, 9.1, 4.9, 7.7, 3.1, 5.2, 4.3, 5.3, 5.8, 3.0, 0.8, 6.8, 3.7, 2.4, 3.2, 3.2, 2.8, 2.9, 3.2, 2.7, 2.0])
pred_X = np.array([2020, 2021, 2022, 2023, 2024, 2025])


regr = RandomForestRegressor()
regr.fit(X.reshape(-1, 1), Y)

pred_Y = regr.predict(pred_X.reshape(-1, 1))

print(len(X), len(Y))
print(X.shape, Y.shape)
print(len(pred_X), len(pred_Y))
plot.scatter(X, Y)
plot.scatter(pred_X, pred_Y)
# plot.plot(X, Y)
plot.show()