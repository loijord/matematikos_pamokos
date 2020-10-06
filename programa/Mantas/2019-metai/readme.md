# Kaip mums bendrauti?
Stengsimės bendrauti bent jau iš dalies taip, kaip bendrauja programuotojai. Naudosime Git.
# Kas yra Git?
Visa informacija pateikta šiame [puslapyje](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861/).
Kad būtų paprasčiau, išversiu pagrindines idėjas:
* Šis įrankis yra pati populiariausia pasaulyje ir visuotiškai primta naudoti versijų kontrolės sistema (Version Control System, trumpinama VCS).
* Version control system - tai kol kas mokyklose negirdėtas dalykas. Net ir per informatikos pamokas. Tačiau pati idėja, kam programuotojui prireikia naudoti VCS, nėra sudėtinga. Įsivaizduokime, kad grupė programuotojų kuria projektą, kurį sudaro daugybė failų su kodu. Dalis tų failų yra keičiami vieno ar kelių žmonių, tačiau dabartinė projekto versija gali būti tik vienintelė, suklijuota iš failų, kurie negali turėti keletos skirtingų versijų.
Tam ir prireikia versijų kontrolės sistemos. Ji leidžia saugoti visus pakeitimus, kuriuos atlieka kiekvienas programuotojas individualiai ir juos kombinuoti visiems suprantamu būdu.
* Git leidžia perkelti projektus į internetą. Populiariausi saugojimo serveriai yra GitHub, BitBucket ir GitLab. Mes naudosime Github.
* Šiandieniniame pasaulyje programuotojai nebebendrauja laiškais persiuntinėdami vienas kitam kodą. Kodas yra keliamas į internetą ir prieinamas tik uždarai grupei žmonių arba visiems. Atnaujintą kodą galima sukelti į internetą vienu paspaudimu kada tik nori.
* Štai [pavyzdys](https://github.com/trokas/ai_primer), kaip atrodo sukeltas projektas. 
## Kaip parsisiųsti Pycharm ir per jį paleisti Python?

## Kaip parsisiųsti projektą?
* Susikuriame naują projektą. Spaudžiame (```File -> New Project```).
* Pycharm programos apačioje surandame terminalą (Terminal) ir parsisiunčiame projektą. Įvedame:
* ```git clone https://github.com/loijord/Mantui```
* Parsiųstame projekte galime daryti pakeitimus, kokius tik norime.

## Kaip pasiruošti pakeisto projekto kėlimui į internetą?
* Pirmiausia reikia turėti, kur sukelti. Tam reikės susikurti paskyrą GitHube. 
Einame į [GitHub](https://github.com) ir sukuriame ten paskyrą (reikės slaptažodžio patvirtinimo paštu).
* Susikuriame naują projektą Pycharme (```File -> New project```) ir sugalvojame jam pavadinimą.
* Projektas yra kuriamas virtualioje aplinkoje. Susikūrus projektui turime aktyvuoti versijų kontrolę (```VCS -> Enable Version Control Integration```) ir naujai atsidariusiame lange pasirenkame Git.
* Dabar reikės susieti versijų kontrolės sistemą su Github (```VCS -> Import into Version Control -> Share Project on GitHub```), įvedame savo paskyros duomenis ir pasirenkame, kuriuos failus norim sukelti.
* Galime atsidaryti savo anketą per internetą ir įsitikinti, kad paskyra pasipildė nauju projektu.

## Kaip sukelti projektą keliais paspaudimais?
* Klaviatūros kombinacija CTRL + K padės išrinkti failus, kuriuos norime atšviežinti (**pull**). Būtų gerai atsidariusiame lange įrašyti, ką keičiame. Pastabos gali prasidėti tokias žodžiais kaip *bugfix*, *feature*, *update* ir pan.
* Klaviatūros kombinacija CTRL + SHIFT + K padės sukelti jau išsirinktus failus (**push**)

## Dėl bendros tvarkos
Kiekviena pamoka turės savo aplanką, kurio pavadinimas yra tos dienos data. Aplankuose bus:
* python failai (.py). tai yra python programos, skirtos pademonstruoti sprendimams arba kam nors pavaizduoti.
* readme.md failas - tai, ką sprendėme per pamoką, kas pavyko ir kas nepavyko.
* readme.pdf failas - tas pats, kas ir readme.md faile, jeigu prireiks įmantresnio teksto (dažniausiai formulių, diagramų).
Visas projektas taip pat turės:
* *venv* aplanką
* *.gitignore* failą
* *requirements.txt* failą
* *backlog.md* failą
apie juos truputį vėliau.

Be to, natūralu, jog kai kurias demonstracijas programuoti pamokos metu yra sunkoka dėl laiko trūkumo. Tad Simonas kai kurias programas ir iliustracijas kurs iš namų ir įkels praėjus šiek tiek laiko po pamokos.

## Ką daryti, jeigu Simonas išėjo, bet liko klausimų?
Reikia pakeisti paskutinės pamokos readme.md failą jame pridedant rūpimą klausimą, projektą *supull'inti* su CTRL+K ir *supush'inti* su CTRL+SHIFT+K.  
Ar yra šviežių atnaujinimų, galime pasitikrinti [šiame puslapyje](https://github.com/loijord/Mantui). Jeigu yra, juos parsisiunčiame terminale įvedę ```git clone https://github.com/loijord/Mantui```.

## Papildoma pastaba

Pycharm suinstaliuoti nepakanka. Jo nustatymuose reikia nurodyti kelią iki Python interpretatoriaus. Aš parsisiunčiu 
Python 3.7 iš oficialaus puslapio python.org (prieš tai nepamirštu patikrinti, ar sistema yra 32 bitų, ar 64 bitų). Tačiau parsisiųsti Python nepakanka. 
Galima remtis [šiuo siūlomu sprendimu](https://stackoverflow.com/a/55796938/3044825).

* Jei Pycharm jau suinstaliuotas:

1) einam į file -> Settings -> Project ..., Pasirenkame Python interpreter ir spaudžiame '+', kad pridėtume kelią ligi interpretatoriaus.
2) mano nustatymai tokie:
"![](langas1.png)"

* Jei prašo nurodyti kelią iki interpretatoriaus instaliacijos metu:
![](langas2.png)