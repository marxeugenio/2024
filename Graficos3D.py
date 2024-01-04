from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# geração de dados

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)

# Scatter plot 3D

ax.scatter(x, y, z)

plt.show()

# Customizações 3D adicionais
# (ex: superficies, wireframes, etc.)
