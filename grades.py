print("Grading system form 3 and 4")

math_pp1 = float(input("Maths paper1:"))
math_pp2 = float(input("Maths paper 2:"))
math_total = (math_pp1 + math_pp2) /200 *100
print("Math:", + float(math_total))


english_pp1 = float(input("english_pp1(marks out of 60):"))
english_pp2 = float(input("english_pp2(marks out of 80):"))
english_pp3 = float(input("english_pp3(marks out of 60):"))
english_total = (english_pp1 + english_pp2 + english_pp3) / 200 *100
print("English:", + float(english_total))


kiswahili_pp1 = float(input("Kiswahili paper 1(marks out of 60):"))
kiswahili_pp2 = float(input("Kiswahili paper 2(marks out of 80):"))
kiswahili_pp3 = float(input("kiswahili paper 3(marks out of 60):"))
kiswahili_total = (kiswahili_pp1 + kiswahili_pp2 + kiswahili_pp3) /200 *100
print("Kiswahili:", + float(kiswahili_total))


chemistry_pp1 = float(input("chemistry paper 1(marks out of 80):"))
chemistry_pp2 = float(input("chemistry paper 2(marks out of 80):"))
chemistry_pp3 = float(input("chemistry paper 3(marks out of 40):"))
chemistry_total = ((chemistry_pp1 + chemistry_pp2) / 160 * 60) + chemistry_pp3
print("Chemistry:", + float(chemistry_total))


physics_pp1 = float(input("physics paper 1(marks out of 80):")) 
physics_pp2 = float(input("physics paper 2(marks out of 80):")) 
physics_pp3 = float(input("physics paper 3(marks out of 40):")) 
physics_total = ((physics_pp1 + physics_pp2) /160 * 60) + physics_pp3 
print("Physics:", + float(physics_total)) or None


biology_pp1 = float(input("biology paper 1(marks out of 80):")) 
biology_pp2 = float(input("biology paper 2(marks out of 80):")) 
biology_pp3 = float(input("biology paper 3(marks out of 40):")) 
biology_total = ((biology_pp1 + biology_pp2) / 160 * 60) + biology_pp3 
print("Biology:", + float(biology_total)) or None


geography_pp1 = float(input("geography paper 1(marks out of 100):")) 
geography_pp2 = float(input("geography paper 2(marks out of 100):")) 
geography_total = (geography_pp1 + geography_pp2) / 2 
print("Geography:", + float(geography_total)) or None


history_pp1 = float(input("history paper 1(marks out of 100):"))
history_pp2 = float(input("history paper 2(marks out of 100):"))
history_total = (history_pp1 + history_pp2) / 2
print("History:", + float(history_total)) or None

business_pp1 = float(input("business paper 1(marks out of 100):"))
business_pp2 = float(input("business paper 2(marks out of 100):"))
business_total = (business_pp1 + business_pp2) / 2
print("Business:", + float(business_total)) or None

home_science_pp1 = float(input("home science paper 1(marks out of 25):"))
home_science_pp2 = float(input("home science paper 2(marks out of 45):"))
home_science_pp3 = float(input("home science paper 3(marks out of 100):"))
home_science_total = (home_science_pp1 + home_science_pp2 + home_science_pp3) / 170 * 100
print("Home science:", + float(home_science_total)) or None


total_marks = math_total + english_total + kiswahili_total + chemistry_total + physics_total + biology_total + geography_total + history_total + business_total + home_science_total
n_of_subjects = float(input("subjects done:"))
mean = total_marks / n_of_subjects
print(mean)


#grade
if 100 < mean > 80:
    print("Grade: A")
 
elif 79 < mean > 75:
    print("Grade: A-")

elif 74 < mean > 70:
    print("Grade: B+")

elif 69 < mean > 65:
    print("Grade: B")

elif 64 < mean >60:
    print("Grade: B-")

elif 59 < mean > 55:
    print("Grade: C+")

elif 54 < mean > 50:
    print("Grade: C")

elif 49 < mean >45:
    print("Grade: C-")

elif 44 < mean > 40:
    print("Grade: D+")

elif 39 < mean >35:
    print("Grade: D")

elif 34 < mean > 30:
    print("Grade: D-")

else:
    print("Grade: E")                                        
