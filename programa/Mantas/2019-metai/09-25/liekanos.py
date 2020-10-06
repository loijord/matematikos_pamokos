#Si programa israso visu galimu formos *36* skaiciu liekanas dalijant is 84
for i in range(1,10):
    print('i =', i)
    print('sujungti skaiciai:', [int(str(i)+'36'+str(j)) for j in range(0,10)])
    print('dalybos liekanos:', [int(str(i)+'36'+str(j))%84 for j in range(0,10)])