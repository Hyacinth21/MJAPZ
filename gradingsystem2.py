import re

students = {}

def student_name():
    while True:
        name = input("Enter student name (Type 'Done' to finish): ").strip()
        if name.lower() == "done":
            return None
        elif re.match("^[A-Za-z ]+$", name):
            return name
        else:
            print("Invalid name. Please enter alphabetic characters only.")

def student_grade():
    while True:
        try:
            grade = float(input("Enter student grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def student_absent():
    while True:
        try:
            absent = int(input("Enter number of absences: "))
            if 0 <= absent <= 100:
                return absent
            else:
                print("Absences must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def student_remarks(grade, absent,):
       
    if 0 <= grade <= 60:
        grade_remark = "F"
    elif 60 < grade <= 69:
        grade_remark = "D"
    elif 70 <= grade <= 79:
        grade_remark = "C"
    elif 80 <= grade <= 89:
        grade_remark = "B"
    elif 90 <= grade <= 100:
        grade_remark = "A"
    else:
        grade_remark = "Invalid"

    match grade:
        case "A":
            final_remark = "EXCELENT"
        case "B": 
            final_remark = "GOOD JOB"
        case "C": 
            final_remark = "NEED IMPROVEMENT"
        case "D": 
            final_remark = "ON PROVATION"
        case "F": 
            final_remark = "FAILED"
            
    if grade_remark in ["A", "B", "C"] and absent < 5:
        final_remark = "PASS - GRADE AND ABSENT"
    elif grade_remark in ["F", "D"] and absent >= 5:
        final_remark = "FAILED - ABSENT AND GRADE"
    elif absent >= 5:
        final_remark = "FAILED - ABSENT"
    elif grade_remark in ["F", "D"]:
        final_remark = "FAILED - GRADE"
    else:
        final_remark = "PASS - GRADE AND ABSENT"

    return grade_remark, final_remark

def show_remarks():
    for name, data in students.items():
        grade = data['grade']
        absences = data['absent']
        grade_remark = data['grade_remark']
        final_remark = data['final_remark']
        

        print(f"Name: {name}")
        print(f"Grade: {grade} ({grade_remark})")
        print(f"Absences: {absences}")
        print(f"Result: {final_remark}")
        print("-" * 30)

def main():
    while True:
        name = student_name()
        if name is None:
            break  # 'Done' entered

        grade = student_grade()
        absent = student_absent()

        grade_remark, final_remark = student_remarks(grade, absent)

        students[name] = {
            'grade': grade,
            'absent': absent,
            'grade_remark': grade_remark,
            'final_remark': final_remark
        }

        # do-while loop 
        while True:
            cont = input("Do you want to add another student? (Y/N): ").strip().lower()
            if cont == 'n':
                # Use simulated switch-case
                action = "SHOW_REMARKS"
                match action:
                    case "SHOW_REMARKS":
                        show_remarks()
                        print("Thank you for using the grading system!")
                        return
            elif cont == 'y':
                break
            else:
                print("Invalid input. Please enter Y or N.")


main()
