#An Electricity board charges:
# 5rs per unit for first 100 units
# 7rs per unit for remaining units
# take units as input and calculate the total bill.

unit=int(input("Enter the unit="))
if unit<=100:
    total=unit*5
    print(total)
else:
    total=(100*5)+((unit-100)*7)
    print(total)
    