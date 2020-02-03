
from Tkinter import Tk, Frame, Label, Button, Checkbutton, IntVar, StringVar, BooleanVar
import ttk
import tkMessageBox
from sys import platform
from PIL import ImageTk, Image
from random import sample 

global v,y, eksen, step, boxs
global lenght
coordinat = [[5,4], [5,3], [5,2], [5,1]]
lenght = 3
v, y = 5,1
eksen, step = "yatay", "+"
boxs = {}
run = 0
def start(event):
	global run
	run =1
	event.widget.place_forget()
	strew()
	master.after(100, timer)
	
def goSecondPage():
	firstPage.pack_forget()
	
def strew():
	global sv, sy
	sv, sy = sample(range(11), 2)
	boxs[sv][sy].configure(bg="red")
	
	
def timer():
	
	global v,y,eksen,step
	global sv, sy
	global lenght
	global run
	
	if eksen == "dikey" and step == "+": v = v + 1
	if eksen == "dikey" and step == "-": v = v - 1
	if eksen == "yatay" and step == "-": y = y - 1
	if eksen == "yatay" and step == "+": y = y + 1
	
	if v is -1: 
		print "game over!"
		run = 0
		return 0
	if v >= 11: 
		print "game over!"
		run = 0
		return 0
	if y < 0: 
		print "game over!"
		run = 0
		return 0
	if y >= 11: 
		print "game over!"
		run = 0
		return 0
		
	coordinat.insert(0, [v,y])
		
	for v, y in reversed(coordinat[0:lenght+1]):
		boxs[v][y].configure(bg="white")
	
	for v, y in reversed(coordinat[0:lenght]):
		boxs[v][y].configure(bg="blue")
		
	xx,yy = coordinat[0:lenght][0]
	boxs[xx][yy].configure(bg="blue")
		
	if [sv, sy] == coordinat[0:lenght][0]:
		lenght = lenght + 1
		[sv,sy] = [-1,-1]
		strew()
	
	if run is 1:
		master.after(200, timer)

def keyboard(e):
	global eksen, step
	print e.keysym.upper()
	keyBoard = {"W":keyUp, "S":keyDown, "A":keyLeft, "D":keyRight}
	for key, value in keyBoard.items(): 
		if key == e.keysym.upper():
			value.configure(bg="gray", fg="black", bd=0)
		else:
			value.configure(bg="white", fg="black", bd=0)
			
	if e.keysym.upper() == "W": 
		eksen = "dikey"
		step = "-"
	if e.keysym.upper() == "S":
		eksen = "dikey"
		step = "+"
		
	if e.keysym.upper() == "A": 
		eksen = "yatay"
		step = "-"
	if e.keysym.upper() == "D": 
		eksen = "yatay"
		step = "+"
		
'''grid_forget->show'''
	
master = Tk()
master.geometry("500x300")
master.title("snake game!")
master.resizable(width="false", height="false")


main = Frame(master)
main.pack(fill="both")

main.bind_all("<Key>", keyboard)

firstPage = Frame(main, bg="white", borderwidth = 20)
firstPage.pack(fill="both")

f1 = Frame(firstPage, bg="white", pady=15)
f1.pack() 

for horizontal in range(0,4):
	f2 = Frame(f1, bg="white", width=25, height=25)
	f2.pack(fill="both", pady=1, padx=5)
	for vertical in range(0,12):
		Frame(f2, bg="gray", width=25, height=25).pack(side="left", padx=1)
firstPageStartBtn = Button(firstPage, text="start a game", bg="red", fg="white", command=goSecondPage)
firstPageStartBtn.pack(pady=45, anchor = "center")


secondPage = Frame(main)
secondPage.pack(fill="both", side="left")

secondPageLeft = Frame(secondPage)
secondPageLeft.pack(fill="both", side="left")

secondPageRight = Frame(secondPage, padx=15, pady=15)
secondPageRight.pack(fill="both", side="right")

f3 = Frame(secondPageLeft, bg="gray", pady=0)
f3.pack() 
for vertical in range(11):
	f4 = Frame(f3, bg="gray", width=25, height=25)
	f4.pack(fill="both", pady=1, padx=0)
	boxs.update({vertical:[]})
	for horizontal in range(11):
		h = Frame(f4, bg="white", width=25, height=25)
		h.pack(side="left", padx=1)
		boxs[vertical].append(h) 
		
image = ImageTk.PhotoImage(file="start.png")
btnPlay = Button(secondPageLeft, text="Play", padx=15, image=image)
btnPlay.place(x = 120, y = 90)
btnPlay.bind('<Button-1>', start)

f5 = Frame(secondPageRight, padx=15)
f5.pack(fill="both") 

lb1 = Label(f5, text="Score :", fg="gray", font="Vertical 15")
lb1.pack(fill="both", side="left")

lb2 = Label(f5, text="100", fg="gray", font="Vertical 15")
lb2.pack(fill="both", side="right")

f6 = Frame(secondPageRight, padx=15, borderwidth=20)
f6.pack(fill="both", side="bottom")

WKey = ImageTk.PhotoImage(file="W.png")
AKey = ImageTk.PhotoImage(file="A.png")
SKey = ImageTk.PhotoImage(file="S.png")
DKey = ImageTk.PhotoImage(file="D.png")

keyUp = Button(f6, width=30, height=30, text="up", bg="white", fg="black", bd=0, image=WKey)
keyUp.grid(row=0, column=2)

keyLeft = Button(f6, width=30, height=30, text="left", bg="white", fg="black", bd=0, image=AKey)
keyLeft.grid(row=1, column=1)

keyDown = Button(f6, width=30, height=30, text="down", bg="yellow", fg="black", bd=0, image=SKey)
keyDown.grid(row=1, column=2)

keyRight = Button(f6, width=30, height=30, text="right", bg="white", fg="black", bd=0, image=DKey)
keyRight.grid(row=1, column=3)

'''https://www.tutorialspoint.com/python/python_gui_programming.htm'''
'''
https://www.flaticon.com/free-icon/volume-off-indicator_60750
https://www.iconfinder.com/icons/342974/arrow_keyboard_keys_icon'''

master.mainloop()

'''
for horizontal in range(3):
	f2 = Frame(f1, bg="white", width=25, height=25)
	f2.pack(fill="both", pady=1, padx=5)
	for vertical in range(11):
		if horizontal is 0 and vertical in [0,1,2,3,4,5,6,7,8,9]:
			Frame(f2, bg="black", width=25, height=25).pack(side="left", padx=1)
		elif horizontal is 0 and vertical in [10]:
			Frame(f2, bg="red", width=25, height=25).pack(side="left", padx=1)
		elif horizontal is 1 and vertical in [0]:
			Frame(f2, bg="black", width=25, height=25).pack(side="left", padx=1)
		elif horizontal is 1 and vertical in [1,2,3,4,5,6,7,8,9,10]:
			Frame(f2, bg="blue", width=25, height=25).pack(side="left", padx=1)
		elif horizontal is 2 and vertical in [0,1,2,3,4]:
			Frame(f2, bg="black", width=25, height=25).pack(side="left", padx=1)
		elif horizontal is 2 and vertical in [5,6,7,8,9,10]:
			Frame(f2, bg="blue", width=25, height=25).pack(side="left", padx=1)
'''
