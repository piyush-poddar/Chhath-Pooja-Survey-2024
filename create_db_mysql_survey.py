import mysql.connector

covid19db_new = mysql.connector.connect(
 host="192.168.10.51",
 user="devopsadmin",
 password="password"
)

cursor = covid19db_new.cursor()

# Create Database

def create_db(dbname):
        cursor.execute("SHOW DATABASES LIKE 'chhathpuja_survey_dev'")
        database = cursor.fetchall()

        if database !=  [('covid19_survey_dev',)]:
            cursor.execute("CREATE DATABASE IF NOT EXISTS chhathpuja_survey_dev")
            print ("Created database successfully")

            cursor.execute("SHOW DATABASES LIKE 'chhathpuja_survey_dev'")
            db_check = cursor.fetchall()
            print(db_check)
            
        else:
            print("DB chhathpuja_survey_dev already Exists.")
            cursor.execute("SHOW DATABASES LIKE 'chhathpuja_survey_dev'")
            db_check = cursor.fetchall()
            print("DB is:", db_check)
        
def create_table():
    try:
        cursor.execute('USE chhathpuja_survey_dev')
        cursor.execute('CREATE TABLE chhathpuja_survey (Name VARCHAR(100), Society VARCHAR(50), Mobile VARCHAR(10), Question1 VARCHAR(50), Question2 VARCHAR(50), Question3 VARCHAR(50), Question4 VARCHAR(50), Question5 VARCHAR(500))')
        
        cursor.execute("SHOW TABLES")
        table_check = cursor.fetchall()
        print("Table", table_check, "created successfully.")

        cursor.close()
    except Exception as e:
        print(e)


create_db(dbname="chhathpuja_survey_dev")
create_table()
