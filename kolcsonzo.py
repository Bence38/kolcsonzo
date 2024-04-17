class Kolcson:
    def __init__(self,nev,jazon,eora,eperc,vora,vperc):
        self.nev = nev
        self.jazon = jazon
        self.eora = eora
        self.eperc = eperc
        self.vora = vora
        self.vperc = vperc
    def __str__(self):
        return f"Név {self.nev}, Járműazonosító {self.jazon}, Elvitel órája {self.eora} Elvitel perce {self.eperc}, Visszahoztal órája {self.vora}, Visszahozatal perce {self.vperc}"

f = open('kolcsonzesek.txt', 'rt', encoding = 'utf-8')
f.readline()
kolcsonzesek = []
for sor in f:  
    tmp = sor.strip().split(';')
    print(sor)  