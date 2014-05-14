import math

class Kolo():
    def __init__(self, promien):
        self.promien = float(promien)
    def wyliczPole(self):
        pole = math.pi * (self.promien ** 2)
        return pole

class Prostokat():
    def __init__(self, bok1, bok2):
        self.bok1 = float(bok1)
        self.bok2 = float(bok2)
    def wyliczPole(self):
        pole = self.bok1 * self.bok2
        return pole

class Trojkat():
    def __init__(self, bok1, bok2, bok3):
        self.bok1 = float(bok1)
        self.bok2 = float(bok2)
        self.bok3 = float(bok3)
    def wyliczPole(self):
        p = (1 / 2) * (self.bok1 + self.bok2 + self.bok3)
        pole = (p * (p - self.bok1) * (p - self.bok2) * (p - self.bok3)) ** (1 / 2)
        return pole
    
try:
    liczbaFigur = int(input())
except ValueError as err:
    print(err)

poleFigur = 0
for i in range(liczbaFigur):
    try: 
        inp = input().split()
        if len(inp) == 1:
            figura = Kolo(inp[0])
            pole = figura.wyliczPole()
            poleFigur+=pole
        elif len(inp) == 2:
            figura = Prostokat(inp[0], inp[1])
            pole = figura.wyliczPole()
            poleFigur+=pole
        elif len(inp) == 3:
            figura = Trojkat(inp[0], inp[1], inp[2])
            pole = figura.wyliczPole()
            poleFigur+=pole
        else:
            pass
    except ValueError as err:
        print(err)  

poleFigur = round(poleFigur, 2)
print(poleFigur)

poleFigur1 = round(poleFigur, 0)
print(poleFigur1)

poleFigur2 = round(poleFigur, 3)
print(poleFigur2)
