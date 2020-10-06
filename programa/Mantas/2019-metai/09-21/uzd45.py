#Si programa patikrina visus variantus, ka reikia irasyti vietoj
#zvaigzduciu uzrase *45*, kad gautas skaicius dalytusi is 18

# 1) atveju naudojame paprasta prijungima:
def sujunk_pirmu_budu(a,b): return int(str(a)+'45'+str(b))
print('Pirmas budas:')
for i in range(1,10):
    for j in range(0,10):
        if sujunk_pirmu_budu(i,j)/18 == int(sujunk_pirmu_budu(i,j)/18):
            print(sujunk_pirmu_budu(i,j))

# 2) atveju naudojame labiau matematini buda sudaryti reiskiniu taip, kaip mokys velesnese klasese:
def sujunk_antru_budu(a,b): return 1000*a + 450 + b
print('Antras budas:')
for i in range(1,10):
    for j in range(0,10):
        if sujunk_antru_budu(i,j)/18 == int(sujunk_antru_budu(i,j)/18):
            print(sujunk_antru_budu(i,j))