x = input("enter your name:")
english = int(input("enter the marks of english:"))
math = int(input("enter the marks of math:"))
physics = int(input("enter the marks of physics:"))
chemistry = int(input("enter the marks of chemistry:"))
computer_science = int(input("enter the marks of computer science:"))
totalmarks = english + math + physics + chemistry + computer_science
percentage = (totalmarks/500)*100
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "c+"
elif percentage >= 40:
    grade = "c"
else :
    grade = "fail! better luck for next time ."
print("your name is:",x)
print("total marks:",totalmarks)
print("total percentage:",percentage)
print("grade:",grade)

    
    