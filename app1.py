from flask import Flask, render_template,request,redirect,url_for,session
import threading
result = 0
cord = []
app = Flask(__name__)
app.secret_key = "super secret key"
@app.route('/')
def index1():
    return render_template('index.html')
@app.route('/handle_data', methods=['GET','POST'])
def handle_data():
    if request.method == 'POST':
        session['dep']=request.form['dep']
        print(session['dep'])
        global result
        global cord
        result = request.form
        cord = [1,1,1,1]
    return render_template('handle_data.html')
@app.route('/student/<id>', methods=['GET','POST'])
def student(id):
    print(id)
    return render_template('student.html',dep=session['dep'],cord = cord)


if __name__ == '__main__':
    # Executing the Threads seperatly.
    app.run(threaded=True)

