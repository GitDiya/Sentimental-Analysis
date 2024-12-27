from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    polarity = None
    subjectivity = None
    classification = None

    if request.method == "POST":
        text = request.form.get('text')

        if text:
            # Perform sentiment analysis using TextBlob
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Classify sentiment based on polarity
            if polarity > 0:
                classification = 'Positive'
            elif polarity < 0:
                classification = 'Negative'
            else:
                classification = 'Neutral'

            sentiment_result = {
                'classification': classification,
                'polarity': polarity,
                'subjectivity': subjectivity
            }

    return render_template("index.html", sentiment_result=sentiment_result)

if __name__ == "__main__":
    app.run(debug=True)
