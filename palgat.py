from module1 import *
from tkinter import*
from math import *
global a,b,c
global p,i
global nimi
global zp
p=loe_failist_listisse("palgad.txt")
i=loe_failist_listisse("Name.txt")
root=Tk()
root.title("zatsonaja")
root.geometry("1200x600")
But1=Button(root,text="add",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:add())
But2=Button(root,text="delete",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:delete())
But3=Button(root,text="keskmine",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:keskmine())
But4=Button(root,text="suurim",font="Arial 15",relief="flat",width=10,height=3,bg="#fb00ff",command=lambda:suurim(i,p))
But1.pack(side=LEFT)
But2.pack(side=LEFT)
But3.pack(side=LEFT)
But4.pack(side=LEFT)
root.mainloop()
