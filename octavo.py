import tkinter
from tkinter import *
import random
import string

root=Tk()
root.title("To-do-list")
root.geometry("700x450")
root.resizable(False,False)
task_list=[]
root.configure(background='#282828')




def addTask():
    task =task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks =taskfile.readlines()

        for task in tasks:
            if task !='\n':
             task_list.append(task)
             listbox.insert(END, task) 
    except:
        file=open('tasklist.txt','w')
        file.close()



frameSide=Frame(root,width=175,height=450,bg="#313131")
frameSide.place(x=0,y=0)

heading=Label(frameSide,text="Octavo",font="arial 20",fg="white",bg="#313131")
heading.place(x=25,y=20)
photoNew = PhotoImage(file = r"G:\octavo\todo1.png")
buttonNew= Button(frameSide,image = photoNew, width=175,bg="#313131",bd=0)
buttonNew.place(x=0,y=100)
#main

frame=Frame(root,width=510,height=50,bg="#282828")
frame.place(x=190,y=325)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",fg="#313131",bd=0)
task_entry.place(x=0,y=14)
task_entry.focus

photo1 = PhotoImage(file = r"G:\octavo\btn.png")
button=Button(frame, image = photo1,bd=0,bg="#282828",command=addTask)
button.place(x=250,y=10)
photo = PhotoImage(file = r"G:\octavo\dltbtn.png")
delButton=Button(frame, image = photo,bd=0,bg="#282828",command=deleteTask)
delButton.place(x=350,y=10)
#listbox

frame1=Frame(root,bd=3,width=525,height=280,bg="#313131",borderwidth=0)
frame1.pack(pady=(250,0))
frame1.place(x=175,y=0)
listbox=Listbox(frame1,font=('arial,12'),width=55,height=16,bg="#313131",fg="white",cursor="hand2",selectbackground="#683FBF")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
#delete






root.mainloop()