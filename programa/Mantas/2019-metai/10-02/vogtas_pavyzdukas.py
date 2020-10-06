import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# tikrieji_balai = (np.random.randn(25)*10+30).astype(int)
# klaidos = np.random.random(15)*2
# plt.hist(len(tikrieji_balai), bins=range(10, 80, 2), edgecolor='black', linewidth=1.2, align='mid')

'''mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)'''

# the histogram of the data
'''n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()'''


class Data:
    def __init__(self, data):
        self.data = data

    def plot_msd(self):
        A = self.data
        plt.axhline(y=A.mean(), zorder=1, color='red')
        plt.axhspan(ymin=A.mean() - A.std(), ymax=A.mean() + A.std(), zorder=0, color='orange')
        plt.bar(range(len(A)), A, align='center', alpha=0.5)
        plt.show()

    def plot_distribution(self, gap=2, density=False, cum=0):
        A = self.data
        plt.hist(A, bins=np.arange(int(A.min()) - 1, int(A.max()) + 1, gap), density=density, cumulative=cum,
                 edgecolor='black', linewidth=1.2, align='mid')
        plt.show()
        # plt.hist(len(self.data), bins=range(10, 80, 2), edgecolor='black', linewidth=1.2, align='mid')

    def get_sd(self, opt=True):
        print('SEKOS STANDARTINIS NUOKRYPIS')

        def br(n):
            if n < 0:
                return '(' + str(round(n, 2)) + ')'
            else:
                return str(round(n, 2))

        if opt: print('Turime duomenis:')
        for n in self.data:
            if opt: print(br(n), end=', ')
        if opt: print()
        if opt: print('1) Vidurkis:', self.data.mean())
        if opt: print('2) Nauja seka su atimtais vidurkiais:')
        for n in self.data - self.data.mean():
            if opt: print(round(n, 2), end=', ')
        if opt: print()
        if opt: print('3) Kvadratu suma:')
        a = self.data - self.data.mean()
        if opt: print(' + '.join([br(n) + chr(178) for n in a]), '=', round(sum(a ** 2), 2))
        if opt: print('4) Dalijam is', len(a) - 1, 'ir traukiam sakni:', round((sum(a ** 2) / (len(a) - 1)) ** 0.5, 2))
        if opt: print('TIKRASIS NUOKRYPIS:', self.data.std(ddof=1))
        if opt: print()
        return self.data.std(ddof=1)

    def get_zscores(self, opt=True):
        def br(n):
            if n < 0:
                return '(' + str(round(n, 2)) + ')'
            else:
                return str(round(n, 2))

        print('SEKOS KONVERTAVIMAS I Z-BALUS')
        if opt: print('Turime duomenis:')
        for n in self.data:
            if opt: print(n, end=', ')
        if opt: print()
        if opt: print('1) Vidurkis:', round(self.data.mean(), 2))
        if opt: print('2) St. nuokrypis:', round(self.data.std(ddof=1), 2))
        if opt: print('3) Nauja seka su atimtais vidurkiais:')
        for n in self.data - self.data.mean():
            if opt: print(round(n, 2), end=', ')
        if opt: print()
        if opt: print('4) Nauja seka padalijus is nuokrypiu:')
        for n in (self.data - self.data.mean()) / self.data.std(ddof=1):
            if opt: print(round(n, 2), end=', ')
        if opt:
            print()
            print()
        return (self.data - self.data.mean()) / self.data.std(ddof=1)

    def get_tscores(self, opt=True):
        print('SEKOS KONVERTAVIMAS I T-BALUS')
        if opt: print('Turime duomenis:')
        for n in self.data:
            if opt: print(n, end=', ')
        if opt: print()
        if opt: print('1) Turejome moketi rasti nariams z-balus:')
        for n in (self.data - self.data.mean()) / self.data.std(ddof=1):
            if opt: print(round(n, 2), end=', ')
        print()
        if opt: print('2) Kiekviena nari dauginsim is 10 ir pridesim 50:')
        for n in 10 * (self.data - self.data.mean()) / self.data.std(ddof=1) + 50:
            if opt: print(round(n, 2), end=', ')
        if opt: print()
        return 10 * (self.data - self.data.mean()) / self.data.std(ddof=1) + 50

    def get_reliabilty(self, artificial_error=2, opt=True):
        gen = np.random.randn(len(self.data)) * artificial_error
        measured_data = self.data + gen
        print('PATIKIMUMAS r')
        if opt: print('Tarkime, kad tikrieji balai:')
        for n in self.data:
            if opt: print(round(n, 2), end=', ')
        if opt: print()
        if opt: print('Kompiuteris sugeneravo dirbtines matavimo klaidas:')
        for n in gen:
            if opt: print(round(n, 2), end=', ')
        if opt: print()
        if opt: print('Taip buvo gauti dirbtiniai ismatuoti balai:')
        for n in measured_data:
            if opt: print(round(n, 2), end=', ')
        print()
        print()
        print('PATIKIMUMAS r = tikruju balu dispersija padalinta padalinta is ismatuotu balu dispersijos =')
        print(round(self.data.var(ddof=1), 2), ':', round(measured_data.var(ddof=1), 2), '=',
              round(self.data.var(ddof=1) / measured_data.var(ddof=1), 2))


