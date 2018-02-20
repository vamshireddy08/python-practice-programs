class Class_name():
    print "class object created"
    def __init__(self,name,age,gender='m'):
        self.age=age
        self.gender=gender
        self.name=name
x=Class_name(name="vamshi",age=21)
print "type of class object ",type(x)
print "class attribute(name of a person) ",x.name
print "class gender attribute ",x.gender

c=Class_name(name='manu',age=5,gender='f')
print c.name 
print c.gender

class Circle(object):
    pi=3.14
    def __init__(self,r=1):
        self.r=r 
        self.perimeter=2*self.r*self.pi
    def area(self):
        """
        calculates the area of a circle 
        input: radius 
        output: area
        """
        return (self.r**2)*self.pi 

c=Circle(r=10)
print "pi value ",c.pi 
print "radius of circle ",c.r
print c.area()
print c.perimeter
c.r=input("enter new radius(integer type)   ")
print c.r 
print c.area()


class vamshi():
    g=11
    def __init__(self):
        print "vamshi class object created "
    
    
y=vamshi()
y.g=input("enter integer   ")
print "your value is ",y.g
        
