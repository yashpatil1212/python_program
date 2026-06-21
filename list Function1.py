a=["yash","kuldip","gaurav","nitin","yash"]
print(a)
#to find the length of a list
print(len(a))

#to count an occurence of a particular element 
print(a.count("yash"))

#to add to the list
a.append("shivam")
print(a)

#to add to a specific location
a.insert(0,"chetan")
print(a)

#to remove from a list
a.remove("yash")
print(a)

#to remove from a certain location
print(a.pop(1))
print(a)