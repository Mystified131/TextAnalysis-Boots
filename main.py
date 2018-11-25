from flask import Flask, request, render_template, session
import datetime, os, cgi
from TextAnalysis import text_processor

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.urandom(24)

@app.route("/", methods=['POST', 'GET'])

def process():
    if request.method == 'GET':
        result = ""
        return render_template('index.html', result = result)
    if request.method == 'POST':
        textchunk = request.form["text"]
        result = text_processor(textchunk)
    return render_template('index.html', result = result)

## THE GHOST OF THE SHADOW ##

if __name__ == '__main__':
    app.run()
   