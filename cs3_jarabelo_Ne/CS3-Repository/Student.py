def check_status(score):
    if score >= 50:
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