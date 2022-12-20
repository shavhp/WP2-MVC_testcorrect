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

    def get_selected_content(self, table_name, columnnames, Start_values, Stop_values):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT * from {table_name} Where  {columnnames} BETWEEN {Start_values} AND {Stop_values} ORDER BY {columnnames} ASC")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        selected_headers = [column_name[0] for column_name in cursor.description]
        selected_content = cursor.fetchall()
        # Note that this method returns 2 variables!
        return selected_content, selected_headers


    #Patronen > Leerdoelen
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
        cursor.execute(f"SELECT * FROM leerdoelen")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        leerdoelen_list = cursor.fetchall()
        return leerdoelen_list

    '''def id_dropdown_leerdoelen(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute(f"SELECT id FROM leerdoelen")
        id_leerdoelen = cursor.fetchall()
        return id_leerdoelen'''

    '''def update_leerdoelen(self, new_leerdoel, new_id):
        cursor = sqlite3.connect(self.database_file).cursor()
        # Creates a new table from the sql query
        cursor.execute(f"UPDATE vragen SET leerdoel = ? WHERE id = ?, (new_leerdoel, new_id)")'''

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

    #Patronen > Auteurs
    def get_auteurs(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute("SELECT * FROM vragen WHERE auteur NOT IN(SELECT id FROM auteurs)")
        # An alternative for this 2 var approach is to set a sqlite row_factory on the connection
        auteurs_table_headers = [column_name[0] for column_name in cursor.description]
        auteurs_table_content = cursor.fetchall()
        return auteurs_table_content, auteurs_table_headers

    #Data kwaliteit > Vragen tabel
    def get_vragen_null(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute("SELECT * FROM vragen WHERE auteur IS NULL OR leerdoel IS NULL OR vraag IS NULL;")
        vragen_table_headers = [column_name[0] for column_name in cursor.description]
        vraag_table_content = cursor.fetchall()
        return vraag_table_content, vragen_table_headers

    #Data kwaliteit > HTML_errors
    def get_htmlcodes(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute("SELECT id,vraag FROM vragen WHERE vraag LIKE '%&nbsp%' OR vraag LIKE '%<br>%';")
        HTML_error_header = [column_name[0] for column_name in cursor.description]
        HTML_error_content = cursor.fetchall()
        return HTML_error_content, HTML_error_header

    def get_Allhtmlcodes(self):
        cursor = sqlite3.connect(self.database_file).cursor()
        cursor.execute("SELECT id,vraag FROM vragen WHERE vraag LIKE '%&%' OR vraag LIKE '%<%' OR vraag LIKE '%>%' OR vraag LIKE '%nbsp%';")
        ALLHTML_error_header = [column_name[0] for column_name in cursor.description]
        ALL_error_content = cursor.fetchall()
        return ALL_error_content, ALLHTML_error_header