from Tkinter import*
import math
import time
import random
import io
import base64
import tkMessageBox
import Tkinter as tk
from urllib2 import urlopen

root = Tk()
root.title("Virtual Robot Project")

image_url = "http://i.imgur.com/Q9VXPIw.gif"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)

canvas=Canvas(root,width = 650, height = 650)

xpos = 0
ypos = 0
print(xpos, ypos)
canvas.create_image(xpos, ypos, image=photo)
canvas.pack()

greenTraffic = canvas.create_oval(3,29,3+10,29+10,fill = 'green')
amberTraffic = canvas.create_oval(3,17,3+10,17+10,fill = 'black')
redTraffic = canvas.create_oval(3,5,3+10,5+10,fill = 'black')

textWarning = canvas.create_text(600, 40, anchor=NE, text=".", fill='black')



###------Scale, GO and Exit Buttons------###
def speedSelect():
    speedValue = "Speed = " +str(var.get())
    label.config(text = speedValue)

def displayUFO():
    Timer1=Timer(root)
    Timer1.pack(side = BOTTOM, anchor = SW, padx = 4, pady = 4)
    Timer1.Start()
    robot1 = Robot(20,20)
    robot1.movement(canvas)

var = DoubleVar()

class toolbarStuff():
    def __init__(self,master):
        
        self.slider = Scale(variable=var, orient=HORIZONTAL, length=450, width=15,\
               sliderlength=10, from_=1, to=10, tickinterval=1,\
               cursor="hand2", bg="grey")
        self.slider.pack(side = RIGHT, padx=8, pady=8)
        
        goButton = Button(text="Start", cursor="hand2", command=displayUFO)
        goButton.pack(side=LEFT, padx=2, pady=2)

        self.button = Button(text="Exit", cursor="trek", command=self.Exit).pack(side=RIGHT)

    def Exit(self):
        if tkMessageBox.askokcancel("Exit", "Are you sure you want to leave?"):
            if tkMessageBox.askokcancel("Exit", "Really?"):
                root.destroy()

toolbarStuff = toolbarStuff(root)


label = Label()
label.pack(side=BOTTOM, padx=5)


###------Timer------###
toolbar = Frame(root)
toolbar.pack(side = BOTTOM, anchor = SW, padx = 10, pady = 5)


