from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'
first = True


def upper(function):
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


@app.route('/assignment9', methods=['get', 'post'])
def assignment9():
    users_list = [{"firstname": "avi", "lastname": "cohen", "email": "avi@gmail.com"},
                  {"firstname": "rotem", "lastname": "levi", "email": "rotem@gmail.com"},
                  {"firstname": "roman", "lastname": "grig", "email": "grig@gmail.com"},
                  {"firstname": "shelly", "lastname": "frumkin", "email": "shelly@gmail.com"}]
    user_name = ''

    if 'search' in request.args:
        for user in users_list:
            if request.args['search'] == user['firstname'] \
                    or request.args['search'] == user['lastname'] \
                    or request.args['search'] == user['email']:
                result = [user['firstname'], user['lastname'], user['email']]
                break
            else:
                result = "User not found"
        if request.args['search'] == "":
            result = users_list
    else:
        result = ""

    if not result:
        result = ""
    elif result == "":
        result = users_list

    if user_name in session:
        user_name = session['username']
    else:
        if 'username' in request.form:
            user_name = request.form['username']
            session['username'] = user_name

    return render_template('assignment9.html',
                           user_name=user_name,
                           users_list=users_list,
                           result=result)


@app.route('/logout')
def logout():
    session['username'] = ''
    return redirect(url_for('assignment9'))


# assignment10
from assignment10 import assignment10
app.register_blueprint(assignment10)


if __name__ == '__main__':
    app.run(debug=True)
