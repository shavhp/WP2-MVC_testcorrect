import os.path
import sys

from flask import Flask,request,render_template

from lib.tablemodel import DatabaseModel
from lib.demodatabase import create_demo_database

# This demo glues a random database and the Flask framework. If the database file does not exist,
# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 80
FLASK_DEBUG = True

app = Flask(__name__)
# This command creates the "<application directory>/databases/testcorrect_vragen.db" path
DATABASE_FILE = os.path.join(app.root_path, 'databases', 'testcorrect_vragen.db')

# Check if the database file exists. If not, create a demo database
if not os.path.isfile(DATABASE_FILE):
    print(f"Could not find database {DATABASE_FILE}, creating a demo database.")
    create_demo_database(DATABASE_FILE)
dbm = DatabaseModel(DATABASE_FILE)

# Main route that shows a list of tables in the database
# Note the "@app.route" decorator. This might be a new concept for you.
# It is a way to "decorate" a function with additional functionality. You
# can safely ignore this for now - or look into it as it is a really powerful
# concept in Python.


@app.route("/")
def loginscherm():
    return render_template("login.html")
database={'Erik':'beast','Kangyou':'beast','Sharelle':'beast','Dennis':'beast','':''}

@app.route('/form_login',methods=['POST','GET'])
def login():
    tables = dbm.get_table_list()
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('tables.html',name=name1, table_list=tables)


@app.route("/leerdoelen")
def get_leerdoelen():
    tables = dbm.get_table_list()
    x = 0
    if x == 0:
        rows, column_names = dbm.get_leerdoelen()
        return render_template("foute_leerdoelen.html", rows=rows, columns=column_names, table_list=tables)

@app.route("/vragen")
def get_vragen():
    tables = dbm.get_table_list()
    x = 0
    if x == 0:
        rows, column_names = dbm.get_vragen()
        return render_template("invalid_vraag.html", rows=rows, columns=column_names, table_list=tables)

@app.route("/auteurs")
def get_auteurs():
    tables = dbm.get_table_list()
    x = 0
    if x == 0:
        rows, column_names = dbm.get_auteurs()
        return render_template("invalid_auteur.html", rows=rows, columns=column_names, table_list=tables)


# The table route displays the content of a table
@app.route("/table_details/<table_name>")
def table_content(table_name=None):
    tables = dbm.get_table_list()
    if not table_name:
        return "Missing table name", 400  # HTTP 400 = Bad Request
    else:
        rows, column_names = dbm.get_table_content(table_name)
        return render_template(
            "table_details.html", rows=rows, columns=column_names, table_name=table_name, table_list=tables
        )

# @app.route("")

@app.route('/table_details/<table_name>/<table_list>/')
def filter_table(table_name, table_list):
    tables = dbm.get_table_list()
    columns = dbm.get_columns(table_name)
    return render_template('table_details.html', columns=columns, table=table_name, table_list=tables)


@app.route('/table_details/<table_name>/filter', methods =["GET", "POST"])
def get_select_values(table_name=None):
    tables = dbm.get_table_list()
    columns = dbm.get_columns(table_name)
    if request.method == "POST":
       # Value_1 = request.form.get("Value_1")
       Value_2 = request.form.get("Value_2")
       Value_3 = request.form.get("Value_3")
       print(Value_3, Value_2)
    return render_template('table_details.html', columns=columns, table=table_name, table_list=tables)



if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)
