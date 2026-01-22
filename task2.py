'''
generate a python code if it contains emotioms as['happy', 'sad', 'angry', 'excited','nervous','neutral']
input write any sentence and the code will identify the emotion from the list and print it out.
'''

def identify_emotion(sentence):
    # Define keywords for each emotion
    emotion_keywords = {
        'happy': ['joy', 'pleased', 'delighted', 'content', 'cheerful'],
        'sad': ['unhappy', 'sorrowful', 'dejected', 'downcast', 'mournful'],
        'angry': ['mad', 'furious', 'irate', 'livid', 'outraged'],
        'excited': ['thrilled', 'elated', 'eager', 'enthusiastic', 'overjoyed'],
        'nervous': ['anxious', 'tense', 'apprehensive', 'uneasy', 'worried'],
        'neutral': ['calm', 'indifferent', 'unemotional', 'detached', 'impartial']
    }

    # Check for specific keywords in the sentence
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in sentence.lower():
                return emotion
    return "neutral"

# Example usage
input_sentence = "I am feeling very joyful and delighted today!"
detected_emotion = identify_emotion(input_sentence)
print(detected_emotion)
# Example usage
input_sentence = "I am nervous today!"
detected_emotion = identify_emotion(input_sentence)
print(detected_emotion)
