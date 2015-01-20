from Tkinter import*
#from PIL import Image, ImageTk
import math
import time
root = Tk()
canvas=Canvas(root,width = 650, height = 650)
#img = ImageTk.PhotoImage(Image.open("C:\Users\Pavilion\Pictures\space theme\spaceBK3.png"))
#canvas.create_image(0,0, image = img)
canvas.pack()
root.title("Virtual Robot Project")





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
        self.LM1 = LandMark(100,100,150,150,'red',True)
        self.LM1.CreateLM()
        self.LM1coords = self.LM1.givecoords()
        self.LM2 = LandMark(100,200,150,250,'green',True)
        self.LM2.CreateLM()
        self.LM2coords = self.LM2.givecoords()
        self.LM3 = LandMark(200,200,250,250,'purple',True)
        self.LM3.CreateLM()
        self.LM3coords = self.LM3.givecoords()
        self.LM4 = LandMark(300,300,350,350,'orange',False)
        self.LM4.CreateLM()
        self.LM4coords = self.LM4.givecoords()
        self.LM5 = LandMark(400,400,450,450,'black',True)
        self.LM5.CreateLM()
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
        self.id1 = canvas.create_oval(self.x,self.y,self.x1,self.y1,fill = 'grey')
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
            print "FUFUUFUFUFUFUFUUFUFUF ",self.destxy
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

        while i <= dist:
            #print dist
            i+= 1
            sum1 = self.vec1.unit()
            self.LookAhead()
            
                
            
            
            
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
            self.current_coord = (self.x,self.y,self.x1,self.y1)

            
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
                print "FUCK HER RIGHT IN THE PUSSY"
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
                    self.current_coord = (self.x,self.y,self.x1,self.y1)
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
                print "Erm it might be wroking"
                self.search()
                self.movement(canvas)
            print end
            if self.rr == end:
                print "Fucker"
                
                           
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




robot1 = Robot(20,20)
robot1.movement(canvas)
root.mainloop()
