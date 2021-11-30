def add_person ():
	"""inimese ja palga lisamine
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("TextFile1.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("TextFile2.txt", "a") as palgad:
		palgad.write(palga+"\n")
def delete_person ():
	"""Isiku ja palga eemaldamine,Удаление человека и зарплаты 
	"""
	f=open("TextFile1.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed:
		print("Kas sa tahad lisama nimi ja palgad/?")
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
		a=inimesed.index(nimi)
		inimesed.pop(a)
		palgad.pop(a)
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
def keskmine():
	"""Kasmise palka leidmine. Kui ta on loetelus, siis näitame kes saab seda kätte
	:rtype var:
	"""
    summa=0
    for palga in p:
        summa+=palga
	kesk=summa/len(p)
	print(kesk)
	vahe=0
	if 0<=p.index(kesk)<len(p)-1:
		kesk=i[p.index(kesk)]
		return kesk
	else:
		kesk="Puudunud"
		return kesk
def suurim_palk(i,p):
	suurim=max(p)
	b=p.index(suurim)
	kellel=i[b]
	print(suurim)
	print(kellel)
	return suurim,kellel