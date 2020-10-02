from flask import Flask, render_template, redirect

app = Flask(__name__)

my_friends = ['Anne', 'Bill', 'Cathy']

@app.route('/')
def hello():
    return render_template("index.html", friends = my_friends)

@app.route('/home')
def home():
    return redirect('/')

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)