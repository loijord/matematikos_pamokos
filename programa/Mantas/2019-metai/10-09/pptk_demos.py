import pptk
import numpy as np

helix1 = [(10*np.sin(t), 10*np.cos(t), 3*t) for t in np.linspace(0, 100, 50)]
helix2 = [(10*np.sin(t), 10*np.cos(t), 3*t) for t in np.linspace(0, 100, 200)]
helix3 = [(10*np.sin(t), 10*np.cos(t), 3*t) for t in np.linspace(0, 100, 1000)]

parabola1 = [(t, t**2, 0) for t in np.linspace(-5, 5, 10)]
parabola2 = [(t, t**2, 0) for t in np.linspace(-5, 5, 1000)]



h1 = pptk.viewer(helix1)
h1.set(point_size=0.3)

h2 = pptk.viewer(helix2)
h2.set(point_size=0.3)

h3 = pptk.viewer(helix3)
h3.set(point_size=0.3)

p1 = pptk.viewer(parabola1)
p1.set(point_size=0.3)

p2 = pptk.viewer(parabola2)
p2.set(point_size=0.3)
