from lib2to3.pgen2.tokenize import generate_tokens
from utilities.gen import generate_summary
from flask import Flask, render_template, url_for, request, redirect
from forms import InputForm, UploadFileForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3e72de2c1be97c192c10ec97280d3239'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/getstarted", methods=['GET', 'POST'])
def getstarted():
    form = InputForm()
    if form.validate_on_submit():
        txt = form.inputtext.data
        if request.method == 'POST':
            with open('files/test.txt', 'w') as f:
                f.write(str(txt))
        sum_txt = ". ".join(generate_summary("files/test.txt", 4))
        return render_template('result.html', txt=sum_txt)
    return render_template('getstarted.html', form=form)

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        return redirect(url_for('result'))
    return render_template('upload.html', form=form)

@app.route("/result")
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)