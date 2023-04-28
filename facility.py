monthly_salary = input ("Enter the monthly salary:")
years_experienced = input ("Enter the years experienced:")
years_salary = sum = 12 * int(monthly_salary)
print(sum)

if int(years_salary) > 300000 and int(years_experienced) > 2:
    print("you qualify for the facility...")

else:
    print("you dont qualify for the facility...")