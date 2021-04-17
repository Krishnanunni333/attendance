from flask import Flask, render_template,request,redirect,url_for,session
import threading
result = 0
cord = []
app = Flask(__name__)
app.secret_key = "super secret key"
'''@app.route('/')
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
    return render_template('handle_data.html')'''
    
@app.route('/student', methods=['GET','POST'])
def student():
    dep = request.args.get('dep')
    if dep == None:
        return render_template('error.html')
    print(dep)
    sem = request.args.get('sem')
    if sem == None:
        return render_template('error.html')
    print(sem)
    sub = request.args.get('sub')
    if sub == None:
        return render_template('error.html')
    print(sub)
    id = request.args.get('id')
    if id == None:
        return render_template('error.html')
    print(id)
    f_name = request.args.get('f_name')
    if f_name == None:
        return render_template('error.html')
    print(f_name)
    l_name = request.args.get('l_name')
    if l_name == None:
        return render_template('error.html')
    print(l_name)
    with open("./csv/{}.csv".format(dep+sem+sub),"a") as f:
        f.write(f_name+","+l_name+","+id+"\n")
        f.close()
    return render_template('student.html')


if __name__ == '__main__':
    # Executing the Threads seperatly.
    app.run(threaded=True)

