#  Q. A collage  stores  student name,roll number and 
# marks in three subjects. 
# Write a program to calculate the total ,average,and display whether student pass(average>=40)

std_name = input("Enter name=")
std_roll_number = int(input("Enter roll number ="))
sub1 = int(input("enter marks of sub 1="))
sub2 = int(input("enter marks of sub 2="))
sub3 = int(input("enter marks of sub 3="))

total = sub1 + sub2 + sub3
average = total/3


print("Student name:",std_name)
print("Roll no:",std_roll_number)
print("Total marks:",total)
print("Average of marks:",average)

if average>=40:
    print("student passed")
else:
    print("fail")    

