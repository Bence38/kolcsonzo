class Kolcsonzes:
    def __init__(self,nev,jazon,eora,eperc,vora,vperc):
        self.nev = nev
        self.jazon = jazon
        self.eora = eora
        self.eperc = eperc
        self.vora = vora
        self.vperc = vperc
    def __str__(self):
        return f"Név: {self.nev}, Járműazonosító: {self.jazon}, Elvitel órája: {self.eora} Elvitel perce: {self.eperc}, Visszahoztal órája: {self.vora}, Visszahozatal perce: {self.vperc}"

f = open('kolcsonzesek.txt', 'rt', encoding = 'utf-8')
f.readline()
kolcson = {}
kolcsonzesek = []
for sor in f:  
    tmp = sor.strip().split(';')
    kolcsonzesek.append(Kolcsonzes(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5]))
    #print(sor)  
for kolcsonzo in kolcsonzesek:
    print(kolcsonzo)
print('5.feladat')
print(f'Napi kölcsönzések száma: {len(kolcsonzesek)}')
print('6.feladat')
nev = input('Kérek egy nevet:')
if nev == tmp[0]:
    print('Kata kölcsönzései')
    print(tmp[3],tmp[4],tmp[5])

