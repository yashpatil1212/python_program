#Iteration Using for loop
a=["yash","gaurav","nitin","kuldip"]
for i in a:
    print(i)

#Iteration Using For loop with Range and Length Function
a=["yash","gaurav","nitin","kuldip"]
for i in range(len(a)):
    print(a[i])

#Iteration Using While loop
a=["yash","gaurav","nitin","kuldip"]
i=0
while i<len(a):
    print(a[i])
    i+=1

#Using Short -Hand for Loop
a=["yash","gaurav","nitin","kuldip"]
[print(i)for i in a ]