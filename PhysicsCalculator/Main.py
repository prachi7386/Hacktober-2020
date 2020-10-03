from Tkinter import *
def pc():
    import PC
def quiz():
    import Quiz
    Quiz.quiz()
def quiz12():
    import Quiz12
def facts():
    import Facts
def feedback():
    import Feedback
def QP():
    import QP
def chapter():
    import chapters
root =  Tk()

button1 = Menubutton(root , text = "Quiz" , width = 25 , height = 4 , relief = RAISED)
button1.place(relx=.5, rely=.5, anchor="c")
button1.menu = Menu(button1)
button1["menu"] = button1.menu     #drop down menu
button1.menu.add_checkbutton(label = "Grade 11" , command  = quiz)
button1.menu.add_checkbutton(label = "Grade 12" , command = quiz12)

button2 = Button(root , text = "Important topics to refer ", width = 25 , height = 4 , relief = RAISED,command = chapter)
button2.place(relx=.5, rely=.3, anchor="c")

button3 = Button(root , text = "Physics calculator ", width = 25 , height = 4 , relief = RAISED , command = pc)
button3.place(relx=.5, rely=.4, anchor="c" )

button4 = Button(root , text = "Previous Q.P" , width = 25 , height = 4 , relief = RAISED , command = QP)
button4.place(relx=.5, rely=.6, anchor="c")


button5 = Button(root , text = "Facts ", width = 25 , height = 4 , relief = RAISED , command = facts)
button5.place(relx=.5, rely=.7, anchor="c")

button6 = Button(root , text = "Feedback", width = 25 , height = 4 , relief = RAISED , command = feedback)
button6.place(relx=.5, rely=.8, anchor="c")


root.mainloop()
