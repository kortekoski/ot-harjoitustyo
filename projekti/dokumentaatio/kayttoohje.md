# Käyttöohje

Lataa ensin viimeisimmän [julkaisun](https://github.com/kortekoski/ot-harjoitustyo/releases) lähdekoodi.

## Asentaminen

Hakeudu kansioon, johon purit lähdekoodin, ja asenna riippuvuudet:

```bash
poetry install
```

## Käyttäminen

Ohjelma käynnistyy seuraavalla komennolla:

```bash
poetry run invoke start
```

Aloitusruutu aukeaa. Näkymästä pääsee päävalikkoon painamalla enteriä. Jos kadut päätöstäsi, peli sulkeutuu escillä.

![](./kuvat/screen1.png)

Ensin valitaan tallennuspaikka, johon tallentuu edistyminen kentissä sekä kerätyt kerättävät. Paikka valitaan enterillä. Deletellä tallennuspaikan voi halutessaan tyhjentää.

![](./kuvat/screen1b.png)

Seuraavassa ruudussa valitaan kenttä nuolinäppäimillä, minkä jälkeen peli alkaa enterillä. Aluksi vain taso 0 on auki; seuraava taso aukeaa, kun edellisen pääsee läpi. Takaisin tallennuspaikkavalikkoon pääsee askelapalauttimella.

![](./kuvat/screen2.png)

Tämän jälkeen pääsee itse pelinäkymään:

![](./kuvat/screen3.png)

Peli liikkuu itsestään. Tavoitteena on päästä tason loppuun ja kerätä mahdollisia kolikoita tai tähtiä. Jos hahmo putoaa ruudusta tai jää ruudun vasempaan laitaan, kenttä on epäonnistunut. Tällöin pelaaja voi aloittaa kentän alusta tai palata päävalikkoon.

## Näppäimet

Tässä on vielä esitettynä näppäimet, joilla peliä ohjataan.

### Alkunäkymä

- Enter: Aloittaa pelin.
- Escape: Sulkee pelin.

### Tallennuspaikkanäkymä

- Nuolinäppäimet: Valitsee tallennuspaikan.
- Enter: Valitsee tallennuspaikan.
- Delete: Tyhjentää tallennuspaikan.
- Escape: Sulkee pelin.

### Valikkonäkymä

- Nuolinäppäimet: Valitsee kentän.
- Enter: Aloittaa valitun kentän pelaaminen.
- Backspace: Palaa tallennuspaikkanäkymään.
- Escape: Sulkee pelin.

### Pelinäkymä

- Välilyönti: Hyppää. Näppäimen pohjassa pitäminen tekee hypystä korkeamman.
- Z: Lyö. Nyrkki tuhoaa pyöreät kiviesteet.
- P: Pysäyttää pelin (pause). Kun peli on pysäytetty, P jatkaa peliä.
- R: Aloittaa kentän alusta.
- Escape: Sulkee pelin. Kun peli on pausella tai pelaaja on epäonnistunut tasossa, palaa valikkonäkymään.
- Enter: Palaa valikkonäkymään, kun kenttä on läpäisty.