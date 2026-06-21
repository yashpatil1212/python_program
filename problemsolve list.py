#a=["rose","rachel","monica","joe"]
a=["rose","rachel","monica","joe"]
print(a)
#write a program to swap first and fourth element.
a[0],a[3]=a[3],a[0]
print(a)

#write a program to add a new value at second position.
a.insert(1,"sunflower")
print(a)

#write a program to delete a value from 3rd position.
a.pop(2)
print(a)

#B=[13,7,12,10]
#write a program to multiply all the numbers in the list.
b=[13,7,12,10]
print(b)
mul=1

for i in (b):
    mul*=i
print("multiplication of b list=",mul)

#write a program to get the largest number from the list.
b=[13,7,12,10]
b.sort()
print(b)
print("The largest value in the list is ",b[-1])

#write a program to get the smallest number from the list. 
b.sort
print(b)
print("The smallest value in the list is ",b[0])