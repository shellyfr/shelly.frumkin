from flask import jsonify
import mysql.connector
from flask import render_template, Blueprint, request, redirect, flash

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10.py',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # insert, update, delete
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # select
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value





@assignment10.route('/assignment10')
def users():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type="fetch")
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['POST'])
def insert():
    name = request.form['name']
    lastName = request.form['lastName']
    email = request.form['email']
    query = "INSERT INTO users(name, lastName, email) VALUES ('%s','%s','%s')" % (name, lastName, email)
    interact_db(query=query, query_type="commit")
    flash('user hase been added to data base')
    return redirect('assignment10')


@assignment10.route('/update_user', methods=['POST'])
def update():
    id_update = request.form['id_update']
    email_update = request.form['email_update']
    query = "UPDATE users SET email= '%s' WHERE id ='%s'" % (email_update, id_update)
    interact_db(query=query, query_type="commit")
    flash('user has been updated')
    return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['POST'])
def delete():
    user_delete = request.form['id']
    query = "DELETE FROM users WHERE id = '%s';" % user_delete
    interact_db(query=query, query_type="commit")
    flash('user has been deleted')
    return redirect('/assignment10')


# -----------------------assignment 11-----------------------


@assignment10.route('/assignment11/users', methods=['GET'])
def users_func():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type="fetch")
    response = {}
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)
    return response


@assignment10.route('/assignment11/users/selected', defaults={'SOME_USER_ID': 1})
@assignment10.route('/assignment11/users/selected/<int:SOME_USER_ID>', methods=['GET'])
def users_data(SOME_USER_ID):
    query = "SELECT * FROM users WHERE id= '%s';" % SOME_USER_ID
    query_result = interact_db(query=query, query_type="fetch")
    response = {}
    if len(query_result) != 0:
        response = query_result[0]
    else:
        response = 'User does not exist'
    response = jsonify(response)
    return response

