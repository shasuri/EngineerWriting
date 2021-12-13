import matplotlib.pyplot as plt
import numpy as np

X = np.array([1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
Y = np.array([6.2, 6.8, 9.2, 9.6, 7.6, 5.9, -5.5, 11.5, 9.1, 4.9, 7.7, 3.1, 5.2, 4.3, 5.3, 5.8, 3.0, 0.8, 6.8, 3.7, 2.4, 3.2, 3.2, 2.8, 2.9, 3.2, 2.7, 2.0])

threshold = 0

# Add below threshold markers
below_threshold = Y >= threshold
plt.scatter(X[below_threshold], Y[below_threshold], color='green') 

# Add above threshold markers
above_threshold = np.logical_not(below_threshold)
plt.scatter(X[above_threshold], Y[above_threshold], color='red') 
plt.show()