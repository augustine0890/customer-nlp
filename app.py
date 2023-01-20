from fastapi import Request, FastAPI
from transformers import pipeline

app = FastAPI()

BASE_SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
TWITTER_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
EMOTION_MODEL = "j-hartmann/emotion-english-distilroberta-base"


@app.get("/")
async def welcome() -> dict:
    return {"message": "The welcome message"}


@app.post("/sentiment")
async def sentiment(request: Request) -> dict:
    classifier = pipeline(
        "sentiment-analysis", model=TWITTER_MODEL)
    body = await request.json()
    text = body['text']
    results = classifier(text)
    # # [{'label': 'POSITIVE', 'score': 0.99}
    return results[0]


@app.post("/emotion")
async def emotion(request: Request) -> dict:
    classifier = pipeline(
        "text-classification", model=EMOTION_MODEL, top_k=1)
    body = await request.json()
    text = body['text']
    results = classifier(text)
    # print(results)
    return results[0][0]


@app.get("/summarization")
async def summarization() -> dict:
    classifier = pipeline("summarization")
    summarization = classifier("Paris is the capital and most populous city of France, \
        with an estimated population of 2,175,601 residents as of 2018, in an area of more than 105 square kilometres (41 square miles). \
        The City of Paris is the centre and seat of government of the region and province of Île-de-France, or Paris Region, \
        which has an estimated population of 12,174,880, or about 18 percent of the population of France as of 2017.")
    return summarization[0]
