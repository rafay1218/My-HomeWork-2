from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
fig = plt.figure()

num = 21

x = np.linspace(-np.pi, np.pi, num)
y = np.linspace(-np.pi, np.pi, num)
xv, yv = np.meshgrid(x, y)
base_matrix_eigen1 = np.zeros([num,num])
base_matrix_eigen2 = np.zeros([num,num])

for i in range(num):
  for j in range(num):
    Diag = np.linalg.eig(matrix(F(xv[i,j],yv[i,j])))
    base_matrix_eigen1[i][j]=Diag[0][0]
    base_matrix_eigen2[i][j]=Diag[0][1]

plt.rcParams["figure.figsize"] = [16, 7]

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(xv, yv, base_matrix_eigen1, cmap='Greens')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(xv, yv, base_matrix_eigen2, cmap='Oranges', )

plt.show()