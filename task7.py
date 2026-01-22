'''
generate a list of student names and store it in a variable.
traverse the list and reverse each name using a loop.
if the reversed name is the same as the original name, print that the name is a palindrome.
otherwise, print that it is not a palindrome.
'''
def main():
    student_names = ["Anna", "Bob", "naman", "karan", "sultan", "Hannah"]
    for name in student_names:
        reversed_name = name[::-1]
        if name.lower() == reversed_name.lower():
            print(f"{name} is a palindrome.")
        else:
            print(f"{name} is not a palindrome.")
if __name__ == "__main__":
    main()