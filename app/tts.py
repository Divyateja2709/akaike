from gtts import gTTS
import os

def generate_tts(text, lang='hi'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_path = "app/assets/audio/output.mp3"
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error generating TTS: {e}")
        return None
from gtts import gTTS
import os

def generate_tts(text, lang='hi'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_path = "app/assets/audio/output.mp3"
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error generating TTS: {e}")
        return None
