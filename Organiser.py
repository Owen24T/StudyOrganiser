from os import getcwd
from tkinter import *
import threading


dataPATH = "StudyOrganiser\APPDATA\Organiser Database.txt"
print(getcwd())
subject_dict = {0: "COMP2511", 1: "MMAN2300", 2: "MMAN1130"}

def viewData():
    # Open file and print contents in Labels
    f = open(dataPATH, 'r')
    all_tasks = f.readlines()
    tasks_zero = [task[2:] for task in all_tasks if task.startswith("0")]
    tasks_one = [task[2:] for task in all_tasks if task.startswith("1")]
    tasks_two = [task[2:] for task in all_tasks if task.startswith("2")]

    display0 = ""
    display1 = ""
    display2 = ""
    
    for index, task in enumerate(tasks_zero):
        display0 += f"Task {index + 1}: {task}"
    
    for index, task in enumerate(tasks_one):
        display1 += f"Task {index + 1}: {task}"
    
    for index, task in enumerate(tasks_two):
        display2 += f"Task {index + 1}: {task}"

    # If no tasks to show, print some message.
    # Create 3 labels for each subject and adjust font size and placement

    
    if display0 + display1 + display2 == '':
        tempLabel0 = Label(root, text="No tasks for all courses!", font=("Times New Roman", 15))
        tempLabel0.place(x=650, y=270)
        t = threading.Timer(3, lambda: tempLabel0.destroy())
        t.start()
    else:
        if display0 == '':
            display0 = f"No tasks for {subject_dict[0]}!"
        if display1 == '':
            display1 = f"No tasks for {subject_dict[1]}!"
        if display2 == '':
            display2 = f"No tasks for {subject_dict[2]}!"
                
        tempLabel0 = Label(root, text=display0.rstrip(), font=("Times New Roman", 18))
        tempLabel1 = Label(root, text=display1.rstrip(), font=("Times New Roman", 18))
        tempLabel2 = Label(root, text=display2.rstrip(), font=("Times New Roman", 18))
        tempLabel0.place(x=380, y=100)
        tempLabel1.place(x=380, y=300)
        tempLabel2.place(x=380, y=500)
        
        t = threading.Timer(10, destroyLabels3, args=(tempLabel0,tempLabel1,tempLabel2))
        t.start()

    f.close()

def addData():
    # Open file and add contents as strings
    f = open(dataPATH, 'a')
    selection = myLstbox1.curselection()
    try:
        subject = int(selection[0]/3)
    except:
        tempLabel0 = Label(root, text="Error: No subject chosen!", font=("Times New Roman", 15), fg="red")
        tempLabel0.place(x=650, y=270)
        t = threading.Timer(3, lambda: tempLabel0.destroy())
        t.start()
        return
    text = myEntry1.get()
    package = str(subject) + ' ' + text + '\n'
    f.write(package)

    tempLabel1 = Label(root, text=f"Task for {subject_dict[subject]} successfully added!")
    tempLabel1.place(x=700, y=100)
    t = threading.Timer(3, lambda: tempLabel1.destroy())
    t.start()

    myEntry1.delete(first=0, last="end")

    f.close()


def deleteData():
    # Open file and delete item acccording to number and course
    f = open(dataPATH, 'r')
    all_list = f.readlines()
    f.close()

    selection = myLstbox1.curselection()
    try:
        subject = int(selection[0]/3)
    except:
        tempLabel0 = Label(root, text="Error: No subject chosen!", font=("Times New Roman", 15), fg="red")
        tempLabel0.place(x=650, y=270)
        t = threading.Timer(3, lambda: tempLabel0.destroy())
        t.start()
        return
    
    try:
        task_num = int(myEntry1.get())
    except:
        tempLabel0 = Label(root, text="Error: No task entered!", font=("Times New Roman", 15), fg="red")
        tempLabel0.place(x=650, y=270)
        t = threading.Timer(3, lambda: tempLabel0.destroy())
        t.start()
        return

    task_list = []
    for task in all_list:
        if task.startswith(str(subject)):
            task_list.append(task)
    
    try:
        delete_task = task_list[task_num - 1]
    except:
        tempLabel0 = Label(root, text=f"Error: Task {task_num} doesnt exist!", font=("Times New Roman", 15), fg="red")
        tempLabel0.place(x=650, y=270)
        t = threading.Timer(3, lambda: tempLabel0.destroy())
        t.start()
        return

    f = open(dataPATH, 'w')
    for task in all_list:
        if task != delete_task:
            f.write(task)
    f.close()

    tempLabel2 = Label(root, text=f"Task {task_num} for {subject_dict[subject]} successfully deleted!")
    tempLabel2.place(x=1050, y=100)
    t = threading.Timer(3, lambda: tempLabel2.destroy())
    t.start()
    myEntry1.delete(first=0, last="end")

def showHelp():
    myLabel2 = Label(root, text="To add a task, select the subject on the left\nthen enter the task and press ADD", font=("Times New Roman", 15), bg="#BBBBBB")
    myLabel3 = Label(root, text="To remove a task, select the subject on the left\nthen enter the task number and press DELETE", font=("Times New Roman", 15), bg="#BBBBBB")
    myLabel2.place(x=360, y=700)
    myLabel3.place(x=780, y=700)
    t = threading.Timer(10, destroyLabels2, args=(myLabel2, myLabel3))
    t.start()

def destroyLabels3(label1, label2, label3):
    label1.destroy()
    label2.destroy()
    label3.destroy()

def destroyLabels2(label1, label2):
    label1.destroy()
    label2.destroy()


root = Tk()
root.title("Term 1 Organiser")
root.attributes("-fullscreen", True)


myLstbox1 = Listbox(root, height=9, font=("Calibri", 40), width=11, bg="#DDDDDD", foreground="#0A1172")
myLstbox1.insert(0, subject_dict[0])
myLstbox1.insert(1, '')
myLstbox1.insert(2, '')
myLstbox1.insert(3, subject_dict[1])
myLstbox1.insert(4, '')
myLstbox1.insert(5, '')
myLstbox1.insert(6, subject_dict[2])
myLstbox1.insert(7, '')
myLstbox1.insert(8, '')
myLstbox1.place(x=10, y=90)

myButton1 = Button(root, text="VIEW", height=5, width=45, bg="#FFD700", command=viewData)
myButton1.place(x=310, y=5)
myButton2 = Button(root, text="ADD", height=5, width=45, bg="#228B22", command=addData)
myButton2.place(x=650, y=5)
myButton3 = Button(root, text="DELETE", height=5, width=45, bg="#D2042D", command=deleteData)
myButton3.place(x=990, y=5)

myEntry1 = Entry(root, width=100, font=("Calibri", 25), bg="#FFFBC8")
myEntry1.place(relwidth=0.739, relheight=0.763, x=310, y=92)

myLabel1 = Label(root, text="Term 1 2022", font=("Calibri", 30), bd=8, bg="#AAAAAA")
myLabel1.place(x=40,y=10)



mybutton4 = Button(root, text="Show Help", height=2, width=18, command=showHelp, bg="#52D9EB")
mybutton4.place(x=80, y=700)
myButton5 = Button(root, text="QUIT", height=2, width=10, command=root.destroy, bg="#AAAAAA", fg="#D2042D")
myButton5.place(x=1220, y=700)

root.mainloop()