from module1 import *
palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("Keskmine palk - 1,\nMiinimumpalk - 2,\nMaksimaalne palk - 3,\nKustutada mees - 4,\n \nLisada mees - 5\n")
    if valik=="1":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)
        print()
        print()
    elif valik=="2":
        m_palgad,nimi=minimum(palk,inimesed)
        for n in nimi:
            print(m_palgad[0], " on saanud ",n)
            print()
            print()
    elif valik=="3":
        max_palk,kto=maksimum(palk,inimesed)
        print("Maksimaalne palk ", max_palk, " on saanud ",kto)
        print()
        print()
    elif valik=="4":                                       
        p,i=asdf(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Tühi list")
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," saab kätte ", palk[i])
    elif valik=="5":                                        
        i=zxcv(palk,inimesed)
        print("Ajakohastatud nimekirjad: ")
        print(inimesed)
        print(palk)
        print("Lisatud üksus", inimesed[-1])
        print("Koos palgaga", str(palk[-1])+'€')
while True:
    palgad(palk,inimesed)