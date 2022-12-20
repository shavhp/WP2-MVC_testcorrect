import os.path
import sys
import sqlite3

from flask import Flask, request, render_template, redirect, session

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


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    tables = dbm.get_table_list()
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('tables.html',name=name1, table_list=tables)


@app.route("/leerdoelen", methods=["GET", "POST"])
def get_leerdoelen():
    tables = dbm.get_table_list()
    rows, column_names = dbm.get_leerdoelen()
    leerdoel_row = dbm.dropdown_leerdoelen()
    return render_template("foute_leerdoelen.html", rows=rows, columns=column_names, table_list=tables, leerdoel_row=leerdoel_row)


@app.route("/auteurs")
def get_auteurs():
    tables = dbm.get_table_list()
    x = 0
    if x == 0:
        rows, column_names = dbm.get_auteurs()
        return render_template("invalid_auteur.html", rows=rows, columns=column_names, table_list=tables)


@app.route("/vragen_null")
def get_vragen_null():
    tables = dbm.get_table_list()
    rows, column_names = dbm.get_vragen_null()
    return render_template("invalid_vragen.html", rows=rows, columns=column_names, table_list=tables)


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



@app.route("/table_details/<table_name>/select", methods =["GET", "POST"] )
def get_select_values(table_name=None):
    tables = dbm.get_table_list()
    columns = dbm.get_columns(table_name)
    columnname = ""
    start_value = ""
    stop_value = ""
    if request.method == "POST":
        result = request.form
        columnname = (result.get('POST'))
        start_value = (result.get('Value_2'))
        stop_value = (result.get('Value_3'))
        rows, column_names = dbm.get_selected_content(table_name, columnname,start_value,stop_value)
    return render_template('filter_column.html',
                           column_names = column_names,
                           rows=rows,
                           columns=columns,
                           table_name=table_name,
                           table_list=tables,
                           columnnames=columnname,
                           Start_values=start_value,
                           Stop_values=stop_value)


@app.route("/nbsp_error")
def get_html_error():
    tables = dbm.get_table_list()
    rows, column_names = dbm.get_htmlcodes()
    return render_template("HTML_errors.html", rows=rows, columns=column_names, table_list=tables)
@app.route("/allHTML_error")
def get_ALLhtml_error():
    tables = dbm.get_table_list()
    rows, column_names = dbm.get_Allhtmlcodes()
    return render_template("ALLHTML_errors.html", rows=rows, columns=column_names, table_list=tables)

if __name__ == "__main__":
    # According to another student: datastructure of leerdoelen is tuple, should be converted to string
    # for x in dbm.dropdown_leerdoelen():
    #    print(str(x[0]))

    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)
