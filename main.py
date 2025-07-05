from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langdetect import detect
from googletrans import Translator
from pycountry import languages
import asyncio

app = Flask(__name__)
CORS(app)  # Allow all origins

translator = Translator()

def get_lang_code(name):
    lang = languages.get(name=name.lower())
    return lang.alpha_2 if lang and hasattr(lang, "alpha_2") else None

async def translate_text(input_text, src_lang, dest_lang):
    result = await translator.translate(input_text, src=src_lang, dest=dest_lang)
    return result.text
@app.get("/")
def home():
    return render_template("index.html")
@app.route("/translate", methods=["POST"])
def translate_route():
    data = request.get_json()
    text = data.get("text")
    target_lang = data.get("target_lang")
    
    if not text or not target_lang:
        return jsonify({"error": "Missing input"}), 400

    src_lang = detect(text)
    dest_lang = target_lang  # Already in 2-letter form from frontend

    translated_text = asyncio.run(translate_text(text, src_lang, dest_lang))
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
