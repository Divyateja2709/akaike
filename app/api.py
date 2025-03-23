from flask import Flask, request, jsonify
from summarizer import summarize
from sentiment import analyze_sentiment
from tts import generate_tts

app = Flask(__name__)

@app.route('/api/summarize', methods=['POST'])
def summarize_news():
    data = request.json
    text = data.get('text')
    model = data.get('model', 'BART')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    summary, wordcloud = summarize(text, model)
    return jsonify({'summary': summary})

@app.route('/api/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    sentiment = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})

@app.route('/api/tts', methods=['POST'])
def tts_generation():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    audio_path = generate_tts(text)
    return jsonify({'audio_path': audio_path})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
