import urllib.request, json
from tkinter import *
import random
from time import sleep

var2=0

while(1):
    if(var2==1):
        sleep(600)
    var2=1
    with urllib.request.urlopen("https://opentdb.com/api.php?amount=50&category=9&difficulty=easy&type=multiple") as url:
        data = json.loads(url.read().decode())
    questionToPick=random.randint(1,49)
    data['results'][questionToPick]['question'].replace("&quot",r'\"')

    def nextQuestion():
        print(data['results'][questionToPick]['correct_answer'])
        correctAnswer=data['results'][questionToPick]['correct_answer']
        if(correctAnswer==questions[var.get()-1]):
           print("Correct!")
        if(r1.cget("text")==correctAnswer):
           r1.config(bg="green")
        if (r2.cget("text") == correctAnswer):
           r2.config(bg="green")
        if (r3.cget("text") == correctAnswer):
           r3.config(bg="green")
        if (r4.cget("text") == correctAnswer):
               r4.config(bg="green")
        root.after(2000,root.destroy)

    def shutDown():
        sys.exit()

    root = Tk()
    var = IntVar()
    root.geometry("800x200")
    w1 = Label(root, text="Tom's Trivia! (C)")
    w2 = Label(root, text="Question:" +data['results'][questionToPick]['question'] )

    list=[]
    questions = []
    while questions.__len__()!=4:
        r=random.randint(1,4)
        if r not in list:
            list.append(r)
            if(r == 4):
                questions.append(data['results'][questionToPick]['correct_answer'])
            else:
                questions.append(data['results'][questionToPick]['incorrect_answers'][r-1])

    r1 = Radiobutton(root, text=questions[0], variable=var,value=1)
    r2 = Radiobutton(root, text=questions[1], variable=var,value=2)
    r3 = Radiobutton(root, text=questions[2], variable=var,value=3)
    r4 = Radiobutton(root, text=questions[3], variable=var,value=4)
    B = Button(root, text ="I AM SURE", command = nextQuestion)
    B2 = Button(root, text ="Shutdown", command = shutDown)

    #label = Label(root)

    w2.pack()
    r1.pack( anchor = W)
    r2.pack( anchor = W)
    r3.pack( anchor = W)
    r4.pack( anchor = W)
    B.pack()
    B2.pack()
    w1.pack()

    #label.pack()
    root.mainloop()