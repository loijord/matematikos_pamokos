#duomenu srautas, is kurio kompiuteris duomenu nemato:
srautas = '3 10  3  6  4  6  7  4  8 10  8 11  2  7  5  7  1  2  2  0'
#tie patys duomenys, pateikiami kaip skaiciu sarasas
duomenys = [int(n) for n in srautas.split(' ') if n != '']

#tam, kad palygintume:
print(srautas)
print(duomenys)

#kiekvienam elementui duomenu aibeje: parasome, kiek kartu tas elementas pasitaike
for n in set(duomenys):
    print('elementas=',n, 'kiek pasitaike:', duomenys.count(n))