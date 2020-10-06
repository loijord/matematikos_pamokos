#Si programa bandys imituoti artimiausiu 20 dienu orus (kiekvienasyk vis kitokius)
import numpy as np
random_generator = np.random.normal(0, 3, 20)
decreasing_temps = np.arange(8, 5,-0.15)
results = random_generator + decreasing_temps
print(results.astype(int))