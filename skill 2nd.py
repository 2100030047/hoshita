class two:
    def rectangle(self,l,b):
        print("perimeter of rectangle is",2*(l+b))
        print("area of rectangle is",l*b)
    def triangle(self,a,b,c):
        print("perimeter of triangle is",a+b+c)
        print("height of traingle is",a+b+c/2)
        print("area of traingle is",0.5*b*(a+b+c/2))
    def circle(self,r):
        print("perimeter of circle is",2*3.14*r)
        print("area of circle is",3.14*r*r)
a=two();
a.rectangle(2,3)
a.triangle(1,3,2)
a.circle(4)