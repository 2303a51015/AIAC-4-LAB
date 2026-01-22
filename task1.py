'''
write a python code to  check whearther the text is spam or not spam 
n=""Congratulations! You have won a free lottery ticket."
display as spam
'''
def check_spam(text):
    spam_keywords = ["Congratulations", "free", "lottery", "winner", "prize", "click here", "urgent"]
    text_lower = text.lower()
    for keyword in spam_keywords:
        if keyword.lower() in text_lower:
            return "spam"
    return "not spam"
n = "Congratulations! You have won a free lottery ticket."
result = check_spam(n)
print(result)
