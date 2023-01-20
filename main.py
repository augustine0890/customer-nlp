from transformers import pipeline

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
TWITTER_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"

sentiment_classifier = pipeline("sentiment-analysis", model=MODEL)

text_one = "@Corrie_PlayDapp what about the use of bamboo juice??? when will we have rising star Mikey?"
text_two = "Do you know guys what is problem of the game now? too many stuff to do before earning on the game, 1st need game account next Portis wallet then NFT next Need KYC last  need Game Pass in season server, this is easy for old player but how about new player?"
sentiment = sentiment_classifier(text_one)
# [{'label': 'POSITIVE', 'score': 0.99}
print(sentiment[0])

summarization_classifier = pipeline("summarization")
summarization = summarization_classifier(
    "good day sir Did you fix the problem about item manager on weekly rewards daily rewards who did not received PLa awrds even thier item manager was already KyC verified? Today i still not recieved my awards from january 16-19 please sir fix this problem😓Thanks")
# print(summarization[0])
