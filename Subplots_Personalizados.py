import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Cria uma grade de subplots personalizada

fig = plt.figure()

# Define a grade com diferentes tamanhos de celulas

gs = GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])

plt.show()

# Personaliza cada subplot
# (Por exemplo, plotagem de dados em cada um deles)
