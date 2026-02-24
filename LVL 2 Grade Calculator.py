#File Name - LVL 2 Grade Calculator
#Author - Oliver Culbert
#Date - Monday 16th of February 2026

#------LibaryImports------
import time

#------Variables-------
students = {}

#--------Functions------------
def letter_grade(score):
    if 85 <= score <= 100:
        return "E"
    elif 65 <= score < 85:
        return "M"
    elif 50 <= score < 65:
        return "A"
    elif 0 <= score < 50:
        return "N"
    else:
        print("Invalid Score Try again")

def get_score(prompt):
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
#-------Start-----------
loop = True

print("<<<Welcome To The GPA Calculator>>>")

while loop == True:
    print("What would you like to do")
    print("1: Add student and calculate GPA")
    print("2: Find a student and GPA")
    print("3: Exit")

    choice = input("Choose 1, 2 or 3:")

    if choice == "1":
        name = input("What is the students name")
        print("E = 85+, M = 65+, A = 50+, N = <50")
        one_score = get_score(f"What score did {name} get on assessment 1? ")
        two_score = get_score(f"What score did {name} get on assessment 2? ")
        three_score = get_score(f"What score did {name} get on assessment 3? ")
        four_score = get_score(f"What score did {name} get on assessment 4? ")

        average_score = (one_score + two_score + three_score + four_score) / 4

        final_grade = letter_grade(average_score)

        students [name.lower()] = {
            "Average": average_score,
            "Average Grade": final_grade
        }

        print(f"Average Score: {name} = {average_score}")
        print(f"Average Grade: {name} = {final_grade}")

        time.sleep(4.0)

    elif choice == "2":
        find_student = input("What is the name of the student you are trying to find?:")

        if find_student.lower() in students:
            print(f"Average Score: {students[find_student]['Average']}")
            print(f"Average Grade: {students[find_student]['Average Grade']}")
            time.sleep(3.0)
        else:
            print("Student not found, Try Again")

    elif choice == "3":
        print("Closing")
        loop = False

    else:
        print("Invalid Choice Try Again")