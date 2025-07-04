import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS

# Initialize translator
translator = Translator()

st.set_page_config(page_title="Language Translator", page_icon="🌍")
st.title("🌍 Free Language Translator App")

# Input text
text = st.text_area("Enter text to translate:")

# Language setup
language_names = [lang.title() for lang in LANGUAGES.values()]
lang_code_map = {lang.title(): code for code, lang in LANGUAGES.items()}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", language_names, index=language_names.index("English"))
with col2:
    target_lang = st.selectbox("Target Language", language_names, index=language_names.index("Spanish"))

# Translate button
if st.button("Translate"):
    try:
        src = lang_code_map[source_lang]
        tgt = lang_code_map[target_lang]
        result = translator.translate(text, src=src, dest=tgt)
        translated_text = result.text

        st.success("Translated Text:")
        st.text_area("Translation", translated_text, height=100)

        # Copy to clipboard
        st.markdown(f"""
        <button onclick="navigator.clipboard.writeText(`{translated_text}`)" 
                style="padding:10px;margin-top:10px;background:#4CAF50;color:white;border:none;border-radius:5px;">
            📋 Copy to Clipboard
        </button>
        """, unsafe_allow_html=True)

        # Text-to-speech
        tts = gTTS(text=translated_text, lang=tgt)
        tts.save("translated.mp3")
        st.audio("translated.mp3", format="audio/mp3")

    except Exception as e:
        st.error(f"Translation failed: {e}")
