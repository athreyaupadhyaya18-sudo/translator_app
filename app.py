from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text_to_translate = request.form["text"]
        translated_text = GoogleTranslator(source='english', target='kannada').translate(text_to_translate)
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

