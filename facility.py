import threading


monthly_salary = input("Enter the monthly salary:")
years_experienced = input("Enter the years experienced:")


def my_calculations():  
    years_salary = 12 * int(monthly_salary)
    print(years_salary)


    if int(years_salary) > 300000 and int(years_experienced) > 2:
         print("you qualify for the facility...")

    else:
         print("you dont qualify for the facility...")


my_calculations()


def my_thread():
    thread_1 = threading.Thread(target = my_calculations)

    thread_1.start()

my_thread()


