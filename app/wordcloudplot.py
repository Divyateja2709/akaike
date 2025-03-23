import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from indicnlp.tokenize import indic_tokenize

def plot_wordcloud(input_text):
    # Clean unwanted symbols and extra spaces
    cleantext = re.sub("।", " ", input_text)
    cleantext = re.sub("'", " ", cleantext)
    cleantext = re.sub(" +", " ", cleantext)

    # Tokenize Hindi text using Indic NLP
    def tokenization(indic_string):
        tokens = []
        for t in indic_tokenize.trivial_tokenize(indic_string):
            tokens.append(t)
        return tokens

    # Stopwords to remove common Hindi words
    stopwords_hi = [
        'तुम', 'मेरी', 'मुझे', 'क्योंकि', 'हम', 'प्रति', 'अबकी', 'आगे', 'माननीय', 'शहर', 'बताएं', 'कौनसी',
        'क्लिक', 'किसकी', 'बड़े', 'मैं', 'रही', 'आज', 'लें', 'आपके', 'मिलकर', 'सब', 'मेरे', 'जी', 'श्री', 'वैसा',
        'आपका', 'अंदर', 'अत', 'अपना', 'अपनी', 'अपने', 'अभी', 'आदि', 'आप', 'इत्यादि', 'इन', 'इनका', 'इन्हीं', 'इन्हें',
        'इन्हों', 'इस', 'इसका', 'इसकी', 'इसके', 'इसमें', 'इसी', 'इसे', 'उन', 'उनका', 'उनकी', 'उनके', 'उनको', 'उन्हीं',
        'उन्हें', 'उन्हों', 'उस', 'उसके', 'उसी', 'उसे', 'एक', 'एवं', 'एस', 'ऐसे', 'और', 'कई', 'कर', 'करता', 'करते',
        'करना', 'करने', 'करें', 'कहते', 'कहा', 'का', 'काफ़ी', 'कि', 'कितना', 'किन्हें', 'किन्हों', 'किया', 'किर',
        'किस', 'किसी', 'किसे', 'की', 'कुछ', 'कुल', 'के', 'को', 'कोई', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जा',
        'जितना', 'जिन', 'जिन्हें', 'जिन्हों', 'जिस', 'जिसे', 'जीधर', 'जैसा', 'जैसे', 'जो', 'तक', 'तब', 'तरह', 'तिन',
        'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'तो', 'था', 'थी', 'थे', 'दबारा', 'दिया', 'दुसरा', 'दूसरे', 'दो', 'द्वारा',
        'न', 'नहीं', 'ना', 'निहायत', 'नीचे', 'ने', 'पर', 'पहले', 'पूरा', 'पे', 'फिर', 'बनी', 'बही', 'बहुत', 'बाद',
        'बाला', 'बिलकुल', 'भी', 'भीतर', 'मगर', 'मानो', 'मे', 'में', 'यदि', 'यह', 'यहाँ', 'यही', 'या', 'यिह', 'ये',
        'रखें', 'रहा', 'रहे', 'ऱ्वासा', 'लिए', 'लिये', 'लेकिन', 'व', 'वर्ग', 'वह', 'वहाँ', 'वहीं', 'वाले', 'वुह', 'वे',
        'वग़ैरह', 'संग', 'सकता', 'सकते', 'सबसे', 'सभी', 'साथ', 'साबुत', 'साभ', 'सारा', 'से', 'सो', 'ही', 'हुआ', 'हुई',
        'हुए', 'है', 'हैं', 'हो', 'होता', 'होती', 'होते', 'होना', 'होने'
    ]

    # Cleaned and tokenized text excluding stopwords
    clean_tokens = [i for i in tokenization(cleantext) if i not in stopwords_hi]

    # Font path for rendering Hindi words correctly
    font = "app/gargi.ttf"

    # Create a dictionary of word frequencies
    dictionary = Counter(clean_tokens)

    # Generate WordCloud from word frequencies
    wordcloud = WordCloud(
        width=1000, height=700,
        background_color="white", colormap="Paired",
        min_font_size=10, font_path=font
    ).generate_from_frequencies(dictionary)

    # Plotting the WordCloud
    fig = plt.figure(figsize=(12, 8), facecolor="white")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=4)
    plt.close()

    return fig
