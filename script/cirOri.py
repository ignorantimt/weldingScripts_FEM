import math

class point3:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c

# (x-x1)/dx=(y-y1)/dy=(z-z1)/dz
class line3:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def getDelta(self):
        dx = p2.x-p1.x 
        dy = p2.y-p1.y 
        dz = p2.z-p1.z 
        return dx,dy,dz

    def getLength(self):
        dx,dy,dz = self.getDelta()
        length = math.sqrt(dx*dx+dy*dy+dz*dz)
        return length

    def point3vt(self,t_cur,t_total):
        x1 = p1.x
        y1 = p1.y
        z1 = p1.z
        dx,dy,dz = self.getDelta()
        length = self.getLength()
        v = length/t_total
        lp = point3(0,0,0)
        lp.x = x1+v*t_cur*dx/length
        lp.y = y1+v*t_cur*dy/length
        lp.z = z1+v*t_cur*dz/length
        return lp

# 3-point arc on a circle. angle < 180
class arc3:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def getPxyz(self,p):
        return p.x,p.y,p.z

    def getCirOrig(self):
        x1,y1,z1 = self.getPxyz(self.p1)
        x2,y2,z2 = self.getPxyz(self.p2)
        x3,y3,z3 = self.getPxyz(self.p3)


        a1 = (y1*z2 - y2*z1 - y1*z3 + y3*z1 + y2*z3 - y3*z2)
        b1 = -(x1*z2 - x2*z1 - x1*z3 + x3*z1 + x2*z3 - x3*z2)
        c1 = (x1*y2 - x2*y1 - x1*y3 + x3*y1 + x2*y3 - x3*y2)
        d1 = -(x1*y2*z3 - x1*y3*z2 - x2*y1*z3 + x2*y3*z1 + x3*y1*z2 - x3*y2*z1)

        a2 = 2 * (x2 - x1)
        b2 = 2 * (y2 - y1)
        c2 = 2 * (z2 - z1)
        d2 = x1 * x1 + y1 * y1 + z1 * z1 - x2 * x2 - y2 * y2 - z2 * z2

        a3 = 2 * (x3 - x1)
        b3 = 2 * (y3 - y1)
        c3 = 2 * (z3 - z1)
        d3 = x1 * x1 + y1 * y1 + z1 * z1 - x3 * x3 - y3 * y3 - z3 * z3

        self.ox = -(b1*c2*d3 - b1*c3*d2 - b2*c1*d3 + b2*c3*d1 + b3*c1*d2 - b3*c2*d1)/(a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1)
        self.oy =  (a1*c2*d3 - a1*c3*d2 - a2*c1*d3 + a2*c3*d1 + a3*c1*d2 - a3*c2*d1)/(a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1)
        self.oz = -(a1*b2*d3 - a1*b3*d2 - a2*b1*d3 + a2*b3*d1 + a3*b1*d2 - a3*b2*d1)/(a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1)
        return self.ox,self.oy,self.oz
    
    def getRadius(self):
        ox,oy,oz = self.getCirOrig()
        x1,y1,z1 = self.getPxyz(self.p1)
        return math.sqrt((x1-ox)**2+(y1-oy)**2+(z1-oz)**2)

    def point3vt(self,t_cur,t_total):
        l_13 = line3(self.p1,self.p2)
        length_l_13 = l_13.getLength()
        angle_13 = 2*math.asin(length_l_13/2/self.getRadius())
        w_13 = angle_13/t_total
        




p1 = point3(10,10,0)
p2 = point3(10,0,10)
p3 = point3(10,-10,0)

arc = arc3(p1,p2,p3)
arc.getCirOrig()

<<<<<<< HEAD
# a,b,r = calCirPara(p1=p1,p2=p2,p3=p3)
p1 = point3(34.9148,3.21214,300.226)
p2 = point3(34.9148,14.2698,206.491)
p3 = point3(34.9148,13.8740,115.299)
=======
print(f"x={arc.ox},y={arc.oy},z={arc.oz},R={arc.getRadius()}")
    
line_p1_p2 = line3(p1,p2)
>>>>>>> 71498462bd09a8ba5268f9cd0c09f52c85bd16f3

lp = line_p1_p2.point3vt(1,2)

print(f"{lp.x},{lp.y},{lp.z}")

lp = line_p1_p2.point3vt(1.5,2)

print(f"{lp.x},{lp.y},{lp.z}")