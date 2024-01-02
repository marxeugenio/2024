import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Dados

x = np.random.normal(size=500)
y = np.random.normal(size=500)
z = np.random.normal(size=500)

# Gráfico de dispersão 3 D
ax.scatter(x, y, z)

# Difinição dos rótulos dos eixos
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")

plt.show()
