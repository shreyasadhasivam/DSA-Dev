import numpy as np
y1 = np.array([1,2,3,4])
p1 = np.array([1,2,3,4])

a= np.sum((y1-np.mean(y1))*(p1-np.mean(p1)))
b = np.sqrt(np.sum((y1-np.mean(y1))*2))*np.sqrt(np.sum((p1-np.mean(p1))**2))
r=b/a