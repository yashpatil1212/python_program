
#An organization stores employee ID (int), name (string), basic salary (float), and overtime hours (int).
#  Rules: HRA = 18% of basic DA = 12% of basic Overtime = ₹250/hour If total salary > ₹1,00,000,
#  deduct 10% tax Write a program to calculate ne

ID=123
name="yash patil"
basic_salary=50000.0
overtime_hours=10
HRA=0.18*basic_salary
DA=0.12*basic_salary
overtime_pay=250*overtime_hours
total_salary=basic_salary+HRA+DA+overtime_pay
if total_salary > 100000:
    tax=0.10*total_salary
    net_salary=total_salary-tax
else:
    net_salary=total_salary
print("Employee ID:", ID)
print("Name:", name)
print("Basic Salary:", basic_salary)
print("HRA:", HRA)
print("DA:", DA)
print("Overtime Pay:", overtime_pay)
print("Total Salary:", total_salary)
print("Net Salary:", net_salary)
