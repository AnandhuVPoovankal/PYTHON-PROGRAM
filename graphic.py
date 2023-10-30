from program32.circle import*
from program32.rectangle import*
from program32.dgraphics.cuboid import*
from program32.dgraphics.sphere import*
r=int(input("Enter the radios:"))
carea(r)
cperi(r)
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rarea(l,b)
rperi(l,b)
l=int(input("Enter the length of cuboid:"))
b=int(input("Enter the breadth of cuboid:"))
h=int(input("Enter the heigth of cuboid:"))
cubarea(l,b,h)
cubperi(l,b,h)
r=int(input("Enter the radious of sphere:"))
spharea(r)
sphperi(r)