import gradio as gr
from summarizer import summarize

# Updated description and article with olive green color
description = """
<center>
<b style='color:#556B2F;'>Custom News Summarizer: Summarize Hindi News with SOTA models</b>
</center>
"""
article = "<p style='text-align: center; color:#556B2F;'> Developed for Hindi News Summarization </p>"

# Sample news article links
link1 = "https://www.amarujala.com/world/india-providing-dry-ration-packs"
link2 = "https://www.amarujala.com/lucknow/now-the-government-will-go"
link3 = "https://www.amarujala.com/india-news/supreme-court-cannot-give"

# Read the example file
with open("app/Example/File.txt", 'r', encoding="utf8") as f:
    text = f.read()

# Gradio interface with CSS applied
interface = gr.Interface(fn=summarize,
                         inputs=[gr.Textbox(lines=5,
                                            placeholder="Enter your text...",
                                            label='News Input'),
                                 gr.Radio(["T5", "BART"],
                                          type="value",
                                          label='Model')],
                         outputs=[gr.Textbox(label="Summary"),
                                  gr.Plot(label="WordCloud")],
                         title="Custom News Summarizer",
                         examples=[[link1, "BART"],
                                   [link2, "BART"],
                                   [link3, "BART"],
                                   [text, "BART"]],
                         description=description,
                         article=article,
                         css="app/assets/styles.css")

# Launch the application with the favicon
interface.launch(debug=True, favicon_path="app/assets/favicon.ico", share=False)
