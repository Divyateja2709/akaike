import re
from extractdata import extract_text
from wordcloudplot import plot_wordcloud
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Function to clean text and remove extra spaces and newlines
WHITESPACE_HANDLER = lambda k: re.sub(r'\s+', ' ', re.sub(r'\n+', ' ', k.strip()))

def summarize(input_, model):
    # Check if the input is a URL or plain text
    if input_.startswith("https://"):
        text = extract_text(input_)
    else:
        text = input_

    # Model selection
    if model == "T5":
        checkpoint = "csebuetnlp/mT5_multilingual_XLSum"
    elif model == "BART":
        checkpoint = "ai4bharat/IndicBART"
    else:
        raise ValueError("Invalid model selected. Choose between 'T5' or 'BART'.")

    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

    # Tokenize input and prepare for model inference
    input_ids = tokenizer(
        [WHITESPACE_HANDLER(text)],
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=512
    )["input_ids"]

    # Generate summary with constraints
    output_ids = model.generate(
        input_ids=input_ids,
        max_length=70,
        min_length=30,
        no_repeat_ngram_size=2,
        num_beams=4
    )[0]

    # Decode the generated summary
    summary = tokenizer.decode(
        output_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )

    # Generate the word cloud for visualization
    figure = plot_wordcloud(text)

    return summary, figure
