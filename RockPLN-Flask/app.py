from flask import Flask, render_template, request
import pickle
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import re, string

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Cargar stopwords y modelos
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words and word.isalpha()]
    return ' '.join(words)

# Cargar vectorizador
with open("modelos_guardados/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Diccionario de modelos
modelos = {
    'mlp': pickle.load(open("modelos_guardados/mlp.pkl", "rb"))
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    prob_rock = None
    prob_no_rock = None

    if request.method == "POST":
        lyrics = request.form["lyrics"]
        modelo_seleccionado = request.form["modelo"]

        cleaned = clean_text(lyrics)
        vectorized = vectorizer.transform([cleaned])

        modelo = modelos[modelo_seleccionado]
        prob = modelo.predict_proba(vectorized)[0]

        prediction = "Rock" if prob[1] > prob[0] else "No Rock"
        prob_rock = round(prob[1] * 100, 2)
        prob_no_rock = round(prob[0] * 100, 2)

    return render_template("index.html", prediction=prediction, prob_rock=prob_rock, prob_no_rock=prob_no_rock)

if __name__ == "__main__":
    app.run(debug=True)
