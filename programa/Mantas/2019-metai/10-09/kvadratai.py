import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.widgets import Slider  # import the Slider widget
import numpy as np

'''for a in np.arange(1,10,0.1):
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    ax = plt.gca()
    ax.add_patch(pch.Polygon([(0, 0), (0, a), (1/a, a), (1/a, 0)], closed=True, facecolor='blue', edgecolor = 'purple'))
    plt.pause(0.01)
    plt.draw()
    plt.cla()'''

a_min = 0.1    # the minimial value of the paramater a
a_max = 10   # the maximal value of the paramater a
a_init = 1   # the value of the parameter a to be used initially, when the graph is created




x = np.linspace(0, 10, 500)
fig = plt.figure(figsize=(8,3))
ax = plt.gca()

rectangle_ax = plt.axes([0.1, 0.2, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])

plt.title('varying rectangle')
#rectangles = [pch.Polygon([(0, 0), (0, a_init), (1/a_init, a_init), (1/a_init, 0)], closed=True, facecolor='blue', edgecolor = 'purple')]
#ax.add_patch(rectangles[-1])
#sin_plot, = plt.plot(x, np.sin(a_init*x), 'r')
#plt.xlim(0, 10)
#plt.ylim(0, 4)

# here we create the slider; parameters are:
# the axes object containing the slider; the name of the slider parameter, min, max, initial values of the parameter
a_slider = Slider(slider_ax, 'a', a_min, a_max, valinit=a_init)

# Next we define a function that will be executed each time the value
# indicated by the slider changes. The variable of this function will
# be assigned the value of the slider.
def update(a):
    poly = pch.Polygon([(0, 0), (0, a), (1/a, a), (1/a, 0)], closed=True, facecolor='blue', edgecolor = 'purple')
    ax.add_patch(poly) # set new y-coordinates of the plotted points
    fig.canvas.draw_idle() # redraw the plot

# the final step is to specify that the slider needs to execute the above function when its value changes
a_slider.on_changed(update)

fig.canvas.draw_idle()
plt.show(block=True)

