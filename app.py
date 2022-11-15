from flask import Flask
from flask import *
app = Flask(__name__)

@app.route("/")
def homepage():
    name = "Andrew Salmeron"
    details = readDetails('static/description.txt')
    return render_template('aboutme.html', name = name, aboutMe=details)


@app.route("/")
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)
