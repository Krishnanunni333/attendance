from flask import Flask, render_template, redirect
from flask import request
from flask_ngrok import run_with_ngrok
import os
import extract

UPLOAD_FOLDER = './upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CASES = [] #['test1', 'test2', 'test3', 'test4']
MAIN = []
run_with_ngrok(app)


@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route("/fetch_csv", methods=['POST'])
def fetch_csv():
    result = request.form.to_dict(flat=False)
    global MAIN
    global BRANCH
    global YEAR
    global CODE
    BRANCH = result['class'][0]
    YEAR = result['year'][0]
    CODE = result['code'][0]
    MAIN = extract.fetch(BRANCH, YEAR)
    print(MAIN)
    return redirect('/take_pic')

@app.route("/take_pic", methods=['GET', 'POST'])
def take_pic():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        global CASES
        CASES = extract.home(path)
        print(CASES)
        CASES = [ i[0] for i in CASES]
        return redirect('/')
    return render_template('take_pic.html', title="Home")

@app.route("/result")
def result():
    global CASES
    if CASES == []:
        return redirect('/')
    print(CASES)
    print(list(set(MAIN).difference(CASES)))
    return render_template('result.html', cases=list(set(MAIN).difference(CASES)), title="Test Cases")

@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        test = request.form.getlist('checks')
        final = list(set(CASES)) + test
        extract.final_save(final, BRANCH, YEAR, CODE)
        return redirect('/')

app.run()
