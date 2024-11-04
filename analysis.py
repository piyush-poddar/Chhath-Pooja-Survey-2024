from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import plotly.express as px
import pandas as pd

db_config = read_db_config()
conn = None
conn = MySQLConnection(**db_config)

cursor = conn.cursor()
cursor.execute("SET AUTOCOMMIT = 1")

q1_title = "How satisfied were you with the overall <br>organization of the Chhath Puja event?"
q2_title = "What did you enjoy most about this year’s <br>Chhath Puja celebration?"
q3_title = "Were the arrangements for cleanliness and <br>safety during the event adequate?"
q4_title = "Would you attend or recommend our Chhath Puja <br>event to others next year?"

q1_options = ['Very Satisfied','Satisfied','Neutral','Dissatisfied','Very Dissatisfied']
q2_options = ['Pooja Ghat','Decoration and Lighting','NEFOWA <br>Team Support']
q3_options = ['Yes','Needs Improvement']
q4_options = ['Yes','No','Maybe']

titles = [q1_title, q2_title, q3_title, q4_title]
q_options = [q1_options, q2_options, q3_options, q4_options]

def survey_analysis():
    for q_no in range(1,5):
        cursor.execute(f"select Question{q_no} from chhathpuja_survey")
        data =  cursor.fetchall()
        user_options = [option for i in data for option in i]
        values = [user_options.count(option) if option!='NEFOWA <br>Team Support' else user_options.count('NEFOWA Team Support') 
                  for option in q_options[q_no-1]]
        fig = px.pie(names=q_options[q_no-1], values=values,
                     title=titles[q_no-1])
        fig.update_layout(
            title_x=0.5,  # Center the title
            showlegend=False,
            margin=dict(t=150, b=0, l=100, r=100)
        )

        # Updating text properties
        fig.update_traces(textposition='outside', textinfo='label+percent', rotation=90)
        fig.write_image(rf"static/question{q_no}.png", width=600, height=600)
        print(user_options, values)

if __name__=='__main__':
    survey_analysis()