from flask import Flask
from flask import render_template, request
app2 = Flask(__name__)

def readDetails(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    return Lines
    

@app2.route('/')
def home():
    name = "Mark Rodriguez"
    details = readDetails('static/details.txt')
    return render_template("base.html", name = name, aboutMe = details)

@app2.route('/user/CV')
def get_pdf():
        return  "This is my resume"
@app2.route('/form', methods=['GET','POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('form.html', name=name)

if __name__ == '__main__':
    app2.run(debug=True)