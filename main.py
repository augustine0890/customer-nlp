from transformers import pipeline

SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
TWITTER_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
EMOTION_MODEL = "j-hartmann/emotion-english-distilroberta-base"

text_one = "@Corrie_PlayDapp what about the use of bamboo juice??? when will we have rising star Mikey?"
text_two = "Do you know guys what is problem of the game now? too many stuff to do before earning on the game, 1st need game account next Portis wallet then NFT next Need KYC last  need Game Pass in season server, this is easy for old player but how about new player?"
text_three = "@Corrie_PlayDapp i have 3 completed transaction to buy tickets but it eats my gas fees and dont get the tickets or it deducts my pla"
# sentiment_classifier = pipeline("sentiment-analysis", model=SENTIMENT_MODEL)
# sentiment = sentiment_classifier(text_one)
# [{'label': 'POSITIVE', 'score': 0.99}
# print(sentiment[0])

emotion_classifier = pipeline(
    "text-classification", model=EMOTION_MODEL, top_k=1)
emotion = emotion_classifier(text_three)
print(emotion[0])

# summarization_classifier = pipeline("summarization")
# summarization = summarization_classifier(
# "good day sir Did you fix the problem about item manager on weekly rewards daily rewards who did not received PLa awrds even thier item manager was already KyC verified? Today i still not recieved my awards from january 16-19 please sir fix this problem😓Thanks")
# print(summarization[0])
