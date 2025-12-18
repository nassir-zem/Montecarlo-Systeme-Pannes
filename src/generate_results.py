import matplotlib.pyplot as plt
from simulation import simulate_once

N = 5000  # nombre de simulations Monte-Carlo

results = [simulate_once() for _ in range(N)]

# Histogramme
plt.hist(results, bins=30)
plt.xlabel("Disponibilité du système")
plt.ylabel("Fréquence")
plt.title("Histogramme de la disponibilité (Monte-Carlo)")

plt.savefig("results/figures/histogramme_disponibilite.png")
plt.close()

print("Figure générée avec succès")
