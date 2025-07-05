# 🌍 Smart Language Translator (Full Stack App)

This is a full-stack web application that detects the language of user input and translates it into a user-selected language using Google Translate API. It includes:

- ✅ Automatic language detection
- ✅ Intelligent language selection (even with misspellings)
- ✅ Full stack: Python (Flask) backend + HTML/Tailwind frontend
- ✅ Single deployment (no CORS issues)

---

## 🚀 Features

- Detects the input language using `langdetect`
- Converts language names to ISO 639-1 codes using `pycountry`
- Translates using `deep-translator`
- Dynamically loads language list on the frontend using `iso-639-1` via Skypack CDN
- Backend and frontend are served together via Flask

---

## 🛠️ Tech Stack

| Layer        | Tech                       |
|--------------|----------------------------|
| Backend      | Python, Flask, googletrans |
| Frontend     | HTML, Tailwind CSS         |
| Language Map | pycountry, iso-639-1       |
| Deployment   | Render / Railway / Local   |

---

## 📁 Project Structure
```
your_project/
│
├── main.py # Flask backend
├── templates/
│ └── index.html # Frontend HTML
├── static/ # (optional: custom CSS/JS)
├── requirements.txt # Python dependencies
└── README.md # You're here!
```
---

## ▶️ How to Run Locally

```bash
git clone https://github.com/yourusername/translator-app.git
cd translator-app

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python main.py
```
- Then open http://localhost:5000 in your browser.
## 📦 Requirements
```txt
Flask
flask-cors
langdetect
googletrans==4.0.0-rc1
pycountry
```
---
## 🌐 Deployment
You can deploy it to:
- Render (recommended)
- Railway
- Fly.io
`No CORS issues since backend serves the frontend directly.`
---
## 💡 Future Improvements
- Add speech-to-text and text-to-speech
- Improve fuzzy matching for misspelled languages
- Add dark mode and animations
✨ Live Demo
🔗 Demo Link

🧑‍💻 Author
Made For Fun by Sanjoli Vashisth
---
Let me know if you'd like to generate a matching `requirements.txt`, add screenshots, or write a one-liner description for LinkedIn/GitHub bio: [add project screenshots](f).
