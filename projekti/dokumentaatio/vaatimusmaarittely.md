# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on tasohyppely- ja rytmipelin risteytys, jossa pelaaja juoksee eteenpäin ja väistää tai tuhoaa samalla esteitä musiikin tahtiin. Peli koostuu erillisistä kentistä, joissa ensisijaisena tavoitteena on päästä loppuun tekemättä virheitä ja toissijaisena tavoitteena kerätä kerättäviä esineitä.

## Perusversion suunnitellut toiminnallisuudet

### Perusnäkymä (päävalikko)
- Perusnäkymä aukeaa, kun sovelluksen avaa. (TEHTY)
- Perusnäkymästä voi valita kentän. (TEHTY)
- Perusnäkymästä voi valita tallennuspaikan.
- Kentän kohdalla näkyy nimi ja esittelykuva. Jos kenttä on jo läpäisty, näkyvät myös kerätyt esineet.

### Pelinäkymä
- Pelinäkymä aukeaa, kun kenttä on valittu.
- Pelinäkymässä näkyy (TEHTY)
  - hahmo (hieman näkymän keskustasta vasemmalle)
  - tasot ja esteet
  - taustakuva.
- Pelinäkymässä ruutu liikkuu hahmon mukana. (TEHTY)
- Pelinäkymässä soi taustamusiikki. (TEHTY)
- Pelinäkymästä siirrytään takaisin päävalikkoon, kun hahmo pääsee kentän loppuun.

### Pelaajan hahmo (TEHTY)
- Kävely: hahmo liikkuu x-akselilla itsestään.
- Hyppy: hahmo liikkuu y-akselilla ylöspäin välilyönnin painalluksesta, pohjassa pitäminen lisää korkeutta.
- Lyönti: hahmo iskee esteen rikki z-näppäimen painalluksesta.

### Kenttä
- Kenttä koostuu erinäisistä tasoista, joiden päällä hahmo voi liikkua tippumatta alas. Jos hahmo tippuu ruudun alalaitaan, kenttä on aloitettava alusta. (TEHTY)
- Kentässä on kahdenlaisia esteitä: toiset täytyy väistää hyppäämällä, toiset tuhota lyömällä. (TEHTY)
- Ruutu liikkuu automaattisesti eteenpäin. (TEHTY)
- Joten kun pelaaja osuu ruudun alareunaan, esteesen tai seinään, hahmo räjähtää ja pelaaja on epäonnistunut kentän läpäisemisessä. Tällöin aukeaa valikko, josta voi valita, yrittääkö uudelleen (kenttä alkaa alusta) vai luovuttaako (siirrytään päävalikkoon).
- Kun saavutaa kentän oikean reunan, se on läpäisty ja siirrytään päävalikkoon.
- Tasot ja esteet on ajoitettu taustamusiikin mukaisesti siten, että jos pelaaja ajoittaa hypyt ja lyönnit oikein rytmiin, hän onnistuu läpäisemään kentän.
- Kentässä on viisi kerättävää erikoisesinettä, jotka saa kun hahmo osuu niihin. (TEHTY)
- Kentässä on myös vähemmän erikoisia esineitä (esim. kolikoita), jotka saa kun hahmo osuu niihin. (TEHTY)

### Tallentaminen
- Aluksi auki on vain kenttä 1. Seuraavat kentät aukeavat, kun edeltävät saa läpäistyä. 
- Edistymisen saa tallennettua kolmeen eri tallennuspaikkaan siten, että avatut kentät ja kerätyt esineet pysyvät muistissa.
- Tallennuspaikan voi tyhjentää.

## Jatkokehitysideoita
- Käyttäjä voi itse määritellä pelin näppäimet.
- Pelinäkymän voi pysäyttää esc-näppäimellä. Tämä johtaa pysäytysnäkymään, jossa on valikko. Valikosta voi siirtyä takaisin liikkuvaan peliin, kentän alkuun tai päävalikkoon.
- Kentissä on erilaisia liikkumisen muotoja.
- Hahmo voi lyömisen lisäksi ampua.
- Kentissä on esteiden lisäksi liikkuvia vihollisia.
- Kentissä on kohtia, joissa täytyy näppäillä tietty sarja näppäimiä rytmissä. Onnistumisesta saa bonuksen.
- Peli generoi yksinkertaisen kentän musiikkitiedoston pohjalta.
