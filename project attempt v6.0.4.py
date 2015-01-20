from Tkinter import*
#from PIL import Image, ImageTk
import math
import time
root = Tk()
#img = ImageTk.PhotoImage(Image.open("C:\Users\Pavilion\Pictures\space theme\spaceBK3.png"))
#canvas.create_image(0,0, image = img)
root.title("Virtual Robot Project")

import io
import base64
import Tkinter as tk
from urllib2 import urlopen


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


class Robot(object):


    

    def __init__(self, x, y, destination):
        self.x = x
        self.y = y
        self.x1 = x + 20
        self.y1 = y + 20
        self.id1 = canvas.create_oval(self.x,self.y,self.x1,self.y1,fill = 'grey')
        self.rx = (self.x1 - self.x)/2
        self.ry = (self.y1 - self.y)/2
        self.z = canvas.create_line(self.x+10,self.y+10,self.x+100,self.x+100)
        self.rotated = False
        #canvas.create_rectangle(self.obx,self.oby,self.obx2,self.oby2,fill = 'green')
        #canvas.create_rectangle(self.ob2x,self.ob2y,self.ob2x2,self.ob2y2,fill = 'red')
        self.LM1 = LandMark(400,400,600,600,'red',True)
        self.LM1.CreateLM()
        self.LM2 = LandMark(100,100,200,200,'green',False)
        self.LM1coords = self.LM2.givecoords()
        self.LM2coords = self.LM2.givecoords()
        self.LM2.CreateLM()
        self.LM1.havetresure()
        self.LM2.havetresure()
        self.destination = destination
        print self.LM2coords[0]
        self.listx = [self.LM2coords[0],self.LM1coords[0]]
        self.listy = [self.LM2coords[1],self.LM1coords[1]]
        self.listx2 = [self.LM2coords[2],self.LM1coords[2]]
        self.listy2 = [self.LM2coords[3],self.LM1coords[3]]
        a = self.returncenter()
        b = destination.finaldest()
        self.vec1 = vector(a,b)
        #print self.vec1.distance()
        dist2pass = self.vec1.distance()
        #print self.vec1.unit()
        #print self.listx
        #robot1.movement(sum1[0],sum1[1],dist2pass,canvas,b)
        canvas.create_line(20,20,b)
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center

    def LookAhead(self):
            unit = self.vec1.unit()
            self.xAhead = self.x + unit[0]*50
            self.yAhead = self.y + unit[1]*50
            canvas.coords(self.z,self.x+10,self.y+10,self.xAhead,self.yAhead) 
            #self.z = canvas.create_line(self.x,self.y,self.xAhead,self.yAhead)
            #self.z = canvas.create_line(self.x,self.y,self.x+100,self.y+100, fill="red", dash=(4, 4))
            #x - x1, y-y1 of sqr
            #print self.listx
            i=0
            ###########x,x1,y,y1############
            for i in range (0,2):
                if self.xAhead >= self.listx[i] and self.xAhead <= self.listx2[i] and self.yAhead >= self.listy[i]  and self.yAhead <= self.listy2[i]:
            #if self.xAhead >= self.obx and self.xAhead <= self.obx2 and self.yAhead >= self.oby  and self.yAhead <= self.oby2:
            #if self.xAhead in self.listx and self.xAhead
                    print "Hit the sqr"
                    self.rotated = self.vec1.rotate(90)
                    #print self.rotated
            else:
                #print "Not Hitting"
                pass
            #canvas.delete(self.z)
    def movement(self,canvas):
        dest = self.destination.finaldest()
        canvas.create_oval(dest[0]-10,dest[1]-10,dest[0]+10,dest[1]+10,fill = 'red')

       # self.xpos = self.x
        #self.ypos = self.y
        #self.xdest = dest[0]
       # self.ydest = dest[1]
       # self.maxvol = 10
       # print "here"
        #print "xpos = ", self.xpos
       # print "xdest = ",self.xdest
        #print "ypos = ",self.ypos
        #print "ydest = ",self.ydest
        
        
        #self.xvelocity = (self.xdest - self.xpos) * self.maxvol
        #self.yvelocity = (self.ydest - self.ypos) * self.maxvol
        #self.velocity = self.xvelocity,self.yvelocity

        dist = self.vec1.distance()
        i = 0

        while i <= dist:
            #print dist
            i+= 1
            sum1 = self.vec1.unit()
            self.LookAhead()
            self.rr = (self.x+10,self.y+10)
                
            
            if self.rotated == True:
                tempxdest = dest[0]
                tempydest = dest[1]
                dest[0] = self.xAhead
                dest[1] = self.yAhead
                self.rr= (self.x,self.y)
                self.vec2 = vector(self.rr,dest)
                self.vec2.distance()
                dist = self.vec2.distance()
                #print dist
                i=0
                self.rotated = False
            if i >= dist -1:
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
            self.current_coord = (self.x,self.y,self.x1,self.y1)

            
            enddest1 = dest[0]
            enddest2  = dest[1]
            finalenddest = int(enddest1),int(enddest2)
            current1 = self.x
            current2 = self.y
            finalcurrent = int(current1),int(current2)
            #print finalenddest
            #print finalcurrent
            #print "yy"
            if finalcurrent == finalenddest:
                print "mfdsalkgnoisngoierwANGOERWJNOIGRNEROIN"
            canvas.coords(self.id1, self.current_coord)
            canvas.update()
            
            time.sleep(0.01)

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
            print "Yes"
        else:
            print "No"


class Destination:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        
    def finaldest(self):
        self.dest = [self.x,self.y]
        return self.dest

class vector():
    def __init__(self,list1,list2):
        self.diff = [list2[0] - list1[0], list2[1] - list1[1]]
        #print self.diff

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

class treasure():
    def __init__(self):
        treasure1 = canvas.create_oval(200,200,280,280,fill = 'purple')
        treasure2 = canvas.create_oval(300,500,380,420,fill = 'purple')
        treasure3 = canvas.create_oval(100,500,180,415,fill = 'purple')




treasure()

destination1 = Destination(316,523)
robot1 = Robot(20,20, destination1)
robot1.movement(canvas)
root.mainloop()
