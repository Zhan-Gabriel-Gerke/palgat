from module1 import *
p=loe_failist_listisse("TextFile2.txt")
i=loe_failist_listisse("TextFile1.txt")
while True:
	a=input("Funktsioonid: Add users-1\n delete users-2\n keskmine-3\n suurim palk-4")
	if a=="1":
		add_person ()
	elif a=="2":
		delete_person()
	elif a=="3":
		 keskmine()
	elif a=="4":
		suurim_palk(i,p)
	else:
		break