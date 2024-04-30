## Viikko 3

- Lisätty testikenttä, jonka avulla voi kehittää pelin mekaniikkoja.
- Kentässä voi epäonnistua tippumalla ruudusta ulos tai onnistua pääsemällä loppuun.
- Kentän voi aloittaa alusta.
- Lisätty luokat kentille, tasoille, pelaajalle ja taustalle.
- Lisätty pelaajalle kävely, juoksu ja hyppy.
- Hahmoteltu koodin rakennetta (moduulit).
- Testattu, että pelaaja voi liikkua x-tasolla eikä voi liikkua tason läpi.

## Viikko 4

- Pelin mekaniikkoja on kehitetty. Hahmo ei enää leiju satunnaisesti tasojen yläpuolella. Hyppiminen ja törmääminen muihin objekteihin on tarkempaa. Liikkuminen tuntuu paremmalta. Tähän meni yllättävän paljon aikaa.
- Lisätty neljä spriteä:
    - Nyrkki: Ilmestyy pelaajan eteen ja tuhoaa esteen. On olemassa tällä hetkellä yhdeksän ruudunpäivityksen ajan.
    - Este: Toimii kuten taso, mutta voidaan tuhota lyömällä.
    - Kolikko ja tähti: Kerättäviä esineitä, jotka kasvattavat numeroa peliluupissa, kun pelaajahahmo osuu niihin. Kolikko ei välttämättä näytä kolikolta.
- Tason uudelleenkäynnistys poistaa nyt spritet ennen uusien luomista.
- Ruudussa näkyvät teksteinä kerätyt kolikot ja tähdet. Samalla renderöijää on uudelleenjärjestetty siten, että ruudulle voi piirtää useita tekstejä.
- Hahmo lyö z-näppäimellä, eli nyrkki ilmestyy hetkeksi hahmon eteen. Jos nyrkki osuu esteeseen, este katoaa.
- Testattu hahmon ja nyrkin ominaisuuksia.

## Viikko 5

- Lisätty toinen testikenttä.
- Ruutu "liikkuu" nyt automaattisesti säädetyllä nopeudella. Käytännössä pelaajahahmo pysyy paikoillaan ja muut spritet liikkuvat vasemmalle.
- Kentässä soi nyt musiikki. Ruudun liikettä on pyritty synkkaamaan musiikin tahtiin, mutta sen kanssa on toistaiseksi ollut vaikeuksia.
- Aloitusruutu ja päävalikko lisätty. Päävalikosta voi valita kentän, muuta informaatiota ei ainakaan vielä näy.
- Päävalikkoon voi palata, kun kenttä on läpäisty. Pelisilmukkaan on siis lisätty toinen kerros.
- Liikkuminen on muutettu vapaasta liikkeestä automaattisesti etenevään muotoon. Muutos on tehty ajankäyttösyistä.
- Testattu kellon, tason ja esteen ominaisuuksia.

## Viikko 6

- Lisätty pause-ominaisuus p-näppäimeen. Pause pysäyttää pelin ja näyttää oman ruutunsa. Pausesta pääsee takaisin peliin tai päävalikkoon.
- Kentän läpäisynäkymästä pääsee suoraan päävalikkoon.
- Säädetty synkkausta musiikkiin, on nyt ehkä vähän parempi? Kello käyttää nyt tarkempaa tick_busy_loop-metodia.
- Päävalikossa näkyy nyt vain olemassa olevat kentät, ei mielivaltainen määrä kenttiä.
- Hyppykorkeus muuttuu, jos nappia pitää pohjassa.