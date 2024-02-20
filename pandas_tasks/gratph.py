import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, 'b-', label='sin(x)')
plt.plot(x, y_cos, 'r+', label='cos(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций sin(x) и cos(x)')
plt.legend()
plt.grid(True)
plt.axis((0, 2 * np.pi, -1, 1))

plt.xticks(np.arange(0, 2 * np.pi + np.pi / 2, np.pi / 2), ['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
plt.savefig('result.png')
plt.show()
