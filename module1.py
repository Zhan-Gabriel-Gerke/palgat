def add():
	"""see funktsioon lisab loendisse isiku nime ja palga
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("TextFile1.txt", "a") as inimesed:# Lisa inimene faili lõppu  lisame nimi failisse
		inimesed.write(nimi+"\n")	
	with open("TextFile2.txt", "a") as palgad:# Lisame palk faili lõppu
		palgad.write(palga+"\n")
def delete():
	"""see funktsioon eemaldab nimekirjast isiku ja tema palga 
	"""
	f=open("TextFile1.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed: #kontrollitakse, kas on olemas selline inimene
		print("Kas sa tahad lisada nime ja palga/?")#kui inimene ei leitud registreeri oma
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person()
		else:
			pass
	else:
		palgad=[]
		with open("TextFile2.txt", "r") as f1:
			for stro in f1:
				palgad.append(stro.strip())
		a=inimesed.index(nimi)#kui nimi on olemas, siis leidke indeks
		inimesed.pop(a)#eemalda nimi
		palgad.pop(a)#
	f=open("TextFile1.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("TextFile2.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_
def keskmine(i:list,p:list):
    """Keskmise palka leidmine. Kui ta on loetelus, siis näiame kes saab seda kätte
    :rtype var:
    """
    summa=0
    for palga in p:
        summa+=p
    kesk=summa/len(p)
    print(kesk)
    vahe=0
    if 0<=p.index(kesk)<len(p)-1:
        kesk=i[p.index(kesk)]
        return kesk
    else:
        kesk="Puudunud"
        return kesk
def suurim(i:list,p:list):
    """
    :rtype: str,str:
    """
    suurim=max(p)
    b=p.index(suurim)
    kellel=i[b]
    return suurim , kellel
#Почему 3 и 4 не работает я сам не понимаю я 3 и 4 списал с доски но почему-то они не робят