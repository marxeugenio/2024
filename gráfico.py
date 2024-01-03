import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure
ax = fig.add_subplot(111, projection="3D")

# Dados para o grafico de barras

x = [1,2,3,4,5]
y = [2,3,4,5,6]
z = np.zeros(5) # Coordenada z inicial para a base das barras

dx = dy = [1,1,1,1,1]
dz = [1,2,3,4,5] # Altura das barras

# Criação do grafico de dispersão

x_scatter = np.random.rand(10)
y_scatter = np.random.rand(10)
z_scatter = np.random.rand(10)

# Criação do grafico de dispersão

ax.scatter(x_scatter, y_scatter, z_scatter, color = "red")

# Rotulos dos eixos

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

plt.show()