def methods():
    data1 = Data((np.random.randn(35) * 20 + 35).astype(int))
    yield data1.plot_msd()
    yield data1.plot_distribution(gap=5)
    data2 = Data((np.random.randn(35) * 5 + 50).astype(int))
    yield data2.plot_msd()
    yield data2.plot_distribution(gap=1)
    # print(data2)
    data3 = Data((np.random.randn(350) * 35 + 100).astype(int))
    yield data3.plot_msd()
    yield data3.plot_distribution(gap=10)


def methods2():
    data1 = Data((np.random.randn(35) * 20 + 35).astype(int))
    yield data1.plot_msd()
    yield data1.plot_distribution(gap=5)
    data2 = Data(data1.get_zscores(False))
    yield data2.plot_msd()
    yield data2.plot_distribution(gap=0.5)
    # print(data2)
    data3 = Data(data1.get_tscores(False))
    yield data3.plot_msd()
    yield data3.plot_distribution(gap=5)
    yield data3.plot_distribution(gap=5)


def methods3():
    data = Data((np.random.randn(35) * 5 + 35).astype(int))
    yield data.plot_distribution(gap=1)
    yield data.plot_distribution(gap=1, cum=1)

    def m(x, pos): return '%s' % (round(x * 100, 2))

    formatter = FuncFormatter(m)
    plt.gca().yaxis.set_major_formatter(formatter)
    yield data.plot_distribution(gap=1, density=True)
    plt.gca().yaxis.set_major_formatter(formatter)
    yield data.plot_distribution(gap=1, density=True, cum=1)


names = ['imtis1', 'imtis2', 'imtis3', 'skirstinys1', 'skirstinys2', 'skirstinys3']
names2 = ['imtis', 'z-balai', 't-balai', 'skirstinys', 'skirstinys z-balams', 't-balams']
names3 = ['skirstinys', 'skirstinys(procentais)', 'kaupiamasis skirstinys', 'kaupiamasis skirstinys(procentais)']

width, height = 2, 3
meth = methods()

for i in range(width * height):
    def f(i, a, b):
        # return i
        return (i % a) * b + i // a


    plt.subplot(width, height, f(i, width, height) + 1)
    next(meth)
    plt.title(names2[f(i, width, height)])

plt.tight_layout()
plt.show()

data2 = Data((np.random.randn(7) * 5 + 50).astype(int))
data2.get_sd()
data2.get_zscores()
data2.get_tscores()
data2.get_reliabilty(1)
