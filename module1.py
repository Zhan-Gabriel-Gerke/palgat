def add():
	"""see funktsioon lisab loendisse isiku nime ja palga
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("Name.txt", "a") as inimesed:# Lisa inimene faili lõppu  lisame nimi failisse
		inimesed.write(nimi+"\n")	
	with open("Palka.txt", "a") as palgad:# Lisame palk faili lõppu
		palgad.write(palga+"\n")
def delete():
	"""see funktsioon eemaldab nimekirjast isiku ja tema palga 
	"""
	f=open("Name.txt", "r")
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
		with open("Palka.txt", "r") as f1:
			for stro in f1:
				palgad.append(stro.strip())
		a=inimesed.index(nimi)#kui nimi on olemas, siis leidke indeks
		inimesed.pop(a)#eemalda nimi
		palgad.pop(a)#
	f=open("Name.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("Palka.txt", "w")
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
        summa+=int(palga)
    kesk=summa/len(p)
    print(kesk)
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
#Почему 4 и 5 не работает я сам не понимаю я 4 и 5 списал с доски но почему-то они не робят