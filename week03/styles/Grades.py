# Grades
grade=input("What is the grade of the paper?")
grade=float(grade)
if grade>=90:
    letter_grade="A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70 :
    letter_grade="C"
elif grade >= 60 :
    letter_grade="D"
else :
    letter_grade="F"
last_digit=grade%10
# decide whether to add a "+" or "-"
tag_on = ""
if grade>59 and grade < 90 :
    if last_digit >= 7 :
        tag_on = "+"
            
    if last_digit <=3 :
        tag_on="-"
if grade >= 70 :
    print(f"You have earned a {letter_grade}{tag_on} and passed the course!")
else :
    print("You have failed the course.  Please take it again.")