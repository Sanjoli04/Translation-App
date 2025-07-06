from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langdetect import detect
from pycountry import languages
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)

def get_lang_code(name):
    lang = languages.get(name=name.lower())
    return lang.alpha_2 if lang and hasattr(lang, "alpha_2") else None

@app.route("/languages")
def languages():
    codes = [
        {"code": lang.alpha_2, "name": lang.name}
        for lang in pycountry.languages
        if hasattr(lang, "alpha_2")
    ]
    return jsonify(sorted(codes, key=lambda x: x["name"]))

@app.route("/translate", methods=["POST"])
def translate_route():
    data = request.get_json()
    text = data.get("text")
    target_lang = data.get("target_lang")

    if not text or not target_lang:
        return jsonify({"error": "Missing input"}), 400

    detected_lang = detect(text)

    try:
        translated_text = GoogleTranslator(source=detected_lang, target=target_lang).translate(text)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
