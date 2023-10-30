fruits={'Apple':2,'Orange':14,'Watermelon':61,'Grapes':10}
print(fruits)
l=list(fruits.items())
l.sort()
print("Ascendind order is:",l)
l=list(fruits.items())
l.sort(reverse=True)
print("Dscending order is:",l)