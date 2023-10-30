list1=[1,3,5,7]
list2=[2,4,6,8,10]
print("List 1:",list1)
print("List 2",list2)
print("Length of list 1:",len(list1))
print("Length of list 2:",len(list2))
if len(list1)==len(list2):
    print("List have same length ")
else:
     print("Length is not same")
print("Sum of list 1=",sum(list1))
print("Sum of list 2=",sum(list2))
if sum(list1)==sum(list2):
    print("Sum of two list are same")
else:
    print("Sum of  list  not same")
check = any(item in list1 for item in list2)
print("any value occur in both : ", check)

