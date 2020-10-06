## Ką veikėme per pamoką?
09-25 pamoką suinstaliavome Pycharm, tačiau jo paleisti nepavyko, nes neįdiegėme Python interpretatoriaus. Ypač daug užtruko kartojimasis to, ką rodžiau praeitą sykį: kintamųjų tipai, kokias operacijas bei funkcijas leistina atlikti su kintamaisiais, kaip aprašyti funkcijas ir daryti perrinkimus.
Aiškinomės, kaip kodą skaityti pažodžiui. Daug sykių kartojome, kaip parašyti komandą, nustatančią, ar duotas skaičius A dalijasi iš kito skaičiaus B. Likusį laiką aiškinomės, kaip rasti visus keturženklius sk., kurie turi viduryje 36 ir dalijasi iš 84 pagal namų darbą.

## Programavimo pratimai
1) Kokį rezultatą duos sudėties veiksmas šioms komandoms: ```'5281' + '4729'```, ```5281 + '4729'```, ```5281 + 4729```
2) Kaip sudauginti ```'kaip'``` su 50 ir ką sako rezultatas?
3) Kokią komandą reikia parašyti, norint nustatyti, ar skaičius A yra sveikasis?
4) Ką daro komandos ```int(X)```, ```str(X)```, ```float(X)```?
5) Ką daro komanda ```int('493b')```?
6) Ką daro komanda ```int(7457/18)```?
7) Ką daro komanda```int(7457/18) == 7457/18```?
8) Kaip parašyti programą, kuri išrašo visus keturženklius skaičius, kurie baigiasi 369?
9) Kaip parašyti programą, kuri patikrina visų tokių skaičių liekanas dalijant iš 84?
10) Ką maždaug reiškia programos pradžioje naudojama eilutė ```from random import randint```
11) Ką daro komanda ```type(654.953)```
12) Kodėl neveiks ši programa?
    ```
    from random import shuffle
    print(randint(10,99))
    ```
13) Kodėl nepavyko paleisti šios programos?
    ```
    def sujunk(a): int(str(a)+'369')
    for i in range(1,10): 
    print(sujunk(i))
    ```
## Kaip sekėsi Mantui?

Iš praeito karto visai nesisekė prisiminti, ką reiškia tokios komandos, kaip ```str``` ir ```int```. Vėliau tai vėl iškrisdavo iš galvos po 5 min. Po daugybės kartojimų išsiaiškinome, kas svarbiausia:
* ```int(X)``` paverčia X tipą į sveikąjį skaičių arba išskiria sveikąją dalį (*integer* - sveikasis skaičius)
* ```str(X)``` paverčia X tipą į realųjį skaičių (*float* - plūduriuoti) 
* ```float(X)``` paverčia X tipą į tekstinį (*string* - vėrinys)
* ```int, str, float``` taip pat gali reikšti ne komandas, o pačius kintamųjų tipus. Ateityje sakysiu pvz.: pasiversk skaičių į realų ir pan.
Tačiau pavyko pakeisti kodą, kad būtų perrenkami visi formos \*369 skaičiai. 

### Manto klausimas
Bekeičiant kodą kilo protingas klausimas:
    ```
    def sujunk(a): return int(str(a)+'369')
    for i in range(1,10): 
        print(sujunk(i))
    ```
Kodėl apačioje rašome ```sujunk(i)```, o ne ```sujunk(a)```? 

### Atsakymas
 ```def``` reiškia apibrėžti komandą (*define*). Ją galima apibrėžti kuriam tik nori kintamajam, nebūtinai *a* ir pirmą eilute pakeisti tokia:

```def sujunk(x): return int(str(x)+'369')``` arba pagal taisyklingo programavimo taisykles:

```def sujunk(pirmas_skaitmuo): return int(str(pirmas_skaitmuo)+'369')```

Apibrėžtą komandą atliekame būtent kintamajam *i*, kuris pereina skaičius nuo 1 iki 9, tad negalime vietoj jo rašyti kintamojo *a*, apie kurį nebuvo užsiimta kitur, kaip tik komandos apibrėžimo ribose. Už apibrėžimo ribų kintamasis *a* lieka nežinomas.
## Sudėtingesnės sąvokos, kurias aptarėme:
1) Realusis skaičius
2) Virtuali aplinka
3) Komandinė eilutė

## Namų darbai
1) Trikampį padalijame į keletą daugiakampių 2 tiesėmis ir užrašome skaičių rinkinį, parodantį, kokie tai daugiakampiai. Pavyzdžiui (3, 4, 4).
Reikia rasti visus tokius rinkinius. Vienodas situacijas atspindinčių rinkinių, pvz. (3, 4, 4) ir (4, 3, 4) nerašyti.
2) Surasti ir pavaizduoti visų pasaulio vandenynų skritulinę diagramą pagal plotą.
3) 09-25 dienos aplanke yra programa *temperatures.py*, kuri imituoja artimiausių 20 dienų orus. Ji atspausdino tokius duomenis:

```[ 3 10  3  6  4  6  7  4  8 10  8 11  2  7  5  7  1  2  2  0]```

Apskaičiuok šių duomenų vidurkį, medianą, modą ir nubražyk dažnių lentelę.

## Vėliau pridėsiu:
* daryto pratimo apžvalgą.
* atsakymus į programavimo klausimus.
## Šaltiniai
* [Kodėl būtent float?](https://www.quora.com/In-Python-why-is-float-called-float-Why-not-just-call-it-realnum-or-something)
* [Apie programavimą dar paprasčiau](https://cscircles.cemc.uwaterloo.ca/1-lt/)
* [Kur pasibandyti kodą, kol dar neveikia PyCharm?](http://pythontutor.com/visualize.html#mode=edit)
* [Instrukcijos kitai pamokai](https://github.com/loijord/Mantui)