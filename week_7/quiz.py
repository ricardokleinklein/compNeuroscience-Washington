import os
import numpy as np

# Ejercicio 1

Q = [[0.15, 0.1], [0.1, 0.12]]
eigenvalues, eigenvectors = np.linalg.eig(Q)
stable = eigenvalues[0] * eigenvectors[:, 0]
# print(stable)

print(stable[0] / stable[1])
print(-1.5764 / -1.2308)
print(-1.5155 / -1.3051)
# exit()
import pickle
import matplotlib.pyplot as plt

with open('data.pickle', 'rb') as f:
	data = np.array(pickle.load(f)['c10p1'])

plt.subplot(2,1,1)
plt.scatter(data[:,0], data[:, 1])
# normalization
mu = np.mean(data, axis=0)
# data = data - mu
plt.subplot(2,1,2)
plt.scatter(mu[0], mu[1], color='r')
plt.scatter(data[:,0], data[:, 1])
plt.show()

# Implement learning rules
lr = 1
alpha = 1
dt = 0.01
w = np.random.rand(2)
idx = 0
Q = np.dot(data.transpose(), data) / len(data)
eigval, eigvec = np.linalg.eig(Q)
print(sorted(eigval))
print(eigvec)
history = [w]

for it in range(10000):
	u = data[idx, :]
	v = np.dot(w, u)
	w = w + dt * lr * (v * u - alpha * v * v * w)
	# w = w + dt * lr * (v * u)
	history.append(w)
	idx += 1
	if idx == data.shape[0]:
		idx = 0
history = np.array(history)
plt.scatter(history[0,0], history[0, 1], color='r')
plt.plot(history[:,0], history[:,1])
plt.scatter(history[-1,0], history[-1, 1], color='g')
plt.show()