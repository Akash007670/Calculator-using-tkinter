from tkinter import *

root =Tk()
root.title("Calculator")
root.configure(background="#333333")

e = Entry(root,width = 41,borderwidth=5)
e.grid(row = 0,column=0,columnspan=7,padx = 20,pady=10)

def button_click(number):
	current = e.get()
	e.delete(0,END) 
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)
	return

def button_equal():
	second_number = e.get()
	e.delete(0,END)

	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	if math == "percentage":
		e.insert(0, f_num % int(second_number))

def button_mul():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0,END)
	return

def button_sub():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0,END)
	return

def button_div():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0,END)
	return

def button_perc():
	first_number = e.get()
	global f_num
	global math
	math = "percentage"
	f_num = int(first_number)
	e.delete(0,END)
	return


button_1 = Button(root,text="1",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(1))
button_2 = Button(root,text="2",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(2))
button_3 = Button(root,text="3",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(3))
button_4 = Button(root,text="4",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(4))
button_5 = Button(root,text="5",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(5))
button_6 = Button(root,text="6",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(6))
button_7 = Button(root,text="7",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(7))
button_8 = Button(root,text="8",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(8))
button_9 = Button(root,text="9",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(9))
button_0 = Button(root,text="0",padx = 30,pady = 20,fg='white',bg='#262626',command = lambda: button_click(0))
button_10 = Button(root,text="+/-",padx = 24,pady = 20,fg='white',bg='#262626',command = lambda: button_click())
button_11 = Button(root,text=".",padx = 32,pady = 20,fg='white',bg='#262626',command = lambda: button_deci())

button_Mul = Button(root,text="*",padx = 30,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_mul())
button_Sub = Button(root,text="-",padx = 30,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_sub())
button_Add = Button(root,text="+",padx = 28,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_add())
button_Equ = Button(root,text="=",padx = 28,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_equal())

button_Perc = Button(root,text="%",padx = 28,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_perc())
button_Sq = Button(root,text="sq",padx = 27,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_click())
button_Ce = Button(root,text="Ce",padx = 27,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_clear())
button_Div = Button(root,text="/",padx = 30,pady = 20,fg='white',bg='#4d4d4d',command = lambda: button_div())

#put the buttomns on the screen
button_1.grid(row= 4,column = 1)
button_2.grid(row= 4,column = 2)
button_3.grid(row= 4,column = 3)
button_Add.grid(row=4,column = 4)

button_4.grid(row= 3,column = 1)
button_5.grid(row= 3,column = 2)
button_6.grid(row= 3,column = 3)
button_Sub.grid(row=3,column = 4)

button_7.grid(row= 2,column = 1)
button_8.grid(row= 2,column = 2)
button_9.grid(row= 2,column = 3)
button_Mul.grid(row=2,column = 4)

button_10.grid(row= 5,column = 1)
button_0.grid(row= 5,column = 2)
button_11.grid(row= 5,column = 3)
button_Equ.grid(row =5,column = 4)

button_Perc.grid(row= 1,column =1 )
button_Sq.grid(row= 1,column = 2)
button_Ce.grid(row= 1,column = 3)
button_Div.grid(row= 1,column = 4)

root.mainloop()
