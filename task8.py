'''
Generate a list of words related to daily activities
Using the list of words, calculate the length of each word.
Using the word lengths, classify each word as Short (length < 5) or Long (length ≥ 5) and display the results.
'''
def main():
    daily_activities = ["eat", "sleep", "code", "exercise", "read", "write", "shop", "travel"]
    for activity in daily_activities:
        length = len(activity)
        if length < 5:
            classification = "Short"
        else:
            classification = "Long"
        print(f"Activity: {activity}, Length: {length}, Classification: {classification}")
if __name__ == "__main__":
    main()