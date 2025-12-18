import random
import math

def tirage_exponentiel(lmbda):
    return -math.log(random.random()) / lmbda

def simulate_system(machines, T_TOTAL):
    t = 0
    downtime = 0

    while t < T_TOTAL:
        times_to_failure = {
            m: tirage_exponentiel(data["lambda"])
            for m, data in machines.items()
        }

        next_machine = min(times_to_failure, key=times_to_failure.get)
        ttf = times_to_failure[next_machine]

        if t + ttf > T_TOTAL:
            break

        t += ttf
        repair_time = tirage_exponentiel(1 / machines[next_machine]["mttr"])
        downtime += repair_time
        t += repair_time

    availability = 1 - downtime / T_TOTAL
    return availability

