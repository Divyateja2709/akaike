import re
import requests
from bs4 import BeautifulSoup

# Noise patterns to clean extracted text
noise1 = re.compile(r"[([].*?[\)\]]\s+")  # Removes text within brackets
noise2 = re.compile(r"\{.*?\}")  # Removes content between {}
noise3 = re.compile(r"[a-zA-Z]")  # Removes English characters
noise4 = re.compile(r"[\{()#@:%,_;&!=}\]]")  # Removes unwanted symbols
noise5 = re.compile(r"[\?\]]")  # Removes extra question marks and brackets

def extract_text(url):
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the article text from the class containing content
        vistaar = soup.find(class_="article-desc ul_styling")
        if vistaar:
            vistaar = vistaar.text
        else:
            raise ValueError("No article content found on the page.")
    except Exception as e:
        print(f"Error fetching text: {e}")
        return ""

    # Clean and process the extracted text
    vistaar = vistaar.replace("विस्तार ", " ")
    vistaar = vistaar.replace("विज्ञापन", " ")
    vistaar = vistaar.replace("\n", " ")
    vistaar = re.sub("\xa0", " ", vistaar)
    vistaar = re.sub(noise1, " ", vistaar)
    vistaar = re.sub(noise2, " ", vistaar)
    vistaar = re.sub(noise3, " ", vistaar)
    vistaar = re.sub(noise4, " ", vistaar)
    vistaar = re.sub(noise5, " ", vistaar)
    vistaar = re.sub(" +", " ", vistaar).strip()

    return vistaar
