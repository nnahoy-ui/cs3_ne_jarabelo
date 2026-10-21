class Student:


    def__init__(self, name, section, score):
        self.name = name
        self.section = section
        self.score = score

    def display_info(self):
        print("Student Name:", self.name)
        print("Student Section:", self.section)
        print("Student Score:", self.score)
        print("Pass/Fail", self.check_status())

    student1 = Student("Jarabelo", "Neon", 50)
    student2 = Student("Sapinosa", "Neon", 49)

    student1.display_info()
    student2.display_info()

    def check_status(self):
        if self.score >= 50:
            return "Passed"
        else:
            return "Failed"

student1_name = "Jarabelo"
student1_section = "Neon"
student_score = 50

student2_name = "Sapinosa"
student2_section = "Neon"
student2_score = 49

print("Student Name", student1_name)
print("Student Section", student1_section)
print("Student Score", student1_score)

print("Student Name", student2_name)
print("Student Section", student2_section)
print("Student Score", student2_score)

check_status(student1_score)
check_status(student2_score)

student_name = ["Jarabelo", "Sapinosa"]
student_score = [50, 49]