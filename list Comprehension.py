l1=[20,30,40,50]
l2=[]
for i in l1:
    if i>35:

        l2.append(i)
print(l1,"\n",l2)

l3=[i for i in l1 if i>35]#this is list Comprehension methods
print(l3)