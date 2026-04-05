from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.title("LOGIN PAGE")
root.geometry("600x500")
root.configure(background="YELLOW")
conn=sqlite3.connect("COLLEGE.db")
c=conn.cursor()
global listname

def BACK():
	root=Toplevel()
	root.title("LOGIN PAGE")
	root.geometry("600x500")
	root.configure(background="YELLOW")
	conn=sqlite3.connect("COLLEGE.db")
	c=conn.cursor()
	global listname

	def student_login():
		root.withdraw()
		win1=Toplevel()
		win1.configure(background="YELLOW")
		win1.title("STUDENT LOGIN")
		win1.geometry("600x500")
		global username1
		global password1
		username1=StringVar()
		password1=StringVar()
		global row,listname,listdate,listLR,listLB,listdepart
		
		def backstudent_login():
			win1.withdraw()
			BACK()
		
		def STUDENT_LEAVE():
			win1.withdraw()
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			c.execute("SELECT NAME,BRANCH FROM register WHERE USERNAME=? AND PASSWORD=?",(username1.get(),password1.get()))
			row=c.fetchone()
			print(row[0],row[1])
			
			def LEAVE_APP():
				LB=10
				conn=sqlite3.connect("LEAVE.db")
				c=conn.cursor()
				c.execute("INSERT INTO leave_details(NAME,BRANCH,USERNAME,PASSWORD,LEAVE_REASON,DATE,LEAVE_BALANCE) VALUES(?,?,?,?,?,?,?)",(row[0],row[1],username1.get(),password1.get(),var2.get(),ee1.get(),LB))
				conn.commit()
				messagebox.showinfo("SUCCESS","REQUEST SENT SUCCESSFULLY!!")
			
			def STUDENT_LEAVE_EMPTY():
				if(var2.get()=="" or ee1.get()==""):
					return 1
			
			def apply1():
				global listname,listdate,listLR,listLB,listdepart
				if(STUDENT_LEAVE_EMPTY()==1):
					messagebox.showinfo("Oops!","INFORMATION MISSING!!!")
				else:
					LEAVE_APP()
					
			def principal_message():
				name=row[0]
				print(row[0])
				names12=[]
				conn12=sqlite3.connect("LEAVE_ACESS.db")
				c12=conn12.cursor()
				c12.execute("SELECT NAME FROM leave_ac")
				names12=c12.fetchone()
				
				def check12():
					if not names12:
						return 0
					else:
						return 1
												
				if(check12() == 1):
					c12.execute("SELECT PERMISSION FROM leave_ac WHERE NAME=name")
					message=c12.fetchone()
					if(message[0]):
						if(message[0] == "Y"):
							ee2.config(text="YOUR REQUEST HAS BEEN GRANTED!!")
						else:
							ee2.config(text="NO,YOUR REQUEST HAS BEEN REJECTED!!")
					else:
						messagebox.showinfo("SORRY!!","permission not given yet!!")
				else:
					messagebox.showinfo("Oops!","REQUEST NOT FOUND!")
				
				c12.execute('DELETE FROM leave_ac WHERE NAME=?',(name,))
				conn12.commit()
				c12.close()
				
			def student_logout():
				student.withdraw()
				BACK()
			
			student=Toplevel()
			student.configure(background="YELLOW")
			student.title("LEAVE APLICATION--STUDENT")
			student.geometry("600x500")
			var2=StringVar(student)
			le1=Label(student,text="NAME:",bg="YELLOW",fg="RED")
			le1.place(x=30,y=20)
			le2=Label(student,text=row[0].capitalize(),bg="YELLOW")
			le2.place(x=140,y=20)
			le3=Label(student,text="DEPARTMENT:",bg="YELLOW",fg="RED")
			le3.place(x=30,y=70)
			le4=Label(student,text=row[1],bg="YELLOW")
			le4.place(x=140,y=70)
			le5=Label(student,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
			le5.place(x=20,y=100)
			le6=Label(student,text="LEAVE APPLICATION",bg="YELLOW",fg="RED")
			le6.place(x=250,y=140)
			le6.configure(font="100")
			le7=Label(student,text="LEAVE REASON:",bg="YELLOW",fg="RED")
			le7.place(x=200,y=180)
			var2.set("CASUAL LEAVE")
			op2=OptionMenu(student,var2,"CASUAL LEAVE","PERSONAL WORK","EMERGENCY","SICK LEAVE")
			op2.place(x=300,y=180)
			le8=Label(student,text="DATE:",bg="YELLOW",fg="RED")
			le8.place(x=200,y=230)
			ee1=Entry(student)
			ee1.place(x=300,y=230)
			be1=Button(student,text="APPLY",width=20,command=apply1)
			be1.place(x=250,y=280)
			le9=Label(student,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
			le9.place(x=20,y=320)
			be2=Button(student,text="VIEW PRINCIPAL's MESSAGE",command=principal_message,width=40)
			be2.place(x=160,y=350)
			ee2=Label(student,width=60)
			ee2.place(x=125,y=400)
			be3=Button(student,text="LOGOUT",command=student_logout,width=15)
			be3.place(x=250,y=450)
			student.mainloop()
		
		def REGISTER():
			win1.withdraw()
			register=Toplevel()
			register.configure(background="YELLOW")
			register.title("REGISTERATION")
			register.geometry("600x450")
			var1=StringVar(register)
			v=IntVar()
			x=StringVar()
			y=StringVar()
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
		
			def submit():
				c.execute('INSERT INTO register(NAME,EMAIL,BRANCH,USERNAME,PASSWORD,POST) VALUES(?,?,?,?,?,?)',(er1.get(),er2.get(),var1.get(),er3.get(),er4.get(),str(var1.get())))
				conn.commit()
				messagebox.showinfo("DONE!","RECORDS INSERTED SUCESSFULLY")
				dict={}
				x=er3.get()
				y=er4.get()
				dict.update({str(x):str(y)})
				print(dict)
				br3=Button(register,text="GO BACK TO MAIN PAGE",command=backstudent_login,fg="RED")
				br3.place(x=270,y=400)
		
			def empty():
				if(er1.get()=="" or er2.get()=="" or er3.get()=="" or var1.get()=="" or er4.get()=="" or er1.get()=="" or str(var1.get())==""):
					return 1
		
			def duplicateemail():
				conn=sqlite3.connect("COLLEGE.db")
				c=conn.cursor()
				demail=c.execute('SELECT EMAIL FROM register')
				for i in demail:
					if(i==er2.get()):
						return 1
		
			def dupusername():
				conn=sqlite3.connect("COLLEGE.db")
				c=conn.cursor()
				duser=c.execute('SELECT USERNAME FROM register')
				for i in duser:
					if(i==er3.get()):
						return 1	
		
			def click():
				if(empty()==1):
					messagebox.showinfo("Oops!"," Some of the feilds are empty")
				elif(duplicateemail()==1):
					messagebox.showinfo("Warning!"," Email is been taken")
				elif(dupusername()==1):
					messagebox.showinfo("Warning!"," Username is taken")
				else:
					submit()
				
			br1=Button(register,text="BACK",width=8,height=0,command=backstudent_login)
			br1.place(x=10,y=10)
			lr1=Label(register,text="----REGISTER----",bg="YELLOW",fg="RED")
			lr1.config(font=500)
			lr1.place(x=250,y=10)
			lr2=Label(register,text="NAME:",bg="YELLOW",fg="RED")
			lr2.place(x=190,y=100)
			er1=Entry(register)
			er1.place(x=300,y=100)
			lr3=Label(register,text="Email ID:",bg="YELLOW",fg="RED")
			lr3.place(x=190,y=150)
			er2=Entry(register)
			er2.place(x=300,y=150)
			lr4=Label(register,text="BRANCH:",bg="YELLOW",fg="RED")
			lr4.place(x=190,y=200)
			op1=OptionMenu(register,var1,"COMPUTER","IT","EXTC","MECHANICAL","AUTOMOBILE")
			var1.set("COMPUTER")
			op1.place(x=300,y=200)
			lr5=Label(register,text="USERNAME:",bg="YELLOW",fg="RED")
			lr5.place(x=190,y=250)
			er3=Entry(register,textvariable=x)
			er3.place(x=300,y=250)
			lr6=Label(register,text="PASSWORD:",bg="YELLOW",fg="RED")
			lr6.place(x=190,y=300)
			er4=Entry(register,show="*",textvariable=y)
			er4.place(x=300,y=300)
			lr7=Label(register,text="SELECT ONE:",bg="YELLOW",fg="RED")
			lr7.place(x=190,y=350)
			rr1=Radiobutton(register,variable=v,value=1,text="TEACHER",bg="YELLOW")
			rr1.place(x=300,y=350)
			rr2=Radiobutton(register,variable=v,value=2,text="STUDENT",bg="YELLOW")
			rr2.place(x=390,y=350)
			br2=Button(register,text="REGISTER",width=10,command=click)
			br2.place(x=270,y=400)
			register.mainloop()
			
		def database():
			global conn,c
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			c.execute("SELECT * FROM register WHERE USERNAME=username AND PASSWORD=password")
			conn.commit()
		
		def login1():
			database()
			if (username1.get()=="" or password1.get()==""):
				messagebox.showinfo("Oops!","SOME FIELDS ARE INCOMPLETE!!!")
			else:
				c.execute("SELECT * FROM register WHERE USERNAME= ? AND PASSWORD= ?",(username1.get(),password1.get()))
				if c.fetchone() is not None:
					STUDENT_LEAVE()
					username.delete(0,END)
					password.delete(0,END)
				else:
					messagebox.showinfo("Oops!","INVALID USERNAME OR PASSWORD!!!")
					username.delete(0,END)
					password.delete(0,END)
			c.close()
			conn.close()
					
		bs1=Button(win1,text="BACK",width=8,height=0,command=backstudent_login)
		bs1.place(x=20,y=20)
		canvas1=Canvas(win1,width=180,height=180,bg="YELLOW")
		canvas1.place(x=220,y=40)
		img1=PhotoImage(file="image2.png")
		canvas1.create_image(100,100,image=img1)
		ls1=Label(win1,text="STUDENT  LOGIN",bg="YELLOW",fg="RED")
		ls1.config(font=500)
		ls1.place(x=270,y=230)
		ls2=Label(win1,text="USERNAME:",bg="YELLOW")
		ls2.place(x=200,y=280)
		es1=Entry(win1,textvariable=username1)
		es1.place(x=300,y=280)
		ls3=Label(win1,text="PASSWORD:",bg="YELLOW")
		ls3.place(x=200,y=330)
		es2=Entry(win1,textvariable=password1,show="*")
		es2.place(x=300,y=330)
		bs2=Button(win1,text="LOGIN",command=login1,width=8,height=0)
		bs2.place(x=275,y=380)
		ls4=Label(win1,text="------------ OR -------------",bg="YELLOW")
		ls4.place(x=230,y=420)
		bs3=Button(win1,text="REGISTER",command=REGISTER,width=8,height=0)
		bs3.place(x=275,y=450)
		username=es1.get()
		password=es2.get()
		win1.mainloop()

	def teacher_login():
		root.withdraw()
		win2=Toplevel()
		win2.configure(background="YELLOW")
		win2.title("TEACHER LOGIN")
		win2.geometry("600x500")
		global username2
		global password2
		username2=StringVar()
		password2=StringVar()
		global row1
		
		def backteacher_login():
			win2.withdraw()
			BACK()
		
		
		def TEACHER_LEAVE():
			win2.withdraw()
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			c.execute("SELECT NAME,BRANCH FROM register WHERE USERNAME=? AND PASSWORD=?",(username2.get(),password2.get()))
			row1=c.fetchone()
			print(row1[0],row1[1])
			
			def teacher_logout():
				teacher.withdraw()
				BACK()
		
			
			def LEAVE_APP1():
				conn=sqlite3.connect("LEAVE.db")
				c=conn.cursor()
				c.execute("INSERT INTO leave_details(NAME,BRANCH,USERNAME,PASSWORD,LEAVE_REASON,DATE,LEAVE_BALANCE) VALUES(?,?,?,?,?,?,?)",(row1[0],row1[1],username2.get(),password2.get(),var3.get(),eet1.get(),10))
				conn.commit()
				messagebox.showinfo("SUCCESS","REQUEST SENT SUCCESSFULLY!!")
			
			def TEACHER_LEAVE_EMPTY():
				if(var3.get()=="" or eet1.get()==""):
					return 1
			
			def apply2():
				if(TEACHER_LEAVE_EMPTY()==1):
					messagebox.showinfo("Oops!","INFORMATION MISSING!!!")
				else:
					LEAVE_APP1()
			
			def principal_message1():
				name=row1[0]
				print(row1[0])
				names123=[]
				conn123=sqlite3.connect("LEAVE_ACESS.db")
				c123=conn123.cursor()
				c123.execute("SELECT NAME FROM leave_ac")
				names123=c123.fetchone()
				def check123():
					if not names123:
						return 0
					else:
						return 1
								
				if(check123() == 1):
					
					c123.execute("SELECT PERMISSION FROM leave_ac WHERE NAME=name")
					message=c123.fetchone()
					if(message[0]):
						if(message[0] == "Y"):
							eet2.config(text="YOUR REQUEST HAS BEEN GRANTED!!")
						else:
							eet2.config(text="NO,YOUR REQUEST HAS BEEN REJECTED!!")
					else:
						messagebox.showinfo("SORRY!!","permission not given yet!!")
				else:
					messagebox.showinfo("Oops!","REQUEST NOT FOUND!")
				c123.execute('DELETE FROM leave_ac WHERE NAME=?',((name,)))
				conn123.commit()
				c123.close()
			teacher=Toplevel()
			teacher.configure(background="YELLOW")
			teacher.title("LEAVE APLICATION--TEACHER")
			teacher.geometry("600x550")
			var3=StringVar(teacher)
			let1=Label(teacher,text="NAME:",bg="YELLOW",fg="RED")
			let1.place(x=30,y=20)
			let2=Label(teacher,text=row1[0],bg="YELLOW")
			let2.place(x=140,y=20)
			let3=Label(teacher,text="DEPARTMENT:",bg="YELLOW",fg="RED")
			let3.place(x=30,y=70)
			let4=Label(teacher,text=row1[1],bg="YELLOW")
			let4.place(x=140,y=70)
			let5=Label(teacher,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
			let5.place(x=20,y=100)
			let6=Label(teacher,text="LEAVE APPLICATION",bg="YELLOW",fg="RED")
			let6.place(x=250,y=140)
			let6.configure(font="100")
			let7=Label(teacher,text="LEAVE REASON:",bg="YELLOW",fg="RED")
			let7.place(x=200,y=180)
			var3.set("CASUAL LEAVE")
			op3=OptionMenu(teacher,var3,"CASUAL LEAVE","PERSONAL WORK","EMERGENCY","SICK LEAVE")
			op3.place(x=300,y=180)
			let8=Label(teacher,text="DATE:",bg="YELLOW",fg="RED")
			let8.place(x=200,y=230)
			eet1=Entry(teacher)
			eet1.place(x=300,y=230)
			bet1=Button(teacher,text="APPLY",width=20,command=apply2)
			bet1.place(x=250,y=280)
			let9=Label(teacher,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
			let9.place(x=20,y=320)
			bet2=Button(teacher,text="VIEW PRINCIPAL's MESSAGE",width=40,command=principal_message1)
			bet2.place(x=160,y=350)
			eet2=Label(teacher,width=60)
			eet2.place(x=125,y=400)
			bet3=Button(teacher,text="LOGOUT",command=teacher_logout,width=15)
			bet3.place(x=250,y=450)
			teacher.mainloop()

		def REGISTER():
			win2.withdraw()
			register=Toplevel()
			register.configure(background="YELLOW")
			register.title("REGISTERATION")
			register.geometry("600x450")
			var1=StringVar(register)
			v=IntVar()
			x=StringVar()
			y=StringVar()
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
		
			def submit():
				c.execute('INSERT INTO register(NAME,EMAIL,BRANCH,USERNAME,PASSWORD,POST) VALUES(?,?,?,?,?,?)',(er1.get(),er2.get(),var1.get(),er3.get(),er4.get(),str(var1.get())))
				conn.commit()
				messagebox.showinfo("DONE!","RECORDS INSERTED SUCESSFULLY")
				dict={}
				x=er3.get()
				y=er4.get()
				dict.update({str(x):str(y)})
				print(dict)
				br3=Button(register,text="GO BACK TO MAIN PAGE",command=teacher_login,fg="RED")
				br3.place(x=270,y=400)
		
			def empty():
				if(er1.get()=="" or er2.get()=="" or er3.get()=="" or var1.get()=="" or er4.get()=="" or er1.get()=="" or str(var1.get())==""):
					return 1
		
			def duplicateemail():
				conn=sqlite3.connect("COLLEGE.db")
				c=conn.cursor()
				demail=c.execute('SELECT EMAIL FROM register')
				for i in demail:
					if(i==er2.get()):
						return 1
		
			def dupusername():
				conn=sqlite3.connect("COLLEGE.db")
				c=conn.cursor()
				duser=c.execute('SELECT USERNAME FROM register')
				for i in duser:
					if(i==er3.get()):
						return 1	
		
			def click():
				if(empty()==1):
					messagebox.showinfo("Oops!"," Some of the feilds are empty")
				elif(duplicateemail()==1):
					messagebox.showinfo("Warning!"," Email is been taken")
				elif(dupusername()==1):
					messagebox.showinfo("Warning!"," Username is taken")
				else:
					submit()
		
			br1=Button(register,text="BACK",width=8,height=0,command=backteacher_login)
			br1.place(x=10,y=10)
			lr1=Label(register,text="----REGISTER----",bg="YELLOW",fg="RED")
			lr1.config(font=500)
			lr1.place(x=250,y=10)
			lr2=Label(register,text="NAME:",bg="YELLOW",fg="RED")
			lr2.place(x=190,y=100)
			er1=Entry(register)
			er1.place(x=300,y=100)
			lr3=Label(register,text="Email ID:",bg="YELLOW",fg="RED")
			lr3.place(x=190,y=150)
			er2=Entry(register)
			er2.place(x=300,y=150)
			lr4=Label(register,text="BRANCH:",bg="YELLOW",fg="RED")
			lr4.place(x=190,y=200)
			op1=OptionMenu(register,var1,"COMPUTER","IT","EXTC","MECHANICAL","AUTOMOBILE")
			var1.set("COMPUTER")
			op1.place(x=300,y=200)
			lr5=Label(register,text="USERNAME:",bg="YELLOW",fg="RED")
			lr5.place(x=190,y=250)
			er3=Entry(register,textvariable=x)
			er3.place(x=300,y=250)
			lr6=Label(register,text="PASSWORD:",bg="YELLOW",fg="RED")
			lr6.place(x=190,y=300)
			er4=Entry(register,show="*",textvariable=y)
			er4.place(x=300,y=300)
			lr7=Label(register,text="SELECT ONE:",bg="YELLOW",fg="RED")
			lr7.place(x=190,y=350)
			rr1=Radiobutton(register,variable=v,value=1,text="TEACHER",bg="YELLOW")
			rr1.place(x=300,y=350)
			rr2=Radiobutton(register,variable=v,value=2,text="STUDENT",bg="YELLOW")
			rr2.place(x=390,y=350)
			br2=Button(register,text="REGISTER",width=10,command=click)
			br2.place(x=270,y=400)
			register.mainloop()
		
		def database1():
			global conn,c
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			c.execute("SELECT * FROM register WHERE USERNAME=username AND PASSWORD=password")
			conn.commit()
		
		def login2():
			database1()
			if (username2.get()=="" or password2.get()==""):
				messagebox.showinfo("Oops!","SOME FIELDS ARE INCOMPLETE!!!")
			else:
				c.execute("SELECT * FROM register WHERE USERNAME= ? AND PASSWORD= ?",(username2.get(),password2.get()))
				if c.fetchone() is not None:
					TEACHER_LEAVE()
					username.delete(0,END)
					password.delete(0,END)
				else:
					messagebox.showinfo("Oops!","INVALID USERNAME OR PASSWORD!!!")
					username.delete(0,END)
					password.delete(0,END)
			c.close()
			conn.close()
		
		bt1=Button(win2,text="BACK",width=8,height=0,command=backteacher_login)
		bt1.place(x=20,y=20)
		canvas2=Canvas(win2,width=180,height=180,bg="YELLOW")
		canvas2.place(x=220,y=40)
		img2=PhotoImage(file="image2.png")
		canvas2.create_image(100,100,image=img2)
		lt1=Label(win2,text="TEACHER  LOGIN",bg="YELLOW",fg="RED")
		lt1.config(font=500)
		lt1.place(x=270,y=230)
		lt2=Label(win2,text="USERNAME:",bg="YELLOW")
		lt2.place(x=200,y=280)
		et1=Entry(win2,textvariable=username2)
		et1.place(x=300,y=280)
		lt3=Label(win2,text="PASSWORD:",bg="YELLOW")
		lt3.place(x=200,y=330)
		et1=Entry(win2,textvariable=password2,show="*")
		et1.place(x=300,y=330)
		bt2=Button(win2,text="LOGIN",command=login2,width=8,height=0)
		bt2.place(x=275,y=380)
		lt4=Label(win2,text="------------ OR -------------",bg="YELLOW")
		lt4.place(x=230,y=420)
		bt3=Button(win2,text="REGISTER",command=REGISTER,width=8,height=0)
		bt3.place(x=275,y=450)
		win2.mainloop()
		
	def principal_login():
		root.withdraw()
		win3=Toplevel()
		win3.configure(background="YELLOW")
		win3.title("PRINCIPAL LOGIN")
		win3.geometry("600x450")
		global admin_user
		global admin_pass
		global list
		admin_user=StringVar()
		admin_pass=StringVar()
		
		def backprincipal_login():
			win3.withdraw()
			BACK()
		
		def DETAILS():
			det=Toplevel()
			det.title("APPLICANT's DETAILS")
			det.geometry("400x400")
			det.configure(background="YELLOW")
			item=listname.curselection()
			name=listname.get(item)
			#LB=listLB.get(item)
			#LB=LB-1
			conn=sqlite3.connect("LEAVE.db")
			c=conn.cursor()
			name1=c.execute('SELECT NAME,BRANCH,LEAVE_REASON,DATE,LEAVE_BALANCE FROM leave_details WHERE NAME=name')
			conn.commit()
			row2=name1.fetchone()
			for i in row2:
				print(i)
				
			ld1=Label(det,text="NAME:",bg="YELLOW",fg="RED")
			ld1.place(x=20,y=20)
			ld2=Label(det,text=row2[0],fg="RED")
			ld2.place(x=150,y=20)
			ld3=Label(det,text="DEPARTMENT:",bg="YELLOW",fg="RED")
			ld3.place(x=20,y=70)
			ld4=Label(det,text=row2[1],fg="RED")
			ld4.place(x=150,y=70)
			ld5=Label(det,text=" DATE :",bg="YELLOW",fg="RED")
			ld5.place(x=20,y=120)
			ld6=Label(det,text=row2[3],fg="RED")
			ld6.place(x=150,y=120)
			ld7=Label(det,text="LEAVE BALANCE:",bg="YELLOW",fg="RED")
			ld7.place(x=20,y=170)
			ld8=Label(det,text=row2[4],fg="RED")
			ld8.place(x=150,y=170)
			ld9=Label(det,text="LEAVE REASON:",bg="YELLOW",fg="RED")
			ld9.place(x=20,y=220)
			ld10=Label(det,text=row2[2],fg="RED")
			ld10.place(x=150,y=220)
			bd1=Button(det,text="CLOSE",fg="RED",width=15,command=det.destroy)
			bd1.place(x=120,y=270)
			c.close()
			
			det.mainloop()

		
		def checkdet():
			if listname.curselection():
				DETAILS()
			else:
				messagebox.showinfo("Oops!","PLEASE SELECT THE NAME.")
			
		def principal_main():
			win3.withdraw()
			hod=Toplevel()
			hod.title("LEAVE APLLICATION BY PRINCIPAL")
			hod.configure(background="YELLOW")
			hod.geometry("700x500")
			global listname
			conn=sqlite3.connect("LEAVE.db")
			c=conn.cursor()
			c1=conn.cursor()
			c2=conn.cursor()
			c3=conn.cursor()
			c4=conn.cursor()
			row=c.execute("SELECT NAME FROM leave_details")
			#row=c.fetchone()
			row1=c1.execute("SELECT BRANCH FROM leave_details")
			#row1=c.fetchone()
			row2=c2.execute("SELECT LEAVE_REASON FROM leave_details")
			#row2=c.fetchone()
			row3=c3.execute("SELECT LEAVE_BALANCE FROM leave_details")
			#row3=c.fetchone()
			row4=c4.execute("SELECT DATE FROM leave_details")
			#row4=c.fetchone()
			
			def reply():
				item=listname.curselection()
				name1=listname.get(item)
				LB1=listLB.get(item)
				depart1=listdepart.get(item)
				LR1=listLR.get(item)
				date1=listdate.get(item)
				permission1=vara1.get()
				#LB=LB-1
				list1=[]
				list1.append(name1)
				list1.append(LB1)
				list1.append(depart1)
				list1.append(LR1)
				list1.append(date1)
				list1.append(permission1)
				list2=[i[0] for i in list1]
				print(list2)
				
				conn=sqlite3.connect("LEAVE_ACESS.db")
				c=conn.cursor()
				c.execute('INSERT INTO leave_ac(NAME,BRANCH,LEAVE_REASON,LEAVE_BALANCE,DATE,PERMISSION) VALUES(?,?,?,?,?,?)',(list2[0],list2[1],list2[2],list2[3],list2[4],list2[5]))
				conn.commit()
				c.close()
				conn1=sqlite3.connect("LEAVE.db")
				c1=conn1.cursor()
				c1.execute('DELETE FROM leave_details WHERE NAME=name')
				conn1.commit()
				c1.close()
				listname.delete(item)
				listdepart.delete(item)
				listLR.delete(item)
				listLB.delete(item)
				listdate.delete(item)
				
			def checkreply():
				if listname.curselection():
					reply()
				else:
					messagebox.showinfo("Oops!","PLEASE SELECT THE NAME.")
			
			def principal_logout():
				hod.withdraw()
				BACK()
		
			
			vara1=StringVar()
			lm1=Label(hod,text="PRINCIPAL",bg="YELLOW",fg="RED")
			lm1.place(x=300,y=20)
			lm1.configure(font="200")
			lm2=Label(hod,text="LEAVE APPLICATIONS:",fg="RED",bg="YELLOW")
			lm2.place(x=50,y=50)
			ld1=Label(hod,text="NAME.",bg="YELLOW",fg="RED")
			ld1.place(x=50,y=70)
			listname=Listbox(hod,width=20,selectmode=SINGLE)
			listname.place(x=50,y=90)
			ld2=Label(hod,text="DEPARTMENT.",bg="YELLOW",fg="RED")
			ld2.place(x=170,y=70)
			listdepart=Listbox(hod,width=20,selectmode=SINGLE)
			listdepart.place(x=170,y=90)
			ld3=Label(hod,text="LEAVE REASON.",bg="YELLOW",fg="RED")
			ld3.place(x=290,y=70)
			listLR=Listbox(hod,width=20,selectmode=SINGLE)
			listLR.place(x=290,y=90)
			ld4=Label(hod,text="LEAVE BALANCE.",bg="YELLOW",fg="RED")
			ld4.place(x=410,y=70)
			listLB=Listbox(hod,width=20,selectmode=SINGLE)
			listLB.place(x=410,y=90)
			ld5=Label(hod,text="DATE.",bg="YELLOW",fg="RED")
			ld5.place(x=530,y=70)
			listdate=Listbox(hod,width=20,selectmode=SINGLE)
			listdate.place(x=530,y=90)
			lm3=Label(hod,text="------------------------------------------------------------------------------------------------------------------------------",bg="YELLOW",fg="RED")
			lm3.place(x=30,y=260)
			bm1=Button(hod,text="VIEW DETAILS OF LEAVE APPLICANT",command=checkdet,width=50,fg="RED")
			bm1.place(x=160,y=290)
			lm4=Label(hod,text="------------------------------------------------------------------------------------------------------------------------------",bg="YELLOW",fg="RED")
			lm4.place(x=30,y=320)
			opt1=OptionMenu(hod,vara1,"YOUR LEAVE HAS BEEN GRANTED ","NO,YOUR LEAVE HAS BEEN REJECTED")
			vara1.set("YOUR LEAVE HAS BEEN GRANTED")
			opt1.place(x=250,y=350)
			bm2=Button(hod,text="SEND REPLY",fg="RED",command=checkreply)
			bm2.place(x=320,y=410)
			bm3=Button(hod,text="LOGOUT",command=principal_logout,fg="RED")
			bm3.place(x=600,y=470)
			for i in row:
				listname.insert(END,i)
			for i in row1:
				listdepart.insert(END,i)
			for i in row2:
				listLR.insert(END,i)
			for i in row3:
				listLB.insert(END,i)
			for i in row4:
				listdate.insert(END,i)
			hod.mainloop()
		
		def admin_login():
			x=admin_user.get()
			y=admin_pass.get()
			eh1.delete(0,END)
			eh2.delete(0,END)
			if((x!="admin") and (y!="admin")):
				messagebox.showinfo("Oops!","INVALID USERNAME OR PASSWORD!!!")
			else:
				principal_main()
				
		bh1=Button(win3,text="BACK",width=13,height=0,command=backprincipal_login)
		bh1.place(x=20,y=20)
		canvas3=Canvas(win3,width=180,height=180,bg="YELLOW")
		canvas3.place(x=220,y=40)
		img3=PhotoImage(file="image2.png")
		canvas3.create_image(100,100,image=img3)
		lh1=Label(win3,text="PRINCIPAL",bg="YELLOW",fg="RED")
		lh1.config(font=500)
		lh1.place(x=270,y=230)
		lh2=Label(win3,text="USERNAME:",bg="YELLOW")
		lh2.place(x=200,y=280)
		eh1=Entry(win3,textvariable=admin_user)
		eh1.place(x=300,y=280)
		lh3=Label(win3,text="PASSWORD:",bg="YELLOW")
		lh3.place(x=200,y=330)
		eh2=Entry(win3,show="*",textvariable=admin_pass)
		eh2.place(x=300,y=330)
		bh2=Button(win3,text="LOGIN",command=admin_login,width=8,height=0)
		bh2.place(x=250,y=380)
		win3.mainloop()

	def REGISTER():
		root.withdraw()
		register=Toplevel()
		register.configure(background="YELLOW")
		register.title("REGISTERATION")
		register.geometry("600x450")
		var1=StringVar(register)
		v=IntVar()
		x=StringVar()
		y=StringVar()
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()

		def registerback():
			register.withdraw()
			BACK()
	
		def submit():
			c.execute('INSERT INTO register(NAME,EMAIL,BRANCH,USERNAME,PASSWORD,POST) VALUES(?,?,?,?,?,?)',(er1.get(),er2.get(),var1.get(),er3.get(),er4.get(),str(v.get())))
			conn.commit()
			messagebox.showinfo("DONE!","RECORDS INSERTED SUCESSFULLY")
			br3=Button(register,text="GO BACK TO MAIN PAGE",command=BACK,width=10,fg="RED")
			br3.place(x=270,y=400)

		def empty():
			if(er1.get()=="" or er2.get()=="" or er3.get()=="" or var1.get()=="" or er4.get()=="" or er1.get()=="" or str(var1.get())==""):
				return 1

		def duplicateemail():
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			demail=c.execute('SELECT EMAIL FROM register')
			for i in demail:
				if(i==er2.get()):
					return 1

		def dupusername():
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			duser=c.execute('SELECT USERNAME FROM register')
			for i in duser:
				if(i==er3.get()):
					return 1	

		def click():
			if(empty()==1):
				messagebox.showinfo("Oops!"," Some of the feilds are empty")
			elif(duplicateemail()==1):
				messagebox.showinfo("Warning!"," Email is been taken")
			elif(dupusername()==1):
				messagebox.showinfo("Warning!"," Username is taken")
			else:
				submit()
				br2=Button(register,text="GO BACK TO MAIN PAGE",command=registerback)
				br2.place(x=270,y=400)
		
		br1=Button(register,text="BACK",width=8,height=0,command=registerback)
		br1.place(x=10,y=10)
		lr1=Label(register,text="----REGISTER----",bg="YELLOW",fg="RED")
		lr1.config(font=500)
		lr1.place(x=250,y=10)
		lr2=Label(register,text="NAME:",bg="YELLOW",fg="RED")
		lr2.place(x=190,y=100)
		er1=Entry(register)
		er1.place(x=300,y=100)
		lr3=Label(register,text="Email ID:",bg="YELLOW",fg="RED")
		lr3.place(x=190,y=150)
		er2=Entry(register)
		er2.place(x=300,y=150)
		lr4=Label(register,text="BRANCH:",bg="YELLOW",fg="RED")
		lr4.place(x=190,y=200)
		op1=OptionMenu(register,var1,"COMPUTER","IT","EXTC","MECHANICAL","AUTOMOBILE")
		var1.set("COMPUTER")
		op1.place(x=300,y=200)
		lr5=Label(register,text="USERNAME:",bg="YELLOW",fg="RED")
		lr5.place(x=190,y=250)
		er3=Entry(register,textvariable=x)
		er3.place(x=300,y=250)
		lr6=Label(register,text="PASSWORD:",bg="YELLOW",fg="RED")
		lr6.place(x=190,y=300)
		er4=Entry(register,show="*",textvariable=y)
		er4.place(x=300,y=300)
		lr7=Label(register,text="SELECT ONE:",bg="YELLOW",fg="RED")
		lr7.place(x=190,y=350)
		rr1=Radiobutton(register,variable=v,value=1,text="TEACHER",bg="YELLOW")
		rr1.place(x=300,y=350)
		rr2=Radiobutton(register,variable=v,value=2,text="STUDENT",bg="YELLOW")
		rr2.place(x=390,y=350)
		br2=Button(register,text="REGISTER",width=10,command=click)
		br2.place(x=270,y=400)
		register.mainloop()

	canvas12=Canvas(root,width=300,height=300,bg="YELLOW")
	canvas12.place(x=50,y=80)
	img12=PhotoImage(file="image1.png")
	canvas12.create_image(150,150,image=img12)
	b1=Button(root,text="STUDENT",command=student_login,width=20)
	b1.place(x=400,y=50)
	b2=Button(root,text="TEACHER",command=teacher_login,width=20)
	b2.place(x=400,y=150)
	b3=Button(root,text="PRINCIPAL",command=principal_login,width=20)
	b3.place(x=400,y=250)
	b4=Button(root,text="register",command=REGISTER,width=20)
	b4.place(x=400,y=400)
	b5=Button(root,text="CLOSE",command=root.destroy,width=10)
	b5.place(x=230,y=460)
	root.mainloop()

def student_login():
	root.withdraw()
	win1=Toplevel()
	win1.configure(background="YELLOW")
	win1.title("STUDENT LOGIN")
	win1.geometry("600x500")
	global username1
	global password1
	username1=StringVar()
	password1=StringVar()
	global row,listname,listdate,listLR,listLB,listdepart
	
	def backstudent_login():
		win1.withdraw()
		BACK()
	
	def STUDENT_LEAVE():
		win1.withdraw()
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
		c.execute("SELECT NAME,BRANCH FROM register WHERE USERNAME=? AND PASSWORD=?",(username1.get(),password1.get()))
		row=c.fetchone()
		print(row[0],row[1])
		
		def LEAVE_APP():
			LB=10
			conn=sqlite3.connect("LEAVE.db")
			c=conn.cursor()
			c.execute("INSERT INTO leave_details(NAME,BRANCH,USERNAME,PASSWORD,LEAVE_REASON,DATE,LEAVE_BALANCE) VALUES(?,?,?,?,?,?,?)",(row[0],row[1],username1.get(),password1.get(),var2.get(),ee1.get(),LB))
			conn.commit()
			messagebox.showinfo("SUCCESS","REQUEST SENT SUCCESSFULLY!!")
		
		def STUDENT_LEAVE_EMPTY():
			if(var2.get()=="" or ee1.get()==""):
				return 1
		
		def apply1():
			global listname,listdate,listLR,listLB,listdepart
			if(STUDENT_LEAVE_EMPTY()==1):
				messagebox.showinfo("Oops!","INFORMATION MISSING!!!")
			else:
				LEAVE_APP()
				
		def principal_message():
			name=row[0]
			print(row[0])
			names12=[]
			conn12=sqlite3.connect("LEAVE_ACESS.db")
			c12=conn12.cursor()
			c12.execute("SELECT NAME FROM leave_ac")
			names12=c12.fetchone()
			
			def check12():
				if not names12:
					return 0
				else:
					return 1
			if(check12() == 1):
				c12.execute("SELECT PERMISSION FROM leave_ac WHERE NAME=name")
				message=c1.fetchone()
				if(message[0]):
					if(message[0] == "Y"):
						ee2.config(text="YOUR REQUEST HAS BEEN GRANTED!!")
					else:
						ee2.config(text="NO,YOUR REQUEST HAS BEEN REJECTED!!")
				else:
					messagebox.showinfo("SORRY!!","permission not given yet!!")
			else:
				messagebox.showinfo("Oops!","REQUEST NOT FOUND!")
			c12.execute('DELETE FROM leave_ac WHERE NAME=?',((name,)))
			conn12.commit()
			c12.close()
				
		def student_logout():
			student.withdraw()
			BACK()
		
		student=Toplevel()
		student.configure(background="YELLOW")
		student.title("LEAVE APLICATION--STUDENT")
		student.geometry("600x500")
		var2=StringVar(student)
		le1=Label(student,text="NAME:",bg="YELLOW",fg="RED")
		le1.place(x=30,y=20)
		le2=Label(student,text=row[0].capitalize(),bg="YELLOW")
		le2.place(x=140,y=20)
		le3=Label(student,text="DEPARTMENT:",bg="YELLOW",fg="RED")
		le3.place(x=30,y=70)
		le4=Label(student,text=row[1],bg="YELLOW")
		le4.place(x=140,y=70)
		le5=Label(student,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
		le5.place(x=20,y=100)
		le6=Label(student,text="LEAVE APPLICATION",bg="YELLOW",fg="RED")
		le6.place(x=250,y=140)
		le6.configure(font="100")
		le7=Label(student,text="LEAVE REASON:",bg="YELLOW",fg="RED")
		le7.place(x=200,y=180)
		var2.set("CASUAL LEAVE")
		op2=OptionMenu(student,var2,"CASUAL LEAVE","PERSONAL WORK","EMERGENCY","SICK LEAVE")
		op2.place(x=300,y=180)
		le8=Label(student,text="DATE:",bg="YELLOW",fg="RED")
		le8.place(x=200,y=230)
		ee1=Entry(student)
		ee1.place(x=300,y=230)
		be1=Button(student,text="APPLY",width=20,command=apply1)
		be1.place(x=250,y=280)
		le9=Label(student,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
		le9.place(x=20,y=320)
		be2=Button(student,text="VIEW PRINCIPAL's MESSAGE",command=principal_message,width=40)
		be2.place(x=160,y=350)
		ee2=Label(student,width=60)
		ee2.place(x=125,y=400)
		be3=Button(student,text="LOGOUT",command=student_logout,width=15)
		be3.place(x=250,y=450)
		student.mainloop()
	
	def REGISTER():
		win1.withdraw()
		register=Toplevel()
		register.configure(background="YELLOW")
		register.title("REGISTERATION")
		register.geometry("600x450")
		var1=StringVar(register)
		v=IntVar()
		x=StringVar()
		y=StringVar()
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
	
		def backstudent_loginregister():
			register.withdraw()
			student_login()

		def submit():
			c.execute('INSERT INTO register(NAME,EMAIL,BRANCH,USERNAME,PASSWORD,POST) VALUES(?,?,?,?,?,?)',(er1.get(),er2.get(),var1.get(),er3.get(),er4.get(),str(var1.get())))
			conn.commit()
			messagebox.showinfo("DONE!","RECORDS INSERTED SUCESSFULLY")
			dict={}
			x=er3.get()
			y=er4.get()
			dict.update({str(x):str(y)})
			print(dict)
			br3=Button(register,text="GO BACK TO MAIN PAGE",command=backstudent_login,fg="RED")
			br3.place(x=270,y=400)
	
		def empty():
			if(er1.get()=="" or er2.get()=="" or er3.get()=="" or var1.get()=="" or er4.get()=="" or er1.get()=="" or str(var1.get())==""):
				return 1
	
		def duplicateemail():
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			demail=c.execute('SELECT EMAIL FROM register')
			for i in demail:
				if(i==er2.get()):
					return 1
	
		def dupusername():
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			duser=c.execute('SELECT USERNAME FROM register')
			for i in duser:
				if(i==er3.get()):
					return 1	
	
		def click():
			if(empty()==1):
				messagebox.showinfo("Oops!"," Some of the feilds are empty")
			elif(duplicateemail()==1):
				messagebox.showinfo("Warning!"," Email is been taken")
			elif(dupusername()==1):
				messagebox.showinfo("Warning!"," Username is taken")
			else:
				submit()
			
		br1=Button(register,text="BACK",width=8,height=0,command=backstudent_loginregister)
		br1.place(x=10,y=10)
		lr1=Label(register,text="----REGISTER----",bg="YELLOW",fg="RED")
		lr1.config(font=500)
		lr1.place(x=250,y=10)
		lr2=Label(register,text="NAME:",bg="YELLOW",fg="RED")
		lr2.place(x=190,y=100)
		er1=Entry(register)
		er1.place(x=300,y=100)
		lr3=Label(register,text="Email ID:",bg="YELLOW",fg="RED")
		lr3.place(x=190,y=150)
		er2=Entry(register)
		er2.place(x=300,y=150)
		lr4=Label(register,text="BRANCH:",bg="YELLOW",fg="RED")
		lr4.place(x=190,y=200)
		op1=OptionMenu(register,var1,"COMPUTER","IT","EXTC","MECHANICAL","AUTOMOBILE")
		var1.set("COMPUTER")
		op1.place(x=300,y=200)
		lr5=Label(register,text="USERNAME:",bg="YELLOW",fg="RED")
		lr5.place(x=190,y=250)
		er3=Entry(register,textvariable=x)
		er3.place(x=300,y=250)
		lr6=Label(register,text="PASSWORD:",bg="YELLOW",fg="RED")
		lr6.place(x=190,y=300)
		er4=Entry(register,show="*",textvariable=y)
		er4.place(x=300,y=300)
		lr7=Label(register,text="SELECT ONE:",bg="YELLOW",fg="RED")
		lr7.place(x=190,y=350)
		rr1=Radiobutton(register,variable=v,value=1,text="TEACHER",bg="YELLOW")
		rr1.place(x=300,y=350)
		rr2=Radiobutton(register,variable=v,value=2,text="STUDENT",bg="YELLOW")
		rr2.place(x=390,y=350)
		br2=Button(register,text="REGISTER",width=10,command=click)
		br2.place(x=270,y=400)
		register.mainloop()
		
	def database():
		global conn,c
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
		c.execute("SELECT * FROM register WHERE USERNAME=username AND PASSWORD=password")
		conn.commit()
	
	def login1():
		database()
		if (username1.get()=="" or password1.get()==""):
			messagebox.showinfo("Oops!","SOME FIELDS ARE INCOMPLETE!!!")
		else:
			c.execute("SELECT * FROM register WHERE USERNAME= ? AND PASSWORD= ?",(username1.get(),password1.get()))
			if c.fetchone() is not None:
				STUDENT_LEAVE()
				username.delete(0,END)
				password.delete(0,END)
			else:
				messagebox.showinfo("Oops!","INVALID USERNAME OR PASSWORD!!!")
				username.delete(0,END)
				password.delete(0,END)
		c.close()
		conn.close()

	bs1=Button(win1,text="BACK",width=8,height=0,command=backstudent_login)
	bs1.place(x=20,y=20)
	canvas1=Canvas(win1,width=180,height=180,bg="YELLOW")
	canvas1.place(x=220,y=40)
	img1=PhotoImage(file="image2.png")
	canvas1.create_image(100,100,image=img1)
	ls1=Label(win1,text="STUDENT  LOGIN",bg="YELLOW",fg="RED")
	ls1.config(font=500)
	ls1.place(x=270,y=230)
	ls2=Label(win1,text="USERNAME:",bg="YELLOW")
	ls2.place(x=200,y=280)
	es1=Entry(win1,textvariable=username1)
	es1.place(x=300,y=280)
	ls3=Label(win1,text="PASSWORD:",bg="YELLOW")
	ls3.place(x=200,y=330)
	es2=Entry(win1,textvariable=password1,show="*")
	es2.place(x=300,y=330)
	bs2=Button(win1,text="LOGIN",command=login1,width=8,height=0)
	bs2.place(x=275,y=380)
	ls4=Label(win1,text="------------ OR -------------",bg="YELLOW")
	ls4.place(x=230,y=420)
	bs3=Button(win1,text="REGISTER",command=REGISTER,width=8,height=0)
	bs3.place(x=275,y=450)
	username=es1.get()
	password=es2.get()
	win1.mainloop()

def teacher_login():
	root.withdraw()
	win2=Toplevel()
	win2.configure(background="YELLOW")
	win2.title("TEACHER LOGIN")
	win2.geometry("600x500")
	global username2
	global password2
	username2=StringVar()
	password2=StringVar()
	global row1
	
	def backteacher_login():
		win2.withdraw()
		BACK()
	
	
	def TEACHER_LEAVE():
		win2.withdraw()
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
		c.execute("SELECT NAME,BRANCH FROM register WHERE USERNAME=? AND PASSWORD=?",(username2.get(),password2.get()))
		row1=c.fetchone()
		print(row1[0],row1[1])
		
		def teacher_logout():
			teacher.withdraw()
			BACK()
		
		def LEAVE_APP1():
			conn=sqlite3.connect("LEAVE.db")
			c=conn.cursor()
			c.execute("INSERT INTO leave_details(NAME,BRANCH,USERNAME,PASSWORD,LEAVE_REASON,DATE,LEAVE_BALANCE) VALUES(?,?,?,?,?,?,?)",(row1[0],row1[1],username2.get(),password2.get(),var3.get(),eet1.get(),10))
			conn.commit()
			messagebox.showinfo("SUCCESS","REQUEST SENT SUCCESSFULLY!!")
		
		def TEACHER_LEAVE_EMPTY():
			if(var3.get()=="" or eet1.get()==""):
				return 1
		
		def apply2():
			if(TEACHER_LEAVE_EMPTY()==1):
				messagebox.showinfo("Oops!","INFORMATION MISSING!!!")
			else:
				LEAVE_APP1()
		
		def principal_message1():
			name=row1[0]
			print(row1[0])
			names123=[]
			conn123=sqlite3.connect("LEAVE_ACESS.db")
			c123=conn123.cursor()
			c123.execute("SELECT NAME FROM leave_ac")
			names123=c123.fetchone()
			def check123():
				if not names123:
					return 0
				else:
					return 1
						
			if(check123() == 1):
				c123.execute("SELECT PERMISSION FROM leave_ac WHERE NAME=name")
				message=c123.fetchone()
				if(message[0]):
					if(message[0] == "Y"):
						eet2.config(text="YOUR REQUEST HAS BEEN GRANTED!!")
					else:
						eet2.config(text="NO,YOUR REQUEST HAS BEEN REJECTED!!")
				else:
					messagebox.showinfo("SORRY!!","permission not given yet!!")
			else:
				messagebox.showinfo("Oops!","REQUEST NOT FOUND!")
			c123.execute('DELETE FROM leave_ac WHERE NAME=?',((name,)))
			conn123.commit()
			c123.close()
		teacher=Toplevel()
		teacher.configure(background="YELLOW")
		teacher.title("LEAVE APLICATION--TEACHER")
		teacher.geometry("600x550")
		var3=StringVar(teacher)
		let1=Label(teacher,text="NAME:",bg="YELLOW",fg="RED")
		let1.place(x=30,y=20)
		let2=Label(teacher,text=row1[0],bg="YELLOW")
		let2.place(x=140,y=20)
		let3=Label(teacher,text="DEPARTMENT:",bg="YELLOW",fg="RED")
		let3.place(x=30,y=70)
		let4=Label(teacher,text=row1[1],bg="YELLOW")
		let4.place(x=140,y=70)
		let5=Label(teacher,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
		let5.place(x=20,y=100)
		let6=Label(teacher,text="LEAVE APPLICATION",bg="YELLOW",fg="RED")
		let6.place(x=250,y=140)
		let6.configure(font="100")
		let7=Label(teacher,text="LEAVE REASON:",bg="YELLOW",fg="RED")
		let7.place(x=200,y=180)
		var3.set("CASUAL LEAVE")
		op3=OptionMenu(teacher,var3,"CASUAL LEAVE","PERSONAL WORK","EMERGENCY","SICK LEAVE")
		op3.place(x=300,y=180)
		let8=Label(teacher,text="DATE:",bg="YELLOW",fg="RED")
		let8.place(x=200,y=230)
		eet1=Entry(teacher)
		eet1.place(x=300,y=230)
		bet1=Button(teacher,text="APPLY",width=20,command=apply2)
		bet1.place(x=250,y=280)
		let9=Label(teacher,text="----------------------------------------------------------------------------------------------------------------",fg="RED",bg="yellow")
		let9.place(x=20,y=320)
		bet2=Button(teacher,text="VIEW PRINCIPAL's MESSAGE",width=40,command=principal_message1)
		bet2.place(x=160,y=350)
		eet2=Label(teacher,width=60)
		eet2.place(x=125,y=400)
		bet3=Button(teacher,text="LOGOUT",command=teacher_logout,width=15)
		bet3.place(x=250,y=450)
		teacher.mainloop()

	def REGISTER():
		win2.withdraw()
		register=Toplevel()
		register.configure(background="YELLOW")
		register.title("REGISTERATION")
		register.geometry("600x450")
		var1=StringVar(register)
		v=IntVar()
		x=StringVar()
		y=StringVar()
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
	
		def backteacher_loginregister():
			register.withdraw()
			teacher_login()
	
		def submit():
			c.execute('INSERT INTO register(NAME,EMAIL,BRANCH,USERNAME,PASSWORD,POST) VALUES(?,?,?,?,?,?)',(er1.get(),er2.get(),var1.get(),er3.get(),er4.get(),str(var1.get())))
			conn.commit()
			messagebox.showinfo("DONE!","RECORDS INSERTED SUCESSFULLY")
			dict={}
			x=er3.get()
			y=er4.get()
			dict.update({str(x):str(y)})
			print(dict)
			br3=Button(register,text="GO BACK TO MAIN PAGE",command=teacher_login,fg="RED")
			br3.place(x=270,y=400)
	
		def empty():
			if(er1.get()=="" or er2.get()=="" or er3.get()=="" or var1.get()=="" or er4.get()=="" or er1.get()=="" or str(var1.get())==""):
				return 1
	
		def duplicateemail():
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			demail=c.execute('SELECT EMAIL FROM register')
			for i in demail:
				if(i==er2.get()):
					return 1
	
		def dupusername():
			conn=sqlite3.connect("COLLEGE.db")
			c=conn.cursor()
			duser=c.execute('SELECT USERNAME FROM register')
			for i in duser:
				if(i==er3.get()):
					return 1	
	
		def click():
			if(empty()==1):
				messagebox.showinfo("Oops!"," Some of the feilds are empty")
			elif(duplicateemail()==1):
				messagebox.showinfo("Warning!"," Email is been taken")
			elif(dupusername()==1):
				messagebox.showinfo("Warning!"," Username is taken")
			else:
				submit()
	
		br1=Button(register,text="BACK",width=8,height=0,command=backteacher_loginregister)
		br1.place(x=10,y=10)
		lr1=Label(register,text="----REGISTER----",bg="YELLOW",fg="RED")
		lr1.config(font=500)
		lr1.place(x=250,y=10)
		lr2=Label(register,text="NAME:",bg="YELLOW",fg="RED")
		lr2.place(x=190,y=100)
		er1=Entry(register)
		er1.place(x=300,y=100)
		lr3=Label(register,text="Email ID:",bg="YELLOW",fg="RED")
		lr3.place(x=190,y=150)
		er2=Entry(register)
		er2.place(x=300,y=150)
		lr4=Label(register,text="BRANCH:",bg="YELLOW",fg="RED")
		lr4.place(x=190,y=200)
		op1=OptionMenu(register,var1,"COMPUTER","IT","EXTC","MECHANICAL","AUTOMOBILE")
		var1.set("COMPUTER")
		op1.place(x=300,y=200)
		lr5=Label(register,text="USERNAME:",bg="YELLOW",fg="RED")
		lr5.place(x=190,y=250)
		er3=Entry(register,textvariable=x)
		er3.place(x=300,y=250)
		lr6=Label(register,text="PASSWORD:",bg="YELLOW",fg="RED")
		lr6.place(x=190,y=300)
		er4=Entry(register,show="*",textvariable=y)
		er4.place(x=300,y=300)
		lr7=Label(register,text="SELECT ONE:",bg="YELLOW",fg="RED")
		lr7.place(x=190,y=350)
		rr1=Radiobutton(register,variable=v,value=1,text="TEACHER",bg="YELLOW")
		rr1.place(x=300,y=350)
		rr2=Radiobutton(register,variable=v,value=2,text="STUDENT",bg="YELLOW")
		rr2.place(x=390,y=350)
		br2=Button(register,text="REGISTER",width=10,command=click)
		br2.place(x=270,y=400)
		register.mainloop()
	
	def database1():
		global conn,c
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
		c.execute("SELECT * FROM register WHERE USERNAME=username AND PASSWORD=password")
		conn.commit()
	
	def login2():
		database1()
		if (username2.get()=="" or password2.get()==""):
			messagebox.showinfo("Oops!","SOME FIELDS ARE INCOMPLETE!!!")
		else:
			c.execute("SELECT * FROM register WHERE USERNAME= ? AND PASSWORD= ?",(username2.get(),password2.get()))
			if c.fetchone() is not None:
				TEACHER_LEAVE()
				username.delete(0,END)
				password.delete(0,END)
			else:
				messagebox.showinfo("Oops!","INVALID USERNAME OR PASSWORD!!!")
				username.delete(0,END)
				password.delete(0,END)
		c.close()
		conn.close()
	
	bt1=Button(win2,text="BACK",width=8,height=0,command=backteacher_login)
	bt1.place(x=20,y=20)
	canvas2=Canvas(win2,width=180,height=180,bg="YELLOW")
	canvas2.place(x=220,y=40)
	img2=PhotoImage(file="image2.png")
	canvas2.create_image(100,100,image=img2)
	lt1=Label(win2,text="TEACHER  LOGIN",bg="YELLOW",fg="RED")
	lt1.config(font=500)
	lt1.place(x=270,y=230)
	lt2=Label(win2,text="USERNAME:",bg="YELLOW")
	lt2.place(x=200,y=280)
	et1=Entry(win2,textvariable=username2)
	et1.place(x=300,y=280)
	lt3=Label(win2,text="PASSWORD:",bg="YELLOW")
	lt3.place(x=200,y=330)
	et1=Entry(win2,textvariable=password2,show="*")
	et1.place(x=300,y=330)
	bt2=Button(win2,text="LOGIN",command=login2,width=8,height=0)
	bt2.place(x=275,y=380)
	lt4=Label(win2,text="------------ OR -------------",bg="YELLOW")
	lt4.place(x=230,y=420)
	bt3=Button(win2,text="REGISTER",command=REGISTER,width=8,height=0)
	bt3.place(x=275,y=450)
	win2.mainloop()
	
def principal_login():
	root.withdraw()
	win3=Toplevel()
	win3.configure(background="YELLOW")
	win3.title("PRINCIPAL LOGIN")
	win3.geometry("600x450")
	global admin_user
	global admin_pass
	global list
	admin_user=StringVar()
	admin_pass=StringVar()
	
	def backprincipal_login():
		win3.withdraw()
		BACK()
	
	def DETAILS():
		det=Toplevel()
		det.title("APPLICANT's DETAILS")
		det.geometry("400x400")
		det.configure(background="YELLOW")
		item=listname.curselection()
		name=listname.get(item)
		#LB=listLB.get(item)
		#LB=LB-1
		conn=sqlite3.connect("LEAVE.db")
		c=conn.cursor()
		name1=c.execute('SELECT NAME,BRANCH,LEAVE_REASON,DATE,LEAVE_BALANCE FROM leave_details WHERE NAME=?',(name))
		conn.commit()
		row2=name1.fetchone()
		for i in row2:
			print(i)
			
		ld1=Label(det,text="NAME:",bg="YELLOW",fg="RED")
		ld1.place(x=20,y=20)
		ld2=Label(det,text=row2[0],fg="RED")
		ld2.place(x=150,y=20)
		ld3=Label(det,text="DEPARTMENT:",bg="YELLOW",fg="RED")
		ld3.place(x=20,y=70)
		ld4=Label(det,text=row2[1],fg="RED")
		ld4.place(x=150,y=70)
		ld5=Label(det,text=" DATE :",bg="YELLOW",fg="RED")
		ld5.place(x=20,y=120)
		ld6=Label(det,text=row2[3],fg="RED")
		ld6.place(x=150,y=120)
		ld7=Label(det,text="LEAVE BALANCE:",bg="YELLOW",fg="RED")
		ld7.place(x=20,y=170)
		ld8=Label(det,text=row2[4],fg="RED")
		ld8.place(x=150,y=170)
		ld9=Label(det,text="LEAVE REASON:",bg="YELLOW",fg="RED")
		ld9.place(x=20,y=220)
		ld10=Label(det,text=row2[2],fg="RED")
		ld10.place(x=150,y=220)
		bd1=Button(det,text="CLOSE",fg="RED",width=15,command=det.destroy)
		bd1.place(x=120,y=270)
		c.close()
		
		det.mainloop()

	
	def checkdet():
		if listname.curselection():
			DETAILS()
		else:
			messagebox.showinfo("Oops!","PLEASE SELECT THE NAME.")
		
	def principal_main():
		win3.withdraw()
		hod=Toplevel()
		hod.title("LEAVE APLLICATION BY PRINCIPAL")
		hod.configure(background="YELLOW")
		hod.geometry("700x500")
		global listname
		conn=sqlite3.connect("LEAVE.db")
		c=conn.cursor()
		c1=conn.cursor()
		c2=conn.cursor()
		c3=conn.cursor()
		c4=conn.cursor()
		row=c.execute("SELECT NAME FROM leave_details")
		#row=c.fetchone()
		row1=c1.execute("SELECT BRANCH FROM leave_details")
		#row1=c.fetchone()
		row2=c2.execute("SELECT LEAVE_REASON FROM leave_details")
		#row2=c.fetchone()
		row3=c3.execute("SELECT LEAVE_BALANCE FROM leave_details")
		#row3=c.fetchone()
		row4=c4.execute("SELECT DATE FROM leave_details")
		#row4=c.fetchone()
		
		def reply():
			item=listname.curselection()
			name1=listname.get(item)
			LB1=listLB.get(item)
			depart1=listdepart.get(item)
			LR1=listLR.get(item)
			date1=listdate.get(item)
			permission1=vara1.get()
			#LB=LB-1
			list1=[]
			list1.append(name1)
			list1.append(LB1)
			list1.append(depart1)
			list1.append(LR1)
			list1.append(date1)
			list1.append(permission1)
			list2=[i[0] for i in list1]
			print(list2)
			
			conn=sqlite3.connect("LEAVE_ACESS.db")
			c=conn.cursor()
			c.execute('INSERT INTO leave_ac(NAME,BRANCH,LEAVE_REASON,LEAVE_BALANCE,DATE,PERMISSION) VALUES(?,?,?,?,?,?)',(list2[0],list2[1],list2[2],list2[3],list2[4],list2[5]))
			c.close()
			conn1=sqlite3.connect("LEAVE.db")
			c1=conn1.cursor()
			c1.execute('DELETE FROM leave_details WHERE NAME=(?)',(name1))
			conn1.commit()
			c1.close()
			listname.delete(item)
			listdepart.delete(item)
			listLR.delete(item)
			listLB.delete(item)
			listdate.delete(item)
			
		def checkreply():
			if listname.curselection():
				reply()
			else:
				messagebox.showinfo("Oops!","PLEASE SELECT THE NAME.")
		
		def principal_logout():
			hod.withdraw()
			BACK()
		
		vara1=StringVar()
		lm1=Label(hod,text="PRINCIPAL",bg="YELLOW",fg="RED")
		lm1.place(x=300,y=20)
		lm1.configure(font="200")
		lm2=Label(hod,text="LEAVE APPLICATIONS:",fg="RED",bg="YELLOW")
		lm2.place(x=50,y=50)
		ld1=Label(hod,text="NAME.",bg="YELLOW",fg="RED")
		ld1.place(x=50,y=70)
		listname=Listbox(hod,width=20,selectmode=SINGLE)
		listname.place(x=50,y=90)
		ld2=Label(hod,text="DEPARTMENT.",bg="YELLOW",fg="RED")
		ld2.place(x=170,y=70)
		listdepart=Listbox(hod,width=20,selectmode=SINGLE)
		listdepart.place(x=170,y=90)
		ld3=Label(hod,text="LEAVE REASON.",bg="YELLOW",fg="RED")
		ld3.place(x=290,y=70)
		listLR=Listbox(hod,width=20,selectmode=SINGLE)
		listLR.place(x=290,y=90)
		ld4=Label(hod,text="LEAVE BALANCE.",bg="YELLOW",fg="RED")
		ld4.place(x=410,y=70)
		listLB=Listbox(hod,width=20,selectmode=SINGLE)
		listLB.place(x=410,y=90)
		ld5=Label(hod,text="DATE.",bg="YELLOW",fg="RED")
		ld5.place(x=530,y=70)
		listdate=Listbox(hod,width=20,selectmode=SINGLE)
		listdate.place(x=530,y=90)
		lm3=Label(hod,text="------------------------------------------------------------------------------------------------------------------------------",bg="YELLOW",fg="RED")
		lm3.place(x=30,y=260)
		bm1=Button(hod,text="VIEW DETAILS OF LEAVE APPLICANT",command=checkdet,width=50,fg="RED")
		bm1.place(x=160,y=290)
		lm4=Label(hod,text="------------------------------------------------------------------------------------------------------------------------------",bg="YELLOW",fg="RED")
		lm4.place(x=30,y=320)
		opt1=OptionMenu(hod,vara1,"YOUR LEAVE HAS BEEN GRANTED ","NO,YOUR LEAVE HAS BEEN REJECTED")
		vara1.set("YOUR LEAVE HAS BEEN GRANTED")
		opt1.place(x=250,y=350)
		bm2=Button(hod,text="SEND REPLY",fg="RED",command=checkreply)
		bm2.place(x=320,y=410)
		bm3=Button(hod,text="LOGOUT",command=principal_logout,fg="RED")
		bm3.place(x=600,y=470)
		for i in row:
			listname.insert(END,i)
		for i in row1:
			listdepart.insert(END,i)
		for i in row2:
			listLR.insert(END,i)
		for i in row3:
			listLB.insert(END,i)
		for i in row4:
			listdate.insert(END,i)
		hod.mainloop()
	
	def admin_login():
		x=admin_user.get()
		y=admin_pass.get()
		eh1.delete(0,END)
		eh2.delete(0,END)
		if((x!="admin") and (y!="admin")):
			messagebox.showinfo("Oops!","INVALID USERNAME OR PASSWORD!!!")
		else:
			principal_main()
			
	bh1=Button(win3,text="BACK",width=13,height=0,command=backprincipal_login)
	bh1.place(x=20,y=20)
	canvas3=Canvas(win3,width=180,height=180,bg="YELLOW")
	canvas3.place(x=220,y=40)
	img3=PhotoImage(file="image2.png")
	canvas3.create_image(100,100,image=img3)
	lh1=Label(win3,text="PRINCIPAL",bg="YELLOW",fg="RED")
	lh1.config(font=500)
	lh1.place(x=270,y=230)
	lh2=Label(win3,text="USERNAME:",bg="YELLOW")
	lh2.place(x=200,y=280)
	eh1=Entry(win3,textvariable=admin_user)
	eh1.place(x=300,y=280)
	lh3=Label(win3,text="PASSWORD:",bg="YELLOW")
	lh3.place(x=200,y=330)
	eh2=Entry(win3,show="*",textvariable=admin_pass)
	eh2.place(x=300,y=330)
	bh2=Button(win3,text="LOGIN",command=admin_login,width=8,height=0)
	bh2.place(x=250,y=380)
	win3.mainloop()

def REGISTER():
	root.withdraw()
	register=Toplevel()
	register.configure(background="YELLOW")
	register.title("REGISTERATION")
	register.geometry("600x450")
	var1=StringVar(register)
	v=IntVar()
	x=StringVar()
	y=StringVar()
	conn=sqlite3.connect("COLLEGE.db")
	c=conn.cursor()

	def registerback():
		register.withdraw()
		BACK()
	
	def submit():
		c.execute('INSERT INTO register(NAME,EMAIL,BRANCH,USERNAME,PASSWORD,POST) VALUES(?,?,?,?,?,?)',(er1.get(),er2.get(),var1.get(),er3.get(),er4.get(),str(v.get())))
		conn.commit()
		messagebox.showinfo("DONE!","RECORDS INSERTED SUCESSFULLY")
		br3=Button(register,text="GO BACK TO MAIN PAGE",command=BACK,width=10,fg="RED")
		br3.place(x=270,y=400)

	def empty():
		if(er1.get()=="" or er2.get()=="" or er3.get()=="" or var1.get()=="" or er4.get()=="" or er1.get()=="" or str(var1.get())==""):
			return 1

	def duplicateemail():
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
		demail=c.execute('SELECT EMAIL FROM register')
		for i in demail:
			if(i==er2.get()):
				return 1

	def dupusername():
		conn=sqlite3.connect("COLLEGE.db")
		c=conn.cursor()
		duser=c.execute('SELECT USERNAME FROM register')
		for i in duser:
			if(i==er3.get()):
				return 1	

	def click():
		if(empty()==1):
			messagebox.showinfo("Oops!"," Some of the feilds are empty")
		elif(duplicateemail()==1):
			messagebox.showinfo("Warning!"," Email is been taken")
		elif(dupusername()==1):
			messagebox.showinfo("Warning!"," Username is taken")
		else:
			submit()
			br2=Button(register,text="GO BACK TO MAIN PAGE",command=registerback)
			br2.place(x=270,y=400)
	
	br1=Button(register,text="BACK",width=8,height=0,command=registerback)
	br1.place(x=10,y=10)
	lr1=Label(register,text="----REGISTER----",bg="YELLOW",fg="RED")
	lr1.config(font=500)
	lr1.place(x=250,y=10)
	lr2=Label(register,text="NAME:",bg="YELLOW",fg="RED")
	lr2.place(x=190,y=100)
	er1=Entry(register)
	er1.place(x=300,y=100)
	lr3=Label(register,text="Email ID:",bg="YELLOW",fg="RED")
	lr3.place(x=190,y=150)
	er2=Entry(register)
	er2.place(x=300,y=150)
	lr4=Label(register,text="BRANCH:",bg="YELLOW",fg="RED")
	lr4.place(x=190,y=200)
	op1=OptionMenu(register,var1,"COMPUTER","IT","EXTC","MECHANICAL","AUTOMOBILE")
	var1.set("COMPUTER")
	op1.place(x=300,y=200)
	lr5=Label(register,text="USERNAME:",bg="YELLOW",fg="RED")
	lr5.place(x=190,y=250)
	er3=Entry(register,textvariable=x)
	er3.place(x=300,y=250)
	lr6=Label(register,text="PASSWORD:",bg="YELLOW",fg="RED")
	lr6.place(x=190,y=300)
	er4=Entry(register,show="*",textvariable=y)
	er4.place(x=300,y=300)
	lr7=Label(register,text="SELECT ONE:",bg="YELLOW",fg="RED")
	lr7.place(x=190,y=350)
	rr1=Radiobutton(register,variable=v,value=1,text="TEACHER",bg="YELLOW")
	rr1.place(x=300,y=350)
	rr2=Radiobutton(register,variable=v,value=2,text="STUDENT",bg="YELLOW")
	rr2.place(x=390,y=350)
	br2=Button(register,text="REGISTER",width=10,command=click)
	br2.place(x=270,y=400)
	register.mainloop()

canvas=Canvas(root,width=300,height=300,bg="YELLOW")
canvas.place(x=50,y=80)
img=PhotoImage(file="image1.png")
canvas.create_image(150,150,image=img)
b1=Button(root,text="STUDENT",command=student_login,width=20)
b1.place(x=400,y=50)
b2=Button(root,text="TEACHER",command=teacher_login,width=20)
b2.place(x=400,y=150)
b3=Button(root,text="PRINCIPAL",command=principal_login,width=20)
b3.place(x=400,y=250)
b4=Button(root,text="register",command=REGISTER,width=20)
b4.place(x=400,y=400)
b5=Button(root,text="CLOSE",command=root.destroy,width=10)
b5.place(x=230,y=460)
root.mainloop()
