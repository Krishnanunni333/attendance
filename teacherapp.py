#from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, redirect
from flask import request
app = Flask(__name__)
CASES = [] #['test1', 'test2', 'test3', 'test4']
#run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route("/take_pic")
def take_pic():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return path
    return render_template('take_pic.html', title="Home")

@app.route("/result")
def result():
    if CASES == []:
        return redirect('/')
    return render_template('result.html', cases=CASES, title="Test Cases")

@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        test = request.form.getlist('checks')
        print(test)
        return redirect('/')
  
app.run()
