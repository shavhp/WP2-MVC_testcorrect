import os
import sqlite3


class DatabaseModel:
    """This class is a wrapper around the sqlite3 database. It provides a simple interface that maps methods
    to database queries. The only required parameter is the database file."""

    def __init__(self, database_file):
        self.database_file = database_file
        if not os.path.exists(self.database_file):
            raise FileNotFoundError(f"Could not find database file: {database_file}")

    def run_query(self, sql_query):
        conn = sqlite3.connect(self.database_file)
        c = conn.cursor()
        c.execute(sql_query)
        tables = c.fetchall()
        conn.close()
        return tables

    # Using the built-in sqlite3 system table, return a list of all tables in the database
    def get_table_list(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [table[0] for table in cursor.fetchall()]
        return tables

    # Given a table name, return the rows and column names
    def get_table_content(self, table_name):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        table_headers = [column_name[0] for column_name in cursor.description]
        table_content = cursor.fetchall()
        # Note that this method returns 2 variables!
        return table_content, table_headers

    def get_leerdoelen(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        # Creates a new table from the sql query
        cursor.execute(f"SELECT * FROM vragen WHERE leerdoel NOT IN(SELECT id FROM leerdoelen) OR leerdoel IS NULL")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        leerdoelen_table_headers = [column_name[0] for column_name in cursor.description]
        leerdoelen_table_content = cursor.fetchall()
        # Note that this method returns 2 variables!
        return leerdoelen_table_content, leerdoelen_table_headers

    def dropdown_leerdoelen(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        # Creates a new table from the sql query
        cursor.execute(f"SELECT leerdoel FROM leerdoelen")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        leerdoelen_list = cursor.fetchall()
        # Note that this method returns 2 variables!
        return leerdoelen_list

    def get_columns(self, table):
        sql_query = "PRAGMA table_info({})".format(table)
        result = self.run_query(sql_query)
        table_list = []
        for table in result:
            table_list.append(table[1])
        return table_list

        table_list = []
        for table in result:
            table_list.append(table[0])
        return table_list

    def get_vragen(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT * FROM vragen WHERE vraag IS NULL OR vraag = '';")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        vraag_table_headers = [column_name[0] for column_name in cursor.description]
        vraag_table_content = cursor.fetchall()
        return vraag_table_content, vraag_table_headers

    def get_auteurs(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT * FROM vragen WHERE auteur NOT IN(SELECT id FROM auteurs)")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        auteurs_table_headers = [column_name[0] for column_name in cursor.description]
        auteurs_table_content = cursor.fetchall()
        return auteurs_table_content, auteurs_table_headers

    def get_auteurs_not_null(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT * FROM vragen WHERE auteur IS NOT NULL")
        auteurs_table_headers = [column_name[0] for column_name in cursor.description]
        auteurs_table_content = cursor.fetchall()
        return auteurs_table_content, auteurs_table_headers

    def get_leerdoelen_not_null(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT * FROM vragen WHERE leerdoel IS NOT NULL")
        leerdoelen_table_headers = [column_name[0] for column_name in cursor.description]
        leerdoelen_table_content = cursor.fetchall()
        return leerdoelen_table_content, leerdoelen_table_headers

    def get_htmlcodes(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT id,vraag FROM vragen WHERE vraag LIKE '%&nbsp%' OR vraag LIKE '%<br>%';")
        HTML_error_header = [column_name[0] for column_name in cursor.description]
        HTML_error_content = cursor.fetchall()
        return HTML_error_content, HTML_error_header