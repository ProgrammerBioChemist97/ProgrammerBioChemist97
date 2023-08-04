import nltk

# Load the data
data = ["This is a great movie!", "I hate this movie!", "The movie was okay."]

# Create a sentiment analyzer
sentiment_analyzer = nltk.sentiment.SentimentAnalyzer()

# Analyze the sentiment of the text
for sentence in data:
    sentiment = sentiment_analyzer.polarity_scores(sentence)
    print(sentence, sentiment["positive"], sentiment["negative"])
