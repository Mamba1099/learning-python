def grade():
   get_mean(number)

number = int(input("Enter the mean: "))
   
def get_mean(number):
  if  number >= 80:
    print("Grade: A")
  elif number >= 70:
   print("Grade: B")
  elif number >= 60:
    print("Grade: C")
  else:
    print("Grade: F")



grade()    



   
