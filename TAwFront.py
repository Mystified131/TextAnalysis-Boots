from flask import Flask, request, render_template, session
import datetime, os, cgi
from flask_sqlalchemy import SQLAlchemy
from TextAnalysis import text_processor

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$APPSTotal'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

#This code sets up the model for the database

class APPSTotal(db.Model):
    sessiondata = db.Column(db.String(120), primary_key=True)

    def __init__(self, sessiondata):
        self.sessiondata = sessiondata

@app.route("/", methods=['POST', 'GET'])

def process():
    if request.method == 'GET':
        result = ""
        return render_template('index2.html', result = result)
    if request.method == 'POST':
        right_now = datetime.datetime.now().isoformat()
        list = []
        for i in right_now:
            if i.isnumeric():
                list.append(i)
        tim = "".join(list)
        sessiondata = tim + "_TextAnalysis"
        if len(sessiondata) > 119:
            sessiondata = sessiondata[:119]
        new_entry = APPSTotal(sessiondata)
        db.session.add(new_entry)
        db.session.commit()
        textchunk = request.form["text"]
        result = text_processor(textchunk)
    return render_template('index2.html', result = result)

## THE GHOST OF THE SHADOW ##