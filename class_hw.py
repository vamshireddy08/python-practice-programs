class Line(object):
    def __init__(self,coor1,coor2):
        self.x1=coor1[0]
        self.x2=coor2[0]
        self.y1=coor1[1]
        self.y2=coor2[1]
    def distance(self):
        t= ((self.y2-self.y1)**2) +((self.x2-self.x1)**2)
        return  t**0.5  
            
    def slope(self):
        return (self.y2-self.y1)/float(self.x2-self.x1)
    
coordinate1=(3,2)
coordinate2=(8,10)

li=Line(coordinate1,coordinate2)

print "line distance ",li.distance()
print "line slope    ",li.slope()

class Cylinder(object):
    def __init__(self,height=1,radius=1):
        self.h=height
        self.r=radius
    def volume(self):
        return 3.14*self.h*(self.r**2)
    def surface_area(self):
        return 2*3.14*self.r*self.h +(2*3.14*(self.r**2))

c=Cylinder(2,3)
print "cylinder volume       ",c.volume()
print "cylinder surface area ",c.surface_area()
