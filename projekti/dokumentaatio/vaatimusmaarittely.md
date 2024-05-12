# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen tasohyppelypeli. Peli koostuu erillisistä kentistä, joissa ensisijaisena tavoitteena on päästä loppuun tekemättä virheitä ja toissijaisena tavoitteena kerätä kerättäviä esineitä. Ruutu liikkuu automaattisesti, joten pelaaja voi välttää putoamista tai ruudun vasempaan laitaan osumista hyppimällä ja lyömällä. Ruudun liike on _lähes_ synkronoitu taustalla soivaan "musiikkiin".

## Perusversion toiminnallisuus

### Perusnäkymä (aloitusruutu)
- Perusnäkymä aukeaa, kun sovelluksen avaa.
- Näkymästä pääsee eteenpäin tallennuspaikanvalintanäkymään.

### Tallennuspaikanvalintanäkymä
- Näkymässä voi valita tallennuspaikan, joka on nimetty numerolla.
- Näkymässä voi tyhjentää tallennuspaikan.
- Näkymästä pääsee kentänvalintanäkymään.

### Kentänvalintanäkymä
- Näkymästä voi valita kentän.
- Kentän kohdalla näkyy numero ja kerätyt esineet (tallennuspaikalla).
- Näkymästä pääsee valitun kentän pelinäkymään.
- Näkymästä pääsee takaisin tallennuspaikanvalintanäkymään.

### Pelinäkymä
- Pelinäkymä aukeaa, kun kenttä on valittu.
- Pelinäkymässä näkyy
  - hahmo
  - tasot ja esteet
  - kerättävät kolikot ja tähdet
  - tausta.
- Pelinäkymässä ruutu liikkuu automaattisesti hahmon mukana.
- Pelinäkymässä soi taustamusiikki.
- Pelinäkymästä siirrytään takaisin päävalikkoon, kun hahmo pääsee kentän loppuun tai pelaaja lopettaa hahmon kuoltua.

### Pelaajan hahmo
- Kävely: hahmo liikkuu x-akselilla itsestään.
- Hyppy: hahmo liikkuu y-akselilla ylöspäin välilyönnin painalluksesta, pohjassa pitäminen lisää korkeutta.
- Lyönti: hahmo iskee esteen rikki z-näppäimen painalluksesta.

### Kenttä
- Kenttä koostuu erinäisistä tasoista, joiden päällä hahmo voi liikkua tippumatta alas. Jos hahmo tippuu ruudun alalaitaan, kenttä on aloitettava alusta.
- Kentässä on kahdenlaisia esteitä: toiset täytyy väistää hyppäämällä, toiset tuhota lyömällä.
- Ruutu liikkuu automaattisesti eteenpäin.
- Kun pelaaja osuu ruudun alareunaan tai vasempaan reunaan, pelaaja on epäonnistunut kentän läpäisemisessä. Tällöin aukeaa valikko, josta voi valita, yrittääkö uudelleen (kenttä alkaa alusta) vai luovuttaako (siirrytään päävalikkoon).
- Kun saavuttaa kentän oikean reunan, se on läpäisty ja siirrytään päävalikkoon.
- Kentässä on kerättäviä kolikoita ja tähtiä, jotka saa kun hahmo osuu niihin. Kerätyt esineet tallentuvat tietokantaan ja näkyvät päävalikossa.
- Kentän voi koska vain pysäyttää (pause) tai aloittaa alusta (restart).

### Tallentaminen
- Aluksi auki on vain kenttä 1. Seuraavat kentät aukeavat, kun edeltävät saa läpäistyä.
- Edistymisen saa tallennettua kolmeen eri tallennuspaikkaan siten, että avatut kentät ja kerätyt esineet pysyvät muistissa.
- Tallennuspaikan voi tyhjentää.
- Tallennuspaikan valinnan ja kentän valinnan välillä voi liikkua vapaasti.

## Jatkokehitysideoita
- Käyttäjä voi itse määritellä pelin näppäimet.
- Kentissä on erilaisia liikkumisen muotoja.
- Hahmo voi lyömisen lisäksi ampua.
- Kentissä on esteiden lisäksi liikkuvia vihollisia.
- Kentät on rytmitetty musiikkiin.
- Kentissä on kohtia, joissa täytyy näppäillä tietty sarja näppäimiä rytmissä. Onnistumisesta saa bonuksen.
- Peli generoi yksinkertaisen kentän musiikkitiedoston pohjalta.
