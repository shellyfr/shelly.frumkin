from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

def upper (function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@app.route('/main')
@app.route('/home')
@app.route('/')
def cv():
    return render_template('cv.html')

@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
                           hobbies=['Dancing', 'Cooking', 'Swimming', 'work out']
                           )

if __name__ == '__main__':
    app.run()
