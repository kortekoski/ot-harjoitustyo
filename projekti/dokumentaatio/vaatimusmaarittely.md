# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on tasohyppely- ja rytmipelin risteytys, jossa pelaaja juoksee eteenpäin ja väistää tai tuhoaa samalla esteitä musiikin tahtiin. Peli koostuu erillisistä kentistä, joissa ensisijaisena tavoitteena on päästä loppuun tekemättä virheitä ja toissijaisena tavoitteena kerätä kerättäviä esineitä.

## Perusversion suunnitellut toiminnallisuudet

### Perusnäkymä (päävalikko)
- Perusnäkymä aukeaa, kun sovelluksen avaa.
- Perusnäkymästä voi valita ensin tallennuspaikan ja sitten kentän.
- Kentän kohdalla näkyy nimi ja esittelykuva. Jos kenttä on jo läpäisty, näkyvät myös kerätyt esineet.

### Pelinäkymä
- Pelinäkymä aukeaa, kun kenttä on valittu.
- Pelinäkymässä näkyy
  - hahmo (hieman näkymän keskustasta vasemmalle)
  - tasot ja esteet
  - taustakuva.
- Pelinäkymässä ruutu liikkuu hahmon mukana.
- Pelinäkymässä soi taustamusiikki.
- Pelinäkymästä siirrytään takaisin päävalikkoon, kun hahmo pääsee kentän loppuun.

### Pelaajan hahmo
- Kävely: hahmo liikkuu x-akselilla, kun vasenta/oikeaa nuolta pidetään pohjassa.
- Juoksu: hahmo liikkuu nopeammin x-akselilla, kun vaihtonäppäintä pidetään pohjassa samaan aikaan kun kävellään.
- Hyppy: hahmo liikkuu y-akselilla ylöspäin välilyönnin painalluksesta, pohjassa pitäminen lisää korkeutta.
- Lyönti: hahmo iskee esteen rikki z-näppäimen painalluksesta.

### Kenttä
- Kenttä koostuu erinäisistä tasoista, joiden päällä hahmo voi liikkua tippumatta alas. Jos hahmo tippuu ruudun alalaitaan, kenttä on aloitettava alusta.
- Kentässä on kahdenlaisia esteitä: toiset täytyy väistää hyppäämällä, toiset tuhota lyömällä.
- Vasemmalta pelaajaa lähestyy koko ruudun korkuinen seinä, joka pakottaa pelaajan liikkeelle.
- Joten kun pelaaja osuu ruudun alareunaan, esteesen tai seinään, hahmo räjähtää ja pelaaja on epäonnistunut kentän läpäisemisessä. Tällöin aukeaa valikko, josta voi valita, yrittääkö uudelleen (kenttä alkaa alusta) vai luovuttaako (siirrytään päävalikkoon).
- Kun saavutaa kentän oikean reunan, se on läpäisty ja siirrytään päävalikkoon.
- Tasot ja esteet on ajoitettu taustamusiikin mukaisesti siten, että jos pelaaja ajoittaa hypyt ja lyönnit oikein rytmiin, hän onnistuu läpäisemään kentän.
- Kentässä on viisi kerättävää erikoisesinettä, jotka saa kun hahmo osuu niihin.
- Kentässä on myös vähemmän erikoisia esineitä (esim. kolikoita), jotka saa kun hahmo osuu niihin.

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
