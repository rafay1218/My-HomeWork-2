import numpy as np

print(np.exp(0), np.cos(np.pi))

def F(x, y):
  return np.exp(np.array(y*1j))+2*np.exp(np.array(y*(-1j)/2))*np.cos((np.sqrt(3)/2)*x)

def matrix(f):
  return np.array([[0, f], [np.conjugate(f), 0]])

Diagonalize = np.linalg.eig(matrix(F(1,2)))
print(Diagonalize)
Diag2 = np.linalg.eigh(matrix(F(1,2)))
print(Diag2)
# Differences?

x = np.linspace(-np.pi, np.pi, 3)
y = np.linspace(-np.pi, np.pi, 3)
xv, yv = np.meshgrid(x, y)

print(xv)
print(yv)

for i in range(3):
  for j in range(3):
    print('\n---------------')
    Diag = np.linalg.eig(matrix(F(xv[i,j],yv[i,j])))
    print(xv[i,j], yv[i,j])
    print(Diag)

