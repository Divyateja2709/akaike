Here’s a **detailed explanation** of how the project works along with **instructions** on how to run it on your computer. 🚀

---

## 📝 **Project Overview**

### 🎯 **Objective**
The project aims to **summarize Hindi news articles** by extracting content from supported websites and generating concise summaries using state-of-the-art models like:

- **BART:** Fine-tuned for Hindi text summarization.
- **mT5:** A multilingual model that supports Hindi summarization.

---

## ⚙️ **How It Works**

### 1. **Input: News Article URL**
- The user provides a URL of a news article (e.g., from [Amarujala](https://www.amarujala.com)).
- The URL is passed to the API.

---

### 2. **API Endpoint**
- The API endpoint accepts the URL and a model name (`BART` or `T5`).
- API Endpoint:
```
https://hf.space/embed/d0r1h/Hindi_News_Summarizer/+/api/predict/
```

---

### 3. **Fetching and Preprocessing**
- The system scrapes the news article content.
- Cleans and preprocesses the text to remove unwanted elements like ads, HTML tags, and irrelevant sections.

---

### 4. **Summarization Model**
- The preprocessed text is passed to the selected model (`BART` or `T5`).
- The model generates a concise summary of the article in Hindi.

---

### 5. **Sentiment Analysis (Optional)**
- Sentiment analysis is performed to classify the summary as **Positive**, **Negative**, or **Neutral**.

---

### 6. **WordCloud Generation (Optional)**
- A word cloud is generated from the summarized text to visualize key topics.

---

### 7. **Output**
- The final output includes:
  - Title
  - Summary
  - Sentiment
  - Key Topics
  - Optional: WordCloud Visualization

---

## 🖥️ **How to Run the Project Locally**

---

### ✅ **Step 1: Clone the Repository**

```bash
git clone https://github.com/Divyateja2709/akaike.git
```

---

### ✅ **Step 2: Navigate to Project Directory**

```bash
cd akaike
```

---

### ✅ **Step 3: Create a Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

---

### ✅ **Step 4: Install Required Dependencies**

```bash
pip install -r requirements.txt
```

---

### ✅ **Step 5: Run the Application**

```bash
python app.py
```

---

### ✅ **Step 6: Access the Application**

- Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🔥 **API Usage Instructions**

### 1. **Send POST Request to API**

```python
import requests

# API endpoint
api_endpoint = "https://hf.space/embed/d0r1h/Hindi_News_Summarizer/+/api/predict/"

# News article URL
news_url = "https://www.amarujala.com/uttar-pradesh/shamli/up-news-heroin-caught-in-shaheen-bagh-of-delhi-is-connection-to-kairana-and-muzaffarnagar?src=tlh\u0026position=3"

# API Request
response = requests.post(
    url=api_endpoint,
    json={"data": [news_url, "BART"]}
)

# Get the summarized output
summary = response.json()['data'][0]
print(summary)
```

---

## 🎨 **WordCloud Usage**

To generate a **WordCloud** for summarized Hindi text:

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_wordcloud(text):
    wordcloud = WordCloud(font_path='path_to_hindi_font.ttf', width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Generate WordCloud for the summarized text
plot_wordcloud(summary)
```

---

## 📚 **Troubleshooting and Notes**

- Make sure Python version >= 3.8 is installed.
- Verify that all dependencies from `requirements.txt` are installed properly.
- If facing issues, deactivate the virtual environment and reactivate it:
```bash
# Deactivate
deactivate

# Activate again
venv\Scripts\activate
```

---

## 🎉 **Done!**
Now the application is running locally, and you can start summarizing Hindi news articles. 🚀
