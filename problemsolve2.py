#1.Take an input from a user as a string then,reverse it.
print("***************Reverse String ************")
a=input("Enter anything string here: ")
print(a[::-1])

#2.write a program to check if a string contains only digits.
print("**************Digit check************")
a=input("Enter anything here: ")
b= (a.isdigit())
if b== True:
    print("it contain only digits,True ")
else:
    print("it does not contain only digits ,False")


#3.write a program to check if a string is palindrome.

print("***********String Palindrome*************")
a= input("Enter the any string here:")
rev = a[::-1]

if a==rev:
    print("It is Palindrome string ")
else:
    print("It is not palindrome string ")

