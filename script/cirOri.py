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



p1 = point2(3.21214,300.226)
p2 = point2(14.2698,206.491)
p3 = point2(13.8740,115.299)


a,b,r = calCirPara(p1=p1,p2=p2,p3=p3)

print(f" (a,b):({a},{b}),\n R={r}")
    