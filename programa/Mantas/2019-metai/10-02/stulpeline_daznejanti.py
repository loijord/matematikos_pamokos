import numpy as np
import matplotlib.pyplot as plt

def generate_data(m):
    objects = [str(i) for i in range(m)]
    performance = np.random.normal(0, 3, m)
    for n in range(1,m+1):
        yield objects[:n], np.linspace(0,20,n), performance[:n]

m=50
fig = plt.figure()
for n in generate_data(500):
    fig.clear()
    plt.ylim([-7, 7])
    objects, y_pos, performance = n
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Value, C')
    plt.title('Temperature forecast')
    plt.pause(0.2)
    plt.draw()
    #plt.show()