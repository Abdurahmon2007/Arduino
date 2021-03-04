# my_string = "Odiljanov Abduraxmon"
# print(my_string[0:7:2])
from tkinter import *

def TugmaBosildi():
	soz.configure(text = "Assalomu aleykum !")

Dastur = Tk()

soz = Label(text = "Salom")
soz.pack()

tugma = Button(text = "Ok", command = TugmaBosildi)

tugma.pack()

Dastur.mainloop()