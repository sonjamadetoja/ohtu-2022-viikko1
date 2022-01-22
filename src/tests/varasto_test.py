import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_liian_pieni_tilavuus(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_alkusaldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_liian_pieni_alkusaldo(self):
        varasto = Varasto(10, -10)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uudella_varastolla_liian_iso_alkusaldo(self):
        varasto = Varasto(10, 20)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_liian_pienella_saldolla(self):
        saldo_ensin = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, saldo_ensin)

    def test_lisays_liian_suurella_saldolla(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_liian_suuri_maara_palauttaa_oikein(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_liian_suuri_maara_tila_oikein(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(saatu_maara, 1)

    def test_string(self):

        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
