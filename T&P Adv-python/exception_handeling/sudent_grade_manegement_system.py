grades = {"S001": 85, "S002": 92}

def update_grade(student_id, grade_input):
    try:
        if not student_id in grades:
            raise KeyError(f"Student ID {student_id} not found.") 
        
        if grade_input == "":
            raise ValueError("Grade input cannot be empty.") 
            
        new_grade = float(grade_input)
        grades[student_id] = new_grade
        print(f"Update successful for {student_id}.")
    except KeyError as e:
        print(f"ID Error: {e}")
    except ValueError:
        print("Input Error: Please enter a valid numeric grade.") 

update_grade("S003", "90") 
update_grade("S001", "abc") 