# mark = int(input("Enter your Marks : "))
# if mark < 0 or mark > 100:
#     print("Invalid score! Score must be between 0 and 100.")
# if mark>=80:
#     print(f"You got A+" )
# elif mark>=70:
#     print(f"You got A" )
# elif mark>=60:
#     print(f"You got A-" )
# elif mark>=50:
#     print(f"You got B" )
# elif mark>=40:
#     print(f"You got C" )
# elif mark>=33:
#     print(f"You got D" )
# elif mark<=32:
#     print(f"You fail in the exam ")
def calculate_grade_point(score):
    if score < 0 or score > 100:
        return "Invalid score! Score must be between 0 and 100."
    
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0

# Example usage
score = float(input("Enter your score (0-100): "))
grade_point = calculate_grade_point(score)
print(f"Your grade point is: {grade_point}")
