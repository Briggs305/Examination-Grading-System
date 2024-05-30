#Grading system of students
#Prompt the user to input thier score (1-100)
#Based on the score assign the letter grading using the following
#_A : 90-100
#_B : 80-89
#_C :70- 69
#_D : 60-59
#-F : 0-49

#Print out the user score along wit the corresponding letter (Grade)

#NAMING SYSTEM....
print ('Type name here to know your grade?')
Name = input ()

#Grading System

score = int (input("Enter your Score here"))

#cHECKING OF GRADES
if score >=90:
    grade = "A"
elif score >=80:
    grade ="B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade ="D"
elif score <=40:
    grade ="F"



if score <= 50:
 print ("Your grade is " + (grade) + str (Name) + "You need to work harder next semester")


elif score >= 51:
 print ("Gotcha!" + str (Name) )

#Print final Grade and Score

print ("Your Score is", score)
print ("Your Grade is", grade)