class Timer(Frame):


    #Implements timer widget#
    def __init__(self, thing=None,*toolbar):
        Frame.__init__(self, thing,toolbar)
        self.start = 0
        self.elapsedtime = 0
        self.running = 0
        self.timestr = StringVar()
        self.timerwidget()
        print "yellow"
        

    #Timer widget on screen#
    def timerwidget(self):
        l = Label(self, textvariable=self.timestr)
        self.settime(self.elapsedtime)
        l.pack(side=BOTTOM, padx=27)


    #Timer format in (00:00:00) = (Minutes : Seconds : Milliseconds)#
    def settime(self, elaps):
        minutes = int(elaps/60)
        seconds = int(elaps - minutes*60)
        milliseconds = int((elaps - minutes*60 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d'%(minutes, seconds, milliseconds))


    #Makes timer work#
    def update(self):
        self.elapsedtime = time.time() - self.start
        self.settime(self.elapsedtime)
        self.timer = self.after(50, self.update)


    #Starts timer#
    def Start(self):
        if not self.running:
            self.start = time.time() - self.elapsedtime
            self.update()
            self.running = 1


    #Stops timer#
    def Stop(self):
        if self.running:
            self.after_cancel(self.timer)
            self.elapsedtime = time.time() - self.start
            self.settime(self.elapsedtime)
            self.running = 0


#root = Timer(root)
#root.pack(side = BOTTOM, anchor = SW, padx = 4, pady = 4)


#Start and Stop buttons for timer#
#Button(toolbar, text = 'Start', cursor = "trek", command = root.Start).pack(side = LEFT, padx = 4)
#Button(toolbar, text = 'Stop', cursor = "trek", command = root.Stop).pack(side = LEFT, padx = 4)



###------Robot------###
class Robot(object):


    def __init__(self, x, y):
        self.q = -1
        self.obnum = 5-1
        self.x = x
        self.y = y
        self.x1 = x + 20
        self.y1 = y + 20
        self.pp=0
        self.rx = (self.x1 - self.x)/2
        self.ry = (self.y1 - self.y)/2
        self.tempxy =[]
        self.rotated = False
        

        ##Creating LandMarks

        
        #landmark 1
        LM4IMG_url = "http://i.imgur.com/8AZkQjm.gif"
        image4_byt = urlopen(LM4IMG_url).read()
        image4_b64 = base64.encodestring(image4_byt)
        self.photo4 = tk.PhotoImage(data=image4_b64)
        self.LM1 = LandMark(100,100,150,150,'blue',True)
        self.LM1.CreateLM()
        self.LM4e = canvas.create_image(125,125, image=self.photo4)
        self.LM1coords = self.LM1.givecoords()

        
        #landmark 2
        LM2IMG_url = "http://i.imgur.com/znZzpKZ.gif"
        image5_byt = urlopen(LM2IMG_url).read()
        image5_b64 = base64.encodestring(image5_byt)
        self.photo5 = tk.PhotoImage(data=image5_b64)
        self.LM2 = LandMark(150,250,150,250,'green',True)
        self.LM2.CreateLM()
        self.LM2e = canvas.create_image(125,225, image=self.photo5)
        self.LM2coords = self.LM2.givecoords()


        #landmark 3
        LM3IMG_url = "http://i.imgur.com/PvjBwBA.gif"
        image3_byt = urlopen(LM3IMG_url).read()
        image3_b64 = base64.encodestring(image3_byt)
        self.photo3 = tk.PhotoImage(data=image3_b64)
        self.LM3 = LandMark(200,200,250,250,'purple',True)
        self.LM3.CreateLM()
        self.LM3e = canvas.create_image(225,225, image=self.photo3)
        self.LM3coords = self.LM3.givecoords()

        
        #landmark 4
        LM4IMG_url = "http://i.imgur.com/T9Vht6S.gif"
        image6_byt = urlopen(LM4IMG_url).read()
        image6_b64 = base64.encodestring(image6_byt)
        self.photo6 = tk.PhotoImage(data=image6_b64)
        self.LM4 = LandMark(300,300,350,350,'orange',False)
        self.LM4.CreateLM()
        self.LM4e = canvas.create_image(325,325, image=self.photo6)
        self.LM4coords = self.LM4.givecoords()


        #landmark 5
        LM5IMG_url = "http://i.imgur.com/ZWSvQtS.gif"
        image7_byt = urlopen(LM5IMG_url).read()
        image7_b64 = base64.encodestring(image7_byt)
        self.photo7 = tk.PhotoImage(data=image7_b64)
        self.LM5 = LandMark(400,400,450,450,'black',True)
        self.LM5.CreateLM()
        self.LM5e = canvas.create_image(425,425, image=self.photo7)
        self.LM5coords = self.LM5.givecoords()


        
        
        ##Creating Tresure
        self.Tresure = []
        self.Tresure.append(self.LM1.havetresure())
        self.Tresure.append(self.LM2.havetresure())
        self.Tresure.append(self.LM3.havetresure())
        self.Tresure.append(self.LM4.havetresure())
        self.Tresure.append(self.LM5.havetresure())

        
        ##Creating lists of LandMarks and Tresure
        self.destxy = []
        self.LMList = [self.LM1,self.LM2,self.LM3,self.LM4,self.LM5]
        self.listx = [self.LM1coords[0],self.LM2coords[0],self.LM3coords[0],self.LM4coords[0],self.LM5coords[0]]
        self.listy = [self.LM1coords[1],self.LM2coords[1],self.LM3coords[1],self.LM4coords[1],self.LM5coords[1]]
        self.listx2 = [self.LM1coords[2],self.LM2coords[2],self.LM3coords[2],self.LM4coords[2],self.LM5coords[2]]
        self.listy2 = [self.LM1coords[3],self.LM2coords[3],self.LM3coords[3],self.LM4coords[3],self.LM5coords[3]]
        self.Tresure = [self.Tresure[0],self.Tresure[1],self.Tresure[2],self.Tresure[3],self.Tresure[4]]

        ##Call the method search
        self.search()

        ##Creating a visable oval that represents the robot and a line for its look ahead vector
        #http://i.imgur.com/zR2sDWw.gif
        #self.id1 = canvas.create_oval(self.x,self.y,self.x1,self.y1,fill = 'grey')

        robotimage_url = "http://i.imgur.com/zR2sDWw.gif"
        image2_byt = urlopen(robotimage_url).read()
        image2_b64 = base64.encodestring(image2_byt)
        self.photo2 = tk.PhotoImage(data=image2_b64)
        #canvas.create_image(0,0, image=photo2)
        self.id1 = canvas.create_image(self.x,self.y, image=self.photo2)
        canvas.update()

        self.z = canvas.create_line(self.x+10,self.y+10,self.x+100,self.x+100)
        self.rr = self.returncenter()



    ##The search method decides what LandMarks need to be visited and avoided
    def search(self):
        self.q += 1

        if self.Tresure[self.q] == True:
            LMcoordtemp = self.LMList[self.q].givecoords()
            destx = LMcoordtemp[2] - LMcoordtemp[0]
            destx = destx/2
            destx = destx+LMcoordtemp[0]
            desty = LMcoordtemp[3] - LMcoordtemp[1]
            desty = desty/2
            desty = desty + LMcoordtemp[1]
            self.destxy = [destx,desty]
            print "FUFUUFUFUFUFUFUUFUFUFluffy ",self.destxy
        else:
            self.search()


    ##Not reallt used finds the center on the robots oval
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center




    ##Looks at the end of the LookAhead vector to determin whether the robot need to avoid anything or not
    def LookAhead(self):
            unit = self.vec1.unit()
            #print "From Look ", unit
            self.xAhead = self.x + unit[0]*70
            self.yAhead = self.y + unit[1]*70

            canvas.coords(self.z,self.x+10,self.y+10,self.xAhead,self.yAhead)

            i=0
            ###########x,x1,y,y1############
            for i in range (0,self.obnum):
                if self.LMList[i].havetresure() == False and self.xAhead >= self.listx[i] and self.xAhead <= self.listx2[i] and self.yAhead >= self.listy[i]  and self.yAhead <= self.listy2[i]:
                    
                    print "Hit the sqr"
                    self.rotated = self.vec1.rotate(90)
                    canvas.update
            else:
                pass
    ##Move from a to b
    ##This function is to move our robot while continually call look ahead
    def movement(self,canvas):
        dest = self.destxy
        self.rr = self.returncenter()
        self.vec1 = vector(self.rr,dest)
        #canvas.create_line(self.rr,dest)
        end = []
        dist = self.vec1.distance()
        i = 0

        global counting
        counting = 1

        global sleeping
        sleeping = 1

        global lightchange    
        lightchange = 1

        while i <= dist:
            #print dist
            i+= 1
            sum1 = self.vec1.unit()
            self.LookAhead()
            
##################################################################
                
            if sleeping == 1:
               time.sleep(0.01)
            elif sleeping == 2:
                time.sleep(0.07)
            elif sleeping == 3:
                time.sleep(1.0)

            counting += 1

        
            if counting == 1:
                lightchange = 4
            elif counting == 5:
                lightchange = 1

            if counting == 90:
                lightchange = 2
            elif counting == 110:
                counting = 0
                lightchange = 3

            if lightchange == 1:
                canvas.itemconfigure(greenTraffic, fill = 'green')
                canvas.itemconfigure(amberTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'black')
                sleeping = 1
                canvas.itemconfigure(textWarning, text=".", fill='black')
        
            elif lightchange == 2:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'black')
                sleeping = 2
                canvas.itemconfigure(textWarning, text="Meteor shower incoming!!!", fill='white')
            
            elif lightchange == 3:
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(amberTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 3
                canvas.itemconfigure(textWarning, text="Meteor shower in effect!!!", fill='white')
                print "Stop"

            elif lightchange == 4:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 2
            
###############################################################################
            
            if self.rr == dest:
                print "FUFUFUFU:LASJFJSLKNFQQNOFNPIFQ"
                dest[0] = tempxdest
                dest[1] = tempydest
                
                self.vec1 = vector(self.rr,dest)
                
                dist = self.vec1.distance()
                i=0
                #dist = self.vec1.distance()
            #print "HI", self.y
            self.y+=sum1[1]
            self.x+=sum1[0]
            self.x1 = self.x + 20
            self.y1 = self.y +20 
            #self.current_coord = (self.x,self.y,self.x1,self.y1)
            self.current_coord = (self.x,self.y)

            
            enddest1 = dest[0]
            enddest2  = dest[1]
            finalenddest = int(enddest1),int(enddest2)
            current1 = self.x
            current2 = self.y
            finalcurrent = int(current1)+10,int(current2)+10
            #print finalenddest
            #print finalcurrent
            #print "yy"
  
            ####need to create a small square
            var1= self.destxy[0]+1
            var2= self.destxy[0]-1
            var3= self.destxy[1]+1
            var4= self.destxy[1]-1
            if self.rotated == True:
                print "Nothing to see here..."
                tempxdest = dest[0]
                tempydest = dest[1]
                tempxy = dest
                self.LookAhead()
                dest[0] = self.xAhead
                dest[1] = self.yAhead
                self.rr= (self.x,self.y)
                
                self.vec2 = vector(self.rr,dest)
                
                end = self.vec2.returnend()
                dist = self.vec2.distance()
                #print dist
                i=0
                for x in range(0,int(dist)):
                    sum2 = self.vec2.unit()
                    print"This is sum2 ", sum2
                    self.y+=sum2[1]
                    self.x+=sum2[0]
                    self.x1 = self.x + 20
                    self.y1 = self.y +20 
                    self.current_coord = (self.x,self.y)
                    canvas.coords(self.z,self.x+10,self.y+10,self.xAhead,self.yAhead)
                    canvas.coords(self.id1, self.current_coord)
                    canvas.update()
                    time.sleep(0.01)
                    dist = 0
                self.q = self.q -1
                    #dest = tempxy
                self.rotated = False
                self.movement(canvas)
            
            if finalcurrent[0] >= var2 and finalcurrent[0] <= var1 and finalcurrent[1] >= var4  and finalcurrent[1] <= var3:
                print "Of course it worked i never doubted it!"
                self.search()
                self.movement(canvas)
            print end
            if self.rr == end:
                print "Or here..."
                
                           
            canvas.coords(self.id1, self.current_coord)
            canvas.update()
            
            
            time.sleep(0.01)


            
## class that deals with all land marks
class LandMark:
    def __init__(self,x,x1,y,y1,fill,tresure):
        self.x = x
        self.x1= x1
        self.y = y
        self.y1 = y1
        self.colour = fill
        self.visitmaybe = tresure
        
    
    def CreateLM(self):
        canvas.create_rectangle(self.x,self.x1,self.y,self.y1,fill = self.colour)        
    def givecoords(self):
        return self.x,self.x1,self.y,self.y1

    def havetresure(self):
        if self.visitmaybe == True:
            return True
            
        else:
            return False



class vector():
    def __init__(self,list1,list2):
        self.list2 = list2
        self.diff = [list2[0] - list1[0], list2[1] - list1[1]]
        

    def distance(self):
        self.a = self.diff[0]
        self.b = self.diff[1]
        return math.sqrt(self.a**2 + self.b**2)

    def unit(self): 
        distance = self.distance()
        self.aunit = self.a/distance
        self.bunit = self.b/distance

        return self.aunit, self.bunit

    def rotate(self,angle):
        oldx = self.diff[0]
        oldy = self.diff[1]

        newx = oldx*math.cos(angle)-oldy*math.sin(angle)
        newy = oldx*math.sin(angle)+oldy*math.cos(angle)

        self.diff = (newx, newy)
        return True
    def returnend(self):
        return self.list2




#robot1 = Robot(20,20)
#robot1.movement(canvas)


root.mainloop()
