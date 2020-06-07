"""
	Steady state
"""

import numpy as np

W = 0.1 * np.ones((5, 5))
W += 0.6 * np.eye(5) - 0.1 * np.eye(5)

u = np.array([0.6, 0.5, 0.6, 0.2, 0.1])

M = np.array([[-0.125, 0, 0.125, 0.125, 0],
	[0, -0.125, 0, 0.125, 0.125],
	[0.125, 0, -0.125, 0, 0.125],
	[0.125, 0.125, 0, -0.125, 0],
	[0, 0.125, 0.125, 0, -0.125]])

h = np.dot(W, u)

eigenvalues, eigenvectors = np.linalg.eig(M)

v = np.zeros(u.shape)
for l in range(len(eigenvalues)):
	v += 1 / (1 - eigenvalues[l]) * np.dot(eigenvectors[:, l], h) * eigenvectors[:, l]
print(v)
