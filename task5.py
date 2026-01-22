'''
read the students marks as input.
validate the marks to be between 0 and 100.
students with marks greater than or equal to 40 are considered pass, otherwise fail.
'''
def validate_marks(marks):
    if 0 <= marks <= 100:
        return True
    else:
        return False
def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
def main():
    try:
        marks = float(input("Enter the student's marks (0-100): "))
        if validate_marks(marks):
            result = check_pass_fail(marks)
            print(f"The student has: {result}")
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
if __name__ == "__main__":
    main()
    
    