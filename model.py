# model.py — Kapitan
class Vazifa:
    def __init__(self, matn, muhim=False):
        if matn.strip() == "":
            raise ValueError("Matn bo'sh bo'lmasin")
        self.matn = matn.strip()
        self.muhim = muhim
        self.bajarildi = False

    def bajar(self):
        self.bajarildi = True

    def __str__(self):
        belgi = "[x]" if self.bajarildi else "[ ]"
        yulduz = " ⭐" if self.muhim else ""
        return f"{belgi} {self.matn}{yulduz}"


# test_xizmat.py — Kapitan yozadi, Mantiqchi kodini tekshiradi
import unittest, os
# from xizmat import Royxat

class RoyxatTest(unittest.TestCase):
    def setUp(self):
        self.r = Royxat()
        self.r.qosh("Dars qilish")

    def test_qosh(self):
        idx = self.r.qosh("Non olish")
        self.assertEqual(idx, 1)
        self.assertEqual(len(self.r), 2)

    def test_bajar(self):
        self.assertTrue(self.r.bajar(0))
        self.assertFalse(self.r.bajar(0))

    def test_saqla_yukla(self):
        self.r.saqla("test_tmp.json")
        r2 = Royxat.yukla("test_tmp.json")
        self.assertEqual(len(r2), 1)
        self.assertEqual(r2.vazifalar[0].matn, "Dars qilish")

    def test_yoq_raqam(self):
        with self.assertRaises(IndexError):
            self.r.bajar(5)

    def tearDown(self):
        if os.path.exists("test_tmp.json"):
            os.remove("test_tmp.json")