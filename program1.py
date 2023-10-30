s=int(input("Enterr staring year:"))
e=int(input("Enter ending year:"))
for i in range(s,e):
    if (i%4==0)and (i%100!=0) or (i%400==0):
     print(i)