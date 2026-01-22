'''
read persons age.
if he above 18 then he is eligible to vote.
if he is below 18 then he is not eligible to vote.
'''
def main():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        elif 0 <= age < 18:
            print("You are not eligible to vote.")
        else:
            print("Invalid age! Age cannot be negative.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
if __name__ == "__main__":
    main()
    