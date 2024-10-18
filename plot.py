import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo de valores para x e y
x = np.linspace(-2, 2, 200)
y = np.linspace(-3, 3, 200)

# Criar uma grade de coordenadas
X, Y = np.meshgrid(x, y)

# Calcular os valores de Z para cada ponto (X, Y)
Z = X * Y**3 + 9 * X**2 - 3 * Y**2 + 8

# Criar a figura e o eixo 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotar a superfície
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Adicionar uma barra de cores para a legenda
fig.colorbar(surf, shrink=0.5, aspect=5)

# Adicionar rótulos aos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')

# Definir o título do gráfico
ax.set_title('Gráfico da função f(x, y) = x*y^3 + 9x^2 - 3y^2 + 8')

# Ajustar o ângulo de visualização (opcional)
ax.view_init(elev=30, azim=60)

# Mostrar o gráfico
plt.show()
