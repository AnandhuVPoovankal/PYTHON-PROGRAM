s1=(input("Enter a string:"))
firstchar=s1[0]
s1 = s1.replace(firstchar, '$')
s1 = firstchar+s1[1:]
print(s1)