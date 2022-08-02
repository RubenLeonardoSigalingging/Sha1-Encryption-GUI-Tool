#!/usr/bin/env python3


import hashlib
import os
import sys
if sys.platform=="win32" or sys.platform=="win64":
	os.system("cls")
	os.system("pip install tk")
	os.system("pip install pyfiglet")
	os.system("pip install pycryptodome")
	os.system("cls")
elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
	os.system("clear")
	os.system("pip install tk")
	os.system("pip install pyfiglet")
	os.system("pip install pycryptodome")
	os.system("clear")
import tkinter
from tkinter import *
import pyfiglet
import Crypto.Hash


def SHA1_Hash_Generator(Created_By="Ruben Leonardo Sigalingging"):
	Main_Functions_Of_SHA1_Hash_Generator=tkinter.Tk()
	Main_Functions_Of_SHA1_Hash_Generator.title("SHA1 Hash Generator Tool")
	Main_Functions_Of_SHA1_Hash_Generator.configure(bg="#000000",cursor="crosshair")
	Main_Functions_Of_SHA1_Hash_Generator.geometry("800x500")
	Main_Functions_Of_SHA1_Hash_Generator.resizable(width=False,height=True)


	Title_Label_SHA1_Hash_Generator=tkinter.Label(Main_Functions_Of_SHA1_Hash_Generator,text="SHA1 Hash Generator",font=("Ubuntu",35),bg="#008b8b",fg="#ffffff",anchor=tkinter.CENTER,justify=tkinter.CENTER,cursor="pirate")
	Title_Label_SHA1_Hash_Generator.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP)


	SHA1_Hash_Generator_Entry_Button=Entry(Main_Functions_Of_SHA1_Hash_Generator,bg="#ffffff",fg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",23),highlightcolor="#a9a9a9",justify=tkinter.CENTER,relief=tkinter.FLAT,selectbackground="#008b8b",selectforeground="#006400",width=25)
	SHA1_Hash_Generator_Entry_Button.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=25,pady=25)


	def Processor_Function(Created_By="Ruben Leonardo Sigalingging"):
		Get_Function=SHA1_Hash_Generator_Entry_Button.get()
		from Crypto.Hash import SHA1
		SHA1_Hash=SHA1.new()
		SHA1_Hash.update(Get_Function.encode("ascii"))
		Result_Label=tkinter.Label(Main_Functions_Of_SHA1_Hash_Generator,anchor=tkinter.CENTER,bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",23),fg="#ffffff",justify=tkinter.CENTER,relief=tkinter.FLAT)
		Result_Label.configure(text="Sha1 Encrypted:\n"+str(SHA1_Hash.hexdigest()))
		Result_Label.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=25,pady=25)
		print(f"Sha1 Encrypter Result:\n{SHA1_Hash.hexdigest()}")


	Processor_Button=Button(Main_Functions_Of_SHA1_Hash_Generator,text="Let's Encrypt!",activebackground="#008b8b",activeforeground="#ffffff",bd=2,bg="#ffffff",fg="#008b8b",font=("Times New Roman",18),height=1,highlightcolor="#a9a9a9",justify=tkinter.CENTER,relief=tkinter.RAISED,cursor="pirate",command=Processor_Function)
	Processor_Button.pack(expand=False,fill=tkinter.X,side=tkinter.TOP,padx=25,pady=25)
	Main_Functions_Of_SHA1_Hash_Generator.mainloop()
SHA1_Hash_Generator()