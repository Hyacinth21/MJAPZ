class Student: 
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade  # Private attribute

    def get_grade(self):
        return self.__grade
     
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")
            
Student1 = Student("Mark", 90)
Student2 = Student("Reiley", 85)


print("Student 1 Info:")
Student1.get_grade()
print(f"Name: {Student1.name}, Grade: {Student1.get_grade()}")
print(input("Enter new grade for Student 1: "))
new_grade = int(input())
Student1.set_grade(new_grade)
print(Student1.set_grade(new_grade))
print("Student 2 Info:")
Student2.get_grade()    
print(f"Name: {Student2.name}, Grade: {Student2.get_grade()}")
print(input("Enter new grade for Student 2: "))
new_grade = int(input())
print(Student2.set_grade(new_grade))

