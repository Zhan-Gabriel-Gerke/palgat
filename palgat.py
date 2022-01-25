from module1 import *
from tkinter import*
from math import *
global a,b,c
global nimi
global zp
p=loe_failist_listisse("Palka.txt")
i=loe_failist_listisse("Name.txt")
root=Tk()
root.title("zatsonaja")
root.geometry("1200x600")
But1=Button(root,text="add",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:add())
But2=Button(root,text="delete",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:delete())
But3=Button(root,text="keskmine",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:keskmine(i,p))
But4=Button(root,text="suurim",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:suurim(i,p))
But1.pack(side=LEFT)
But2.pack(side=LEFT)
But3.pack(side=LEFT)
But4.pack(side=LEFT)
root.mainloop()
#while True:
#	a=input("Funktsioonid: Add users-1\n delete users-2\n keskmine-3\n suurim palk-4,")
#	if a=="1":
#		add()
#	elif a=="2":
#		delete()
#	elif a=="3":
#		 keskmine(i,p)
#		 print(kesk)
#	elif a=="4":
#		suurim(i,p)
#		print(suurim)
#	else:
#		break 
