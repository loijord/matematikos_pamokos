import matplotlib.pyplot as plt
#sources:
#1) ivedu Google uzklausa matplotlib draw circle diagram, kuri nera tiksli.
# einu i nuoroda, kuri zada skrituline diagrama: https://pythonspot.com/matplotlib-pie-chart/
# kopijuoju ir perdarau koda
# vandenynu statistika: https://en.wikipedia.org/wiki/Ocean


# 2) Data to plot

def draw_diagram(data):
    #plots piechart of your data given as dictionary of parameters
    plt.pie(data['sizes'],
            explode=data['explode'],
            labels=data['labels'],
            colors=data['colors'],
            autopct='%1.1f%%',
            shadow=True,
            startangle=140)
    plt.axis('equal')
    plt.show()

data1 = {'labels': ['Python', 'C++', 'Ruby', 'Java'],
    'sizes': [215, 130, 245, 210],
    'colors': ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'],
    'explode': (0.2, 0, 0, 0)}  # explode 1st slice

data2 = {'labels': ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'],
    #'sizes': [16872300046.6, 8513300023.5, 70560000195, 219600006.1, 155580004.3],
    'sizes': [177, 82, 75, 22, 14],
    'colors': ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lime'],
    'explode': (0, 0, 0, 0, 0)}  # explode 1st slice

data3 = {'labels': ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic'],
    'sizes': [66988000050.1, 31041090023.3, 26400000019.8, 718000005.4, 187500001.4],
    'colors': ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lime'],
    'explode': (0, 0, 0, 0, 0)}  # explode 1st slice

draw_diagram(data1)
draw_diagram(data2)
draw_diagram(data3)
