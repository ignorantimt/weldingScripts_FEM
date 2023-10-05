import math

class point2:
    def __init__(self,a,b):
        self.x = a
        self.y = b

    def calCirPara(p1,p2,p3):
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y
        x3 = p3.x
        y3 = p3.y
        Ap1 = x1+x2
        Bp1 = y1+y2
        An1 = x1-x2
        Bn1 = y1-y2
        Ap2 = x2+x3
        Bp2 = y2+y3
        An2 = x2-x3
        Bn2 = y2-y3
        k1 = (Ap1 + Bp1*Bn1/An1)/2
        k2 = -Bn1 / An1
        k3 = (Ap2 + Bp2*Bn2/An2)/2
        k4 = -Bn2 / An2
        b = (k3-k1)/(k2-k4)
        a = k1+k2*b
        r = math.sqrt((a-x1)*(a-x1)+(b-y1)*(b-y1))

        return a,b,r

class point3:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
    
    def calCirPara(self,p1,p2,p3):
        x1 = p1.x
        y1 = p1.y
        z1 = p1.z
        x2 = p2.x
        y2 = p2.y
        z2 = p2.z
        x3 = p3.x
        y3 = p3.y
        z3 = p3.z

        a1 = (y1*z2 - y2*z1 - y1*z3 + y3*z1 + y2*z3 - y3*z2)
        b1 = -(x1*z2 - x2*z1 - x1*z3 + x3*z1 + x2*z3 - x3*z2)
        c1 = (x1*y2 - x2*y1 - x1*y3 + x3*y1 + x2*y3 - x3*y2)
        d1 = -(x1*y2*z3 - x1*y3*z2 - x2*y1*z3 + x2*y3*z1 + x3*y1*z2 - x3*y2*z1)

        a2 = 2 * (x2 - x1);
        b2 = 2 * (y2 - y1);
        c2 = 2 * (z2 - z1);
        d2 = x1 * x1 + y1 * y1 + z1 * z1 - x2 * x2 - y2 * y2 - z2 * z2

        a3 = 2 * (x3 - x1);
        b3 = 2 * (y3 - y1);
        c3 = 2 * (z3 - z1);
        d3 = x1 * x1 + y1 * y1 + z1 * z1 - x3 * x3 - y3 * y3 - z3 * z3

        self.x = -(b1*c2*d3 - b1*c3*d2 - b2*c1*d3 + b2*c3*d1 + b3*c1*d2 - b3*c2*d1)/(a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1)
        self.y =  (a1*c2*d3 - a1*c3*d2 - a2*c1*d3 + a2*c3*d1 + a3*c1*d2 - a3*c2*d1)/(a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1)
        self.z = -(a1*b2*d3 - a1*b3*d2 - a2*b1*d3 + a2*b3*d1 + a3*b1*d2 - a3*b2*d1)/(a1*b2*c3 - a1*b3*c2 - a2*b1*c3 + a2*b3*c1 + a3*b1*c2 - a3*b2*c1)





# p1 = point2(3.21214,300.226)
# p2 = point2(14.2698,206.491)
# p3 = point2(13.8740,115.299)

# a,b,r = calCirPara(p1=p1,p2=p2,p3=p3)
p1 = point3(34.9148,3.21214,300.226)
p2 = point3(34.9148,14.2698,206.491)
p3 = point3(34.9148,13.8740,115.299)

o = point3(0,0,10)
o.calCirPara(p1,p2,p3)

print(f"{o.x},{o.y},{o.z}")
    