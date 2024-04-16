# Ohjelmistotekniikan harjoitustyö: OT-Peli

Sovelluksen visio on tasohyppelypeli, jossa liikutaan musiikin rytmissä. Pelinäkymän toiminta on jo tyydyttävällä tasolla, peruspalikat ovat paikoillaan. Pelinäkymän liikkuva ruutu, valikkonäkymä ja pelitietojen tallentaminen ovat seuraavia ongelmia.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/kortekoski/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/kortekoski/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/kortekoski/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Komentorivitoiminnot

### Suorittaminen
```bash
poetry run invoke start
```

### Testaus
```bash
poetry run invoke test
```

### Testikattavuuden raportti
```bash
poetry run invoke coverage-report
```

Raportti löytyy hakemistosta _htmlcov_.