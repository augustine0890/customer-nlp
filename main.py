from transformers import pipeline

classifier = pipeline("sentiment-analysis")
sentiment = classifier("Do you know guys what is problem of the game now? too many stuff to do before earning on the game, 1st need game account next Portis wallet then NFT next Need KYC last  need Game Pass in season server, this is easy for old player but how about new player?")
# [{'label': 'POSITIVE', 'score': 0.99}
print(sentiment[0])

classifier = pipeline("summarization")
summarization = classifier(
    "good day sir Did you fix the problem about item manager on weekly rewards daily rewards who did not received PLa awrds even thier item manager was already KyC verified? Today i still not recieved my awards from january 16-19 please sir fix this problem😓Thanks")
print(summarization[0])
