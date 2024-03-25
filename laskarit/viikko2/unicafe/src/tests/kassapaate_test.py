import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kela_gold = Maksukortti(1000)
        self.kela_silver = Maksukortti(100)

    def test_luotu_paate_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodussa_paatteessa_oikea_saldo(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_luodussa_paatteessa_oikeat_myynnit(self):
        self.assertEqual(self.kassapaate.myytyja_lounaita(), 0)

    ## Onnistunut edullinen käteisosto

    def test_edullinen_käteisosto_palauttaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_edullinen_käteisosto_kerryttää_kassaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)

    def test_edullinen_käteisosto_lisää_myynnin(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    ## Onnistunut maukas käteisosto

    def test_maukas_käteisosto_palauttaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_maukas_käteisosto_kerryttää_kassaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)

    def test_maukas_käteisosto_lisää_myynnin(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    ## Epäonnistunut edullinen käteisosto
        
    def test_epäonnistunut_edullinen_käteisosto_ei_lisää_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_epäonnistunut_edullinen_käteisosto_ei_lisää_myyntejä(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_epäonnistunut_edullinen_käteisosto_palauttaa_kaikki_rahat(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    ## Epäonnistunut maukas käteisosto

    def test_epäonnistunut_maukas_käteisosto_ei_lisää_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_epäonnistunut_maukas_käteisosto_ei_lisää_myyntejä(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_epäonnistunut_maukas_käteisosto_palauttaa_kaikki_rahat(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    ## Onnistunut edullinen korttiosto
        
    def test_onnistunut_edullinen_korttiosto_palauttaa_true(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kela_gold)
        self.assertEqual(tulos, True)

    def test_onnistunut_edullinen_korttiosto_veloittaa_kortilta_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kela_gold)
        self.assertEqual(self.kela_gold.saldo_euroina(), 7.60)
    
    def test_onnistunut_edullinen_korttiosto_lisää_myyntejä(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kela_gold)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_onnistunut_edullinen_korttiosto_ei_lisää_rahaa_kassaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kela_gold)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    ## Onnistunut maukas korttiosto
        
    def test_onnistunut_maukas_korttiosto_palauttaa_true(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kela_gold)
        self.assertEqual(tulos, True)

    def test_onnistunut_maukas_korttiosto_veloittaa_kortilta_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kela_gold)
        self.assertEqual(self.kela_gold.saldo_euroina(), 6.00)
    
    def test_onnistunut_maukas_korttiosto_lisää_myyntejä(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kela_gold)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_onnistunut_maukas_korttiosto_ei_lisää_rahaa_kassaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kela_gold)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    ### Epäonnistunut edullinen korttiosto
        
    def test_epäonnistunut_edullinen_korttiosto_palauttaa_false(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kela_silver)
        self.assertEqual(tulos, False)
        
    def test_epäonnistunut_edullinen_korttiosto_ei_vähennä_rahaa_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kela_silver)
        self.assertEqual(self.kela_silver.saldo_euroina(), 1.0)

    def test_epäonnistunut_edullinen_korttiosto_ei_lisää_myyntejä(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kela_silver)
        self.assertEqual(self.kassapaate.edulliset, 0)

    ### Epäonnistunut maukas korttiosto
        
    def test_epäonnistunut_maukas_korttiosto_palauttaa_false(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kela_silver)
        self.assertEqual(tulos, False)
        
    def test_epäonnistunut_maukas_korttiosto_ei_vähennä_rahaa_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kela_silver)
        self.assertEqual(self.kela_silver.saldo_euroina(), 1.0)

    def test_epäonnistunut_maukas_korttiosto_ei_lisää_myyntejä(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kela_silver)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    ### Kortin lataus
        
    def test_kortin_saldo_muuttuu_ladattaessa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kela_gold, 100)
        self.assertEqual(self.kela_gold.saldo_euroina(), 11.0)

    def test_kassan_saldo_muuttuu_ladattaessa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kela_gold, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)

    def test_kortin_saldo_ei_muutu_ladattaessa_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kela_silver, -100)
        self.assertEqual(self.kela_silver.saldo_euroina(), 1.0)

    def test_kassan_saldo_ei_muutu_ladattaessa_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kela_silver, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)