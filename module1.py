def (palg,inimesed):
    add=input("sisesta nimi: ")
    inimesed.append(add)
    add_zp=int(input("sisesta palga: "))
    palg.append(add_zp)
    return palg,inimesed
def zxcv(palg,inimesed):
    add=input("nimi inemene:  ")
    inimesed.append(add)
    add_palg=int(input("palga inimene:  " ))
    palg.append(add_palg)
    return palg,inimesed
    print()
    print()
def asdf(palg, inimesed):
    x=input("Kasutaja nimi on kirjutatud tähtedega - 1 või numbritega - 2? ")
    if x=="2":
        i=int(input("sisesta number: "))
        palg.pop(i-1)
        inimesed.pop(i-1)
    elif x=="1":
        i=0
        keda=input("sisesta nimi: ")
        n=len(inimesed)
        while i<n:
            if keda==inimesed[i]:
                inimesed.pop(i)
                palg.pop(i)
                n=len(inimesed)
            else:
                i+=1
def kustutamine():
    keskmin = keskmine(palg)
    print(keskmin)
    for i in palg:
        if i < kesk:
            index = palg.index(i)
            palg.pop(index)
            inimesed.pop(index)
            print()
            print()
def nimi(palg,inimesed):
    ots_nimi=[]
    ots_palg=[]
    palg_keda=0
    keda=input("sisesta nimi: ")
    n=len(inimesed)
    for j in range(n):
        if inimesed[j]==keda:
            palg_keda=palg[j]
            ots_nimi.append(inimesed[j])
            ots_palg.append(palg_keda)
            print()
            print()
        else:pass
    return ots_nimi,ots_palg
    print()
    print()
def maksimum(palg,inimesed):
    m_palgad=[]
    nimed=[]
    max_palg=palg[0]
    kellel=inimesed[0]
    for p in palg:
        if p>max_palg:
            max_palg=p
            i=palg.index(max_palg)
            kellel=inimesed[i]
            print()
            print()
    n=palg.count(max_palg)
    palg_copy=palg.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palg_copy.index(max_palg)
        m_palgad.append(palg_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed
    print()
    print()
def minimum(palg,inimesed):
    m_palgad=[]
    nimed=[]
    min_palg=palg[0]
    kellel=inimesed[0]
    for p in palg:
        if p<min_palg:
            min_palg=p
            i=palk.index(min_palg)
            kellel=inimesed[i]
    n=palk.count(min_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palk_copy.index(min_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed
    print()
    print()
def keskmine(palg):
    summa=0
    n=len(palg)
    for p in palg:
        summa+=p
    k=summa/n
    return k
    print()
    print()
def nimi(palg,inimesed):
    ots_nimi=[]
    ots_palg=[]
    palg_keda=0
    keda=input("sisesta nimi: ")
    n=len(inimesed)
    for j in range(n):
        if inimesed[j]==keda:
            palg_keda=palg[j]
            ots_nimi.append(inimesed[j])
            ots_palg.append(palg_keda)
            print()
            print()
        else:pass
    return ots_nimi,ots_palg
    print()
    print()
def otsiing_palgad_jargi(inimesed:list,palgad:list):
    """Tagastame järjend või teksti
    :rtype var: tulemus
    """
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene.upper()==nimi.upper():
            n=inimesed.cocunt(nimi)
            print("Inemene on olemas, selline nimi kohtume",n,"korda")
            b=-1
            for i in range(n):
                k=inimesed.index(nimi)
                palk=palgad[k]
                b+=K
                t.append(nimi+str(palk))
 
    else:
        t="Ei ole nimekotjas"
        return t 