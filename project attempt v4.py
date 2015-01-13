from Tkinter import*
import math
import time
root = Tk()
canvas=Canvas(root,width = 600, height = 600)
canvas.pack()
root.title("Virtual Robot Project")

x_min = 0
y_min = 0
x_max = 600
y_max = 600



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


        self.destination = destination
        a = self.returncenter()
        b = destination.finaldest()
        self.vec1 = vector(a,b)
        print self.vec1.distance()
        dist2pass = self.vec1.distance()
        print self.vec1.unit()
        
        #robot1.movement(sum1[0],sum1[1],dist2pass,canvas,b)
    
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center

    def LookAhead(self):
            unit = self.vec1.unit()
            self.xAhead = self.x + unit[0]*100
            self.yAhead = self.y + unit[1]*100
            canvas.coords(self.z,self.x+10,self.y+10,self.xAhead,self.yAhead) 
            #self.z = canvas.create_line(self.x,self.y,self.xAhead,self.yAhead)
            #self.z = canvas.create_line(self.x,self.y,self.x+100,self.y+100, fill="red", dash=(4, 4))
            #x - x1, y-y1 of sqr
            if self.xAhead > 100 and self.xAhead < 200 and self.yAhead > 100 and self.yAhead < 200:
                print "Hit the sqr"
                self.vec1.rotate(30)
            else:
                print "Not Hitting"
            
            #canvas.delete(self.z)

    def moveAway(self):
        print "move away"
        
        if self.x>=x_max:
            self.vec1.rotate(30)
            print "Right wall"
        if self.y <= y_min:
            self.vec1.rotate(45)
            print "Top wall"
        if self.y1 >= y_max:
            self.vec1.rotate(30)
            print "Bottom wall"
        if self.x1 <=x_min:
            self.vec1.rotate(30)
            print "Left wall"

        print "end"
        
    def movement(self,canvas):
        dest = self.destination.finaldest()
        canvas.create_oval(dest[0],dest[1],dest[0]+10,dest[1]+10,fill = 'red')

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
        canvas.create_rectangle(100,100,200,200,fill = 'green')
        
        #self.xvelocity = (self.xdest - self.xpos) * self.maxvol
        #self.yvelocity = (self.ydest - self.ypos) * self.maxvol
        #self.velocity = self.xvelocity,self.yvelocity

        dist = self.vec1.distance()
        i = 0
        move = True
        while move == True:
            i+= 1
            
            
            self.LookAhead()
            self.moveAway()

            sum1 = self.vec1.unit()
            dist = self.vec1.distance()
            #print "HI", self.y
            self.y+=sum1[1]
            self.x+=sum1[0]
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

    def rotate(self,angle):
        oldx = self.diff[0]
        oldy = self.diff[1]

        newx = oldx*math.cos(angle)-oldy*math.sin(angle)
        newy = oldx*math.sin(angle)+oldy*math.cos(angle)
        

        self.diff = (newx, newy)


class treasure():
    def __init__(self):
        treasure1 = canvas.create_oval(200,200,280,280,fill = 'purple')
        treasure2 = canvas.create_oval(300,500,380,420,fill = 'purple')
        treasure3 = canvas.create_oval(100,500,180,415,fill = 'purple')




treasure()
destination1 = Destination(234,345)
robot1 = Robot(20,20, destination1)
robot1.movement(canvas)
root.mainloop()
