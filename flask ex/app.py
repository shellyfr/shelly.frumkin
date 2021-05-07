from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def get_home():
    return redirect('/')

@app.route('/index')
def get_index():
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)
