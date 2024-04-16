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