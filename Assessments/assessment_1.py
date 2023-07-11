eng = float(input("Enter your English score: "))
math = float(input("Enter your Mathematics score: "))
phy = float(input("Enter your Physics score: "))
chem = float(input("Enter your Chemistry score: "))
bio = float(input("Enter your Biology score: "))
com = float(input("Enter your Computer Science score: "))

def grade_average(*args):
    for i in args:
        total_grade = sum(i)
        length = len(i)
        average = round(total_grade / length)
        
        if average >= 90 and average <= 100:
            print("A")
        elif average >= 80 and average <= 89:
            print("B")
        elif average >= 70 and average <= 79:
            print("C")
        elif average >= 60 and average <= 69:
            print("D")
        else:
            print("F")

grade_average([eng, math, phy, chem, bio, com])

