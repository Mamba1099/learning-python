def main():
    number = get_number()
    ouch(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n >0:
            break


    return n    

        

def ouch(n):
    for _ in range(n):
        print("ouch")

            
main()