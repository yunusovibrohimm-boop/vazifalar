# xizmat.py — 🧠 Mantiqchi
import json
from model import Vazifa


class Royxat:
    def __init__(self):
        self.vazifalar = []

    def __len__(self):
        return len(self.vazifalar)

    def qosh(self, matn, muhim=False):
        vazifa = Vazifa(matn, muhim)
        self.vazifalar.append(vazifa)
        return len(self.vazifalar) - 1

    def bajar(self, idx):
        v = self.vazifalar[idx]

        if v.bajarildi:
            return False

        v.bajar()
        return True

    def ochir(self, idx):
        del self.vazifalar[idx]

    def bajarilmaganlar(self):
        return [v for v in self.vazifalar if not v.bajarildi]
