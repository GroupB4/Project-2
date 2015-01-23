import time
import random

from Tkinter import *
root = Tk()
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack(padx=10,pady=10)

def speedSelect():
    speedValue = "Speed = " +str(var.get())
    label.config(text = speedValue)

#toolbar and slider crap
var = DoubleVar()

class App:
    def __init__(self, master):
        toolbar = Frame(root, bg="blue")
        toolbar.pack(side=BOTTOM,fill=X)
        self.button = Button(toolbar, text="QUIT", fg="black", cursor="hand2", command=root.destroy)
        self.button.pack(side=LEFT)
        self.pr = Button(toolbar, text="Click", cursor="hand2", command=self.write_pr)
        self.pr.pack(side=LEFT)

        self.goButton = Button(toolbar, text="GO", cursor="hand2", command=self.GO)
        self.goButton.pack(side=LEFT, padx=2, pady=2)

        self.slider = Scale(toolbar, variable=var, orient=HORIZONTAL, length=300, width=15,\
               sliderlength=10, from_=1, to=10, tickinterval=1,\
               cursor="hand2", bg="grey")

        self.slider.pack(fill=X, padx=4, pady=4)


    def write_pr(self):
        print "aaaarghh"

    def GO(self):
        #Variablllleeeeees
        vx=4.0
        vy=4.0

        x_min=0.0
        y_min=0.0
        x_max=400.0
        y_max=300.0


        #Moooooooooooooooove
        for t in range(1,800):
            x1,y1,x2,y2=canvas.coords(id1)
            RandomVal=random.randint(1,100)
            if RandomVal>95:
                vx=-var.get()
                vy==var.get()

            if x1 >=x_max:
                vx=-4.0
            if y1 <=y_min:
                vy=4.0
            if y2 >=y_max:
                vy = -4.0
            if x1 <=x_min:
                vx=4.0

            canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
            canvas.update()
            time.sleep(0.05)

        

app = App(root)




changeSpeedButton = Button(root, text="Get Current Speed Value", cursor="hand2", command=speedSelect)
changeSpeedButton.pack()

label = Label()
label.pack()





#Roooobooot
id1=canvas.create_rectangle(3,7,3+10,7+10, fill="purple", outline="lightblue",\
                            width=2)



root.mainloop()
