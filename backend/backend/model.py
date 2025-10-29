
positive_words = [
    "good", "nice", "great", "beautiful", "handsome", "happy", "joyful", "cheerful",
    "excellent", "like", "bright", "positive", "wonderful", "pleasant", "satisfying",
    "amazing", "awesome", "smooth", "friendly", "cheerful", "successful", "superior",
    "smart", "cheerful", "glad", "brilliant", "fantastic", "favorite",
    "best", "excellent", "inspiring", "positive", "fine", "yes", "yeah", "do", 
]

negative_words = [
    "bad", "ugly", "angry", "sad", "hate", "disappointed", "heartbreaking", "dislike",
    "lazy", "tired", "frustrated", "failed", "troublesome", "headache", "messy", "scary",
    "annoying", "oppressive", "anxious", "worried", "severe", "unlucky", "harmful",
    "chaotic", "negative", "uncomfortable", "terrible", "late", "painful", "tragic", "fuck", 
    "shut up", "dirty", "bitch", "not", "no", "do not", "does not", "stupid", "dumb"
    
]
conjuction = ["and", "but", "if", "when"]


def analyze_sentiment(text: str):
    text_lower = text.lower()


    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)
    

    if pos_count > neg_count:
        label = "positive"
    elif neg_count > pos_count:
        label = "negative"
    else:
        label = "neutral"

    return {"label": label}

