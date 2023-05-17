class Student:
  def __init__(self, name, house, patronus):
        if not name:
          raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
          raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
        
  def __str__(self):
     return f"{self.name} from {self.house} owning a {self.patronus}" 
  def charm(self):
     match self.patronus:
         case "Stag":
             return "🐴"
         case "Otter":
             return "🐌"
         case "jack Russel Terrier":
              return "🐶"
         case _:
             return "🪄"

 
def main():
 student = get_student()
 print("Expecto patronum!")
 print(student.charm())



def get_student():
 name = input("Name: ")
 house = input("House: ")
 patronus = input("Patronus:")
 student = Student(name, house, patronus)

 return student


if __name__ == "__main__":
    main()


