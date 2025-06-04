import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load observation vector y from Excel
y = pd.read_excel('y.xlsx', header=None).values.flatten()

# Load design matrix X from Excel
X = pd.read_excel('X.xlsx', header=None).values

# Load end indices of observations
Eind = pd.read_excel('Eind.xlsx', header=None).values.flatten()

# Load start indices of observations
Sind = pd.read_excel('Sind.xlsx', header=None).values.flatten()

# Standard deviation of observations
sigma_moshahedat = 0.1

# Known control point information
known_points_num = 1
known_points_index = 1
height_of_known_point = 100

# Number of observations
n = y.shape[0]

# Number of unknowns
u = X.shape[0] - known_points_num

# Observation vector LO
LO = y.copy()

# Adjust observation vector based on known point
for i in range(n):
    if Sind[i] == known_points_index:  
        LO[i] = LO[i] + height_of_known_point
    elif Eind[i] == known_points_index:
        LO[i] = height_of_known_point - LO[i]

# Weight matrix (diagonal)
W = np.eye(n) * (1 / sigma_moshahedat**2)

# Design matrix A
A = np.zeros((n, u))

for i in range(n):
    j = Eind[i] - 1  # convert to 0-based indexing
    if j >= 1:
        A[i, j - 1] = 1  # shift due to known point excluded
    k = Sind[i] - 1
    if k >= 1:
        A[i, k - 1] = -1  # shift due to known point excluded

# Compute the estimated unknown heights (X̂) using least squares adjustment
At_W = A.T @ W
N = At_W @ A           # Normal matrix
U = At_W @ LO      

Xcap = np.linalg.inv(A.T @ W @ A) @ (A.T @ W @ LO)

# Compute estimated observation vector (LÔ = A * X̂)
LOcap = A @ Xcap

# Compute the residual vector: V = A * X̂ - L
V = A @ Xcap - LO

# Plot residual vector as an image
plt.figure(figsize=(6, 3))
plt.imshow(V.reshape(-1, 1), aspect='auto', cmap='viridis')  # reshape for 2D display
plt.colorbar(label='Residual value')
plt.title('Residual Vector Chart')
plt.xlabel('Residual')
plt.ylabel('Observation Index')
plt.tight_layout()
plt.show()

# Compute variance-covariance matrix of the estimated unknowns
Q = np.linalg.inv(A.T @ W @ A)

# Plot variance-covariance matrix
plt.figure(figsize=(6, 5))
plt.imshow(Q, cmap='viridis')
plt.colorbar(label='Variance / Covariance')
plt.title('Variance-Covariance Matrix')
plt.xlabel('Unknown Index')
plt.ylabel('Unknown Index')
plt.tight_layout()
plt.show()
