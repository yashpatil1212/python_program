#endswith()- Returns True if the string ends with the specified value, otherwise False.
a="Harry Potter"
print(a.endswith("r"))

#startswith()- Returns True if the string starts with the specified value, otherwise False.

print(a.startswith("H"))

#swapcase()-Swaps cases,lower case becomes upper case and vice versa.
print(a.swapcase())
#strip()-Returns a trimmed version of the string.(remove extra spaces )
print(a.strip())

#split()-Splits the string at the specified separator, and returns a list.
b="hello. my name is yash . i am 21 years old "
print(a.split(" "))
print(b.split("."))

#ljust()-Returns a left justified version of the string, 

print(a.ljust(20,"*"))
#rjust()-Returns a right justified version of the string,
print(a.rjust(20,"*"))

#replace()-Returns a string where a specified value is replaced with a specified value.
print(a.replace("Harry Potter","Yash"))

#rindex()-Searches the string for a specified value and returns the position of where it was found.
print(a.rindex("r"))

#rfind()-Searches the string for a specified value and returns the last position of where it was found. Returns -1 if the value is not found.
print(a.rfind("er"))

