global kesk
global suurim
def lists()->list:
	""" tegi listid failist
	"""
	palgad=[]
	with open("Palgad.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("Name.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palgad,inimesed
def add():
	"""see funktsioon lisab loendisse isiku nime ja palga
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("Name.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("Palka.txt", "a") as palgad:
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
	if nimi not in inimesed: 
		print("Kas sa tahad lisada nime ja palga/?")
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
		a=inimesed.index(nimi)
		inimesed.pop(a)
		palgad.pop(a)
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
def keskmine():
    """
    Программа проверяет списки и выводит на экран среднюю зарплату
    rtype var:int
    """
    sum=0
    for palgad in p:
        sum+=palk
    keskm=sum/len(p)
    print(keskm)
    v=0
    if 0<p.index(keskm)<len(p)-1:
        kesk=i(p.index(keskm))
        return keskm
    else:
        print("Нет средней зарплаты")
        return keskm
def suurim(i:list,p:list):
	"""
	:rtype: str,str:
	"""
	palgad,inimesed=lists()
	suurim=max(palgad)
	b=palgad.index(suurim) 
	print("kõike suured palga on "+inimesed[b]+" palga")
