## Uždavinys apšilimui
![](Apšilimas.png)

Simon says: lengva, bet ar tai gyvenime naudinga?

Šiandien imsimės neįprastos veiklos: bandysime tai, ką mokėmės klasėje apie koordinates susieti 
su statistika, pakalbėti apie vaizdo atpažinimo matematiką ir turimas žinias pritaikyti dirbant su vaizdu. 
Realiai, imsime realų uždavinį ir pritaikysime realiame gyvenime.

## Ką veiksime
Imsiu ir pademonstruosiu dvi trimatės erdvės braižykles, kurias naudoju:
* ```pptk_demos.py```
* ```matplotlib_demos.py```

Ką galima naudingo su jomis nuveikti žiūrėkim pratimuose

## pratimai
Iš pradžių leiskime ```pptk_demos.py``` programą.
1. Galima pavaizduoti taškus formos (x; x²). Iš pradžių imkime x reikšmes -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 
ir suskaičiuokime taškų koordinates. 
Klausimas: kokias x reikšmes pasiūlytum imti, kad gautume tikslesnę taškinę diagramą?
Kokias reikšmes reikia imti, kad gautųsi vientisa linija?
2. Uždavinys: rasti atvirkštinį skaičiui 3. Bandykime nagrinėti šį uždavinį tokia seka:
    * išspręsti
    * apibendrinti
    * rasti pasitaikymo pavyzdžių, kad pavyktų apibendrinti
    * sukurti vizualizaciją, kad liktų atmintyje 
3. Tai, ką mokėmės mokykloje, yra dvimačiai taškai. 
Metas išeiti iš dvimatės erdvės narvo ir nusikelti į trimatę erdvę. Parašysiu formulę, kuri 
galbūt neaiški: (10*sin(x), 10*cos(x), 3*x) (bet aš vis tiek esu minėjęs, kad sinusai ir kosinusai 
yra susiję su taško judėjimu apskritimu, tai nieko čia baisaus). Žiūrime, kaip dabar taškai atrodo:
Ko dabar reiktų, kad linija gautųsi vientisa?
4. Kol kas mes kalbėjome vien apie taškus ir linijas. Dabar galime nusikelti į 
kartografinius taškų debesis. Kiekvienas taškas kompiuteryje saugomas kaip 3 koordinatės. 
O taškų gali būti ir keli šimtai milijonų. Faile yra 19488504 taškų - kiekvienas turi koordinačių trejetą.
Ar galima pasakyti bent vieno taško koordinatę iš paveikslėlių, kuriuos parodysiu?
5. Klausimas Mantui - kokius jo galva reiktų atlikti skaičiavimus, norint atskirti objektus?
6. Simonas tvirtina, kad visai nebūtina imti 20 milijonų taškų. Galime atskirti objektus 
ir daug mažesnės raiškos vaizde. Patyrinėkime programą, kuri nuskaito mano USB esantį failą.
ir vizualiai pavaizduoja duomenis. Jos apačioje parašyta, kad vaizduojama tik apie milijoną taškų, 
tačiau vaizdas nepakito, tik jo raiška. Kaip pavyko tai pasiekti?
7. Aptariame kubų idėją. Paaiškinu kubo prasmę: kubas žymimas, jei jame yra bent 1 taškas. Be to,
vaizdas (žmogaus) atpažįstamas ir iš kubų beveik taip pat sėkmingai. 
Kaip nustatyti, kuriame kube saugomas kiekvienas tris koordinates taškas? Bandykime pradėti šį klausimą 
nuo konkrečių atvejų.
8. Tarkime, jog Simonas kuria algoritmą, 
kaip atpažinti elektros laidus. Algoritmas veikia 30s. Iš jų 10s yra skiriama taškų grupavimui į kubus.
Tačiau grupavimą juk galima atlikti tik vieną kartą ir rezultatus kažkur išsaugoti, o po to kiekvienąsyk leidžiant 
programą užteks tik nuskaityti turimą rezultatą. 
Biblioteka, kurią Simonas naudoja, leidžia optimaliai saugoti tik matricose esančius duomenis. 
Kitu atveju duomenyse prirašomos tuščios reikšmės. Taikant šį metodą, duomenys įrašomi per 4 min.
Kaip būtų galima išvengti tuščių reikšmių įrašinėjimo? 
Užuomina: prisimename du metodus, kuriais rėmėmės sudarydami dažnių lentelę.
9. Simonas paaiškina, kas laikoma pirmu ir antru sluoksniais jo sukurtame vaizdo atpažinimo algoritme. 
Iš pradžių Simonas nori pasižiūrėti, kokius pirmus ir antrus sluoksnius turi kiekvienas į stulpą panašus objektas.
Jis gali atrinkti, kurie objektai yra iš tiesų stulpai ir jų sluoksnius pavaizduoti diagrama žalia spalva, 
o ne stulpų sluoksnius - mėlyna spalva. Ar įmanoma iš turimų diagramų (jas galime sukurti su atskira programa) 
nustatyti, kokiomis savybėmis skiriasi stulpai nuo kitų objektų?
10. Kiek liks laiko kalbame apie skirtumus tarp priešingo ir atvirkštinio skaičiaus (susiję su antru uždaviniu).




