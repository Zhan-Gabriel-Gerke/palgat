from module1 import *
p=loe_failist_listisse("TextFile2.txt")
i=loe_failist_listisse("TextFile1.txt")
while True:
	a=input("Funktsioonid: Add users-1\n delete users-2\n keskmine-3\n suurim palk-4, min palk-5")
	if a=="1":
		add_person ()
	elif a=="2":
		delete_person()
	elif a=="3":
		 bbb=keskmine(i,p)
		 print(bbb)
	elif a=="4":
		aaa=suurim(i,p)
		print(aaa)
	elif a=="5":
		smallest_salary(a,b)
	else:
		break