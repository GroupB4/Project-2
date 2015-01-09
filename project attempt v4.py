from Tkinter import*
import math
import time
root = Tk()
canvas=Canvas(root,width = 800, height = 800)
canvas.pack()
class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x1 = x + 20
        self.y1 = y + 20
        self.id1 = canvas.create_oval(self.x,self.y,self.x1,self.y1,fill = 'grey')
        self.rx = (self.x1 - self.x)/2
        self.ry = (self.y1 - self.y)/2
    
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center

    def LookAhead(self):
            self.xAhead = self.x + self.sum1*3
            self.yAhead = self.y + self.sum2*3
            #x - x1, y-y1 of sqr
            if self.xAhead > 100 and self.xAhead < 200 and self.yAhead > 100 and self.yAhead < 200:
                print "Hit the sqr"
    def movement(self,sum1,sum2,dist,canvas,dest):
        canvas.create_oval(dest[0],dest[1],dest[0]+10,dest[1]+10,fill = 'red')

        self.sum1 = sum1
        self.sum2 = sum2
       # self.xpos = self.x
        #self.ypos = self.y
        self.dist = dist
        #self.xdest = dest[0]
       # self.ydest = dest[1]
       # self.maxvol = 10
       # print "here"
        #print "xpos = ", self.xpos
       # print "xdest = ",self.xdest
        #print "ypos = ",self.ypos
        #print "ydest = ",self.ydest
        canvas.create_rectangle(100,100,200,200,fill = 'green')
        
        #self.xvelocity = (self.xdest - self.xpos) * self.maxvol
        #self.yvelocity = (self.ydest - self.ypos) * self.maxvol
        #self.velocity = self.xvelocity,self.yvelocity
        i = 0
        while i <= self.dist:
            i+= 1
            self.LookAhead()
            #print "HI", self.y
            self.y+=self.sum2
            self.x+=self.sum1
            self.x1 = self.x + 20
            self.y1 = self.y +20 
            self.current_coord = (self.x,self.y,self.x1,self.y1)
            
            canvas.coords(self.id1, self.current_coord)
            canvas.update()
            time.sleep(0.01)



class Destination:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        
    def finaldest(self):
        self.dest = self.x,self.y
        return self.dest

class vector():
    def __init__(self,list1,list2):
        self.diff = (list2[0] - list1[0], list2[1] - list1[1])
        print self.diff

    def distance(self):
        self.a = self.diff[0]
        self.b = self.diff[1]
        return math.sqrt(self.a**2 + self.b**2)

    def unit(self):
        distance = self.distance()
        self.aunit = self.a/distance
        self.bunit = self.b/distance
        return self.aunit, self.bunit


    



robot1 = Robot(20,20)
destination1 = Destination(234,345)
a = robot1.returncenter()
b = destination1.finaldest()
vec1 = vector(a,b)
print vec1.distance()
dist2pass = vec1.distance()
print vec1.unit()
sum1 = vec1.unit()
robot1.movement(sum1[0],sum1[1],dist2pass,canvas,b)

root.mainloop()
