
monthly_salary = input("Enter the monthly salary:")
years_experienced = input("Enter the years experienced:")
years_salary = 0.00


def my_calculations():  
    years_salary=  12 * int(monthly_salary)
    return(years_salary)
my_calculations()

def my_statement():
    if int(years_salary) > 300000 and int(years_experienced) > 2:
         print("you qualify for the facility...")

    else:
         print("you dont qualify for the facility...")
my_statement()

