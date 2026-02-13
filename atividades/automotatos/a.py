import numpy as np
import matplotlib.pyplot as plt

# Definir os parâmetros
lambda_charge = 1  # Densidade linear de carga (arbitrária)
epsilon_0 = 8.85e-12  # Permissividade do vácuo (em C^2/(N·m^2))
d = 1  # Distância do ponto P ao fio (em metros, arbitrária)

# Função para calcular o campo elétrico diferencial
def dE(x, d, lambda_charge, epsilon_0):
    r = np.sqrt(x**2 + d**2)
    return (lambda_charge / (4 * np.pi * epsilon_0)) * (d / r**3)

# Definir os valores de x para a integração
x_values = np.linspace(-10, 10, 400)

# Calcular dE para cada valor de x
dE_values = dE(x_values, d, lambda_charge, epsilon_0)

# Calcular o campo elétrico total (integrando)
E_total = np.trapz(dE_values, x_values)

# Plotar o gráfico de dE vs x
plt.figure(figsize=(10, 6))
plt.plot(x_values, dE_values, label=r"$dE_x = \frac{d \cdot dx}{(x^2 + d^2)^{3/2}}$")
plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')
plt.xlabel("x (posição ao longo do fio)")
plt.ylabel(r"$dE_x$ (componente do campo elétrico)")
plt.title("Componente do Campo Elétrico dE_x vs. Posição ao Longo do Fio")
plt.legend()
plt.grid(True)
plt.show()

E_total
