class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def rectarea(self):
        self.area=self.l*self.b

    def  rectperi(self):
        self.peri=2*(self.l+self.b)

    def compare(self, r2):
        if self.area == r2.area:
            print("Area are equal!")
        elif self.area > r2.area:
            print("Area of 1st rectangle is greater!")
        else:
            print("Area of 2nd rectangle is greater!")
    def dispaly(self):
        print("Area of rectangle=",self.area)
        print("Peri meter of reactangle:",self.peri)

l1=int(input("Enter the  length of  rectangle1:"))
b1=int(input("Enter the height of rectangle1:"))
l2=int(input("Enter the length of rectangle2:"))
b2=int(input("Enter the height of  rectangle2:"))

r1=rect(l1,b1)
r1.rectarea()
r1.rectperi()
r2=rect(l2,b2)
r2.rectarea()
r2.rectperi()
r1.dispaly()
r2.dispaly()
r1.compare(r2)
