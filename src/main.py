from simulation import simulate_system
from parameters import machines, T_TOTAL

N = 10000
results = [simulate_system(machines, T_TOTAL) for _ in range(N)]

mean_availability = sum(results) / N
print("Disponibilité moyenne simulée :", mean_availability)
