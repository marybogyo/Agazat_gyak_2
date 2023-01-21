class Lotto:
    def __init__(self, sor):
        self.id = sor[0]
        self.ev = int(sor[1])
        self.het = int(sor[2])
        self.szam1 = int(sor[3])
        self.szam2 = int(sor[4])
        self.szam3 = int(sor[5])
        self.szam4 = int(sor[6])
        self.szam5 = int(sor[7])
        self.szam6 = int(sor[8])

    def __str__(self):
        return f"{self.id}, {self.ev}, {self.het}, {self.szam1}, {self.szam2}, {self.szam3}, {self.szam4}, {self.szam5}, {self.szam6}"
