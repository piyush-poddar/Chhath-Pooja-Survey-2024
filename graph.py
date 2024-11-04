

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os

import time

db_config = read_db_config()
conn = None
conn = MySQLConnection(**db_config)

def connect():
    """ Connect to MySQL database """

    # db_config = read_db_config()
    # conn = None
    try:
        # print('Connecting to MySQL database...')
        pass
        # conn = MySQLConnection(**db_config)

        if conn.is_connected():
            pass
            # print('Connection established.')
            # cursor = conn.cursor()
            # cursor.execute("select * from survey")
            # data = cursor.fetchall()
            # print(data)
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    # finally:
    #     if conn is not None and conn.is_connected():
    #         conn.close()
    #         print('Connection closed.')


def survey_data():
    """ Retrieve Data From Mysql """
    try:
        # question_list = ['question1']
        # for question in question_list:
        #     cursor = conn.cursor()
        #     cursor.execute("SET AUTOCOMMIT = 1")
        #     # cursor.execute("select question1 from survey_new")
            
        #     if question == 'question1':
        #         cursor.execute("select {field} from survey_new".format(field=question))
        #     return cursor.fetchall()

        pass

            # elif question == 'question2':
            #     cursor.execute("select {field} from survey_new".format(field=question))
            #     ques2 = cursor.fetchall()
            #     # print(ques2)
    



    except Error as error:
        print(error)
        conn.close()
    
    # finally:
    #     print("Survey Data is ready for analysis.")


# data_list = survey_data()

def survey_analysis_01():
    """ Analyse Data From Mysql """

    # data_list = survey_data()

    question_list = ['question1', 'question2', 'question3', 'question5', 
                      'question8', 'question9', 'question10']
    for question in question_list:
        # print(question)
        cursor = conn.cursor()
        cursor.execute("SET AUTOCOMMIT = 1")
        # cursor.execute("select question1 from survey_new")
        cursor.execute("select {field} from covid19_survey".format(field=question))
        data =  cursor.fetchall()

    
        data_list = data

        # using list comprehension
        data_listout = [item for data in data_list for item in data]
        set_data_listout = set(data_listout)
        list_data_listout = list(set_data_listout)
        # For Graph - final_data_01
        #final_data_01 = sorted(list_data_listout, reverse=True)
        final_data_01 = ['Yes', 'Sometimes', 'No']

        # print(data_listout)
        # print(final_data_01)

        # print("Total Survey Given : ", len(data_listout))
        total_data_count = len(data_listout)

        # print("Yes : ", data_listout.count('Yes'))
        # print("Sometimes : ", data_listout.count('Sometimes'))
        # print("No : ", data_listout.count('No'))
        

        yes_count = data_listout.count('Yes')
        sometimes_count = data_listout.count('Sometimes')
        no_count = data_listout.count('No')
        
        value_count = [yes_count, sometimes_count, no_count]
        # print("Value Count: ", value_count)        

        yes_percentage = (yes_count / total_data_count) * 100
        sometimes_percentage = (sometimes_count / total_data_count) * 100
        no_percentage = (no_count / total_data_count) * 100
        

        yes_percentage = round(yes_percentage, 2)
        no_percentage = round(no_percentage, 2)
        sometimes_percentage = round(sometimes_percentage, 2 )

        # print("\nPercentage of 'Yes' in {} : ".format(question), yes_percentage)
        # print("Percentage of 'Sometimes' in {} : ".format(question), sometimes_percentage)
        # print("Percentage of 'No' in {} : ".format(question), no_percentage)
        
        # For Graph - list_percentage_data_01
        list_percentage_data_01 = [yes_percentage , sometimes_percentage, no_percentage ]
        # print("List Percentage:", list_percentage_data_01)

        # For Graph - list_colors_data_01
        list_colors_data_01 = ['green', 'yellow', 'red']
        # print(list_colors_data_01)

        

        # Plot_01
        # plt.pie(list_percentage_data_01, labels=final_data_01, colors=list_colors_data_01, autopct='%1.1f%%')
        plt.pie(value_count, labels=final_data_01, colors=list_colors_data_01, autopct='%1.1f%%')
        fig = plt.gcf()
        fig.set_size_inches(4.41,4.8) # or (4,4) or (5,5) or whatever
        # plt.show()

        cw = os.getcwd()
        
        # For Linux
        newcw = cw+"/static/"
        
        # For Windows
        # newcw = cw+"\static\/"


        # Create a file with timestamp
        # basename = "question01"
        # suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        # myfile = "_".join([basename, suffix]) # e.g. 'mylogfile_120508_171442'

        #print(myfile)
        
        # plt.title("Survey analysis : {}".format(question))
        # bytes_image = plt.savefig('D:\web_development - Copy\covid19_survey_new\static\question01.png')

    # for spot, group in df.set_index('spot', append=True).groupby(level='spot'):
    #     group.plot(kind = 'bar, figsize = (12,6))
    #     plt.savefig('{}.png'.format(spot))

        # plt.savefig(newcw+"question01.png")
        
        # for image in question_list:

            # for i in range(2):
            # plt.figure(i)   
            # 

        if question == "question1":
            plt.title("{}".format("""1. Are you happy, as now you are spending
    a lot of time with your family members
    during the lockdown?"""))

        if question == "question2":
            plt.title("{}".format("""2. Have you been able to bring any change
    in the mental health of
    any family members?"""))

        if question == "question3":
            plt.title("{}".format("""3. Have you developed new healthy
    eating habits?
    """))

        if question == "question5":
            plt.title("{}".format("""5. By spending a lot of time with your
    family members these days,
    do you feel more close to them now?"""))
            fig.set_size_inches(6,5.4)
        if question == "question8":
            plt.title("{}".format("""8. Do you agree that the lockdown has enabled
    you to communicate with your close ones
    as compared to your previous busy routine?"""))

        if question == "question9":
            plt.title("{}".format("""9. Do you feel that mental health is as
    important as the physical health and
    we should equally pay attention to it?"""))

        if question == "question10":
            plt.title("{}".format("""10. Do you agree that watching spiritual
    shows improves the health status
    of our minds?"""))



        plt.savefig(newcw+'{}.png'.format(question))
        # plt.show()
        plt.clf()

        # print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

def survey_analysis_02():
    """ Analyse Data From Mysql """

    # data_list = survey_data()

    question_list = ['question4', 'question6', 'question7']
    for question in question_list:
        # print(question)
        cursor = conn.cursor()
        cursor.execute("SET AUTOCOMMIT = 1")
        # cursor.execute("select question1 from survey_new")
        cursor.execute("select {field} from covid19_survey".format(field=question))
        data =  cursor.fetchall()

    
        data_list = data

        # using list comprehension
        data_listout = [item for data in data_list for item in data]
        set_data_listout = set(data_listout)
        list_data_listout = list(set_data_listout)
        # For Graph - final_data_01
        # final_data_01 = sorted(list_data_listout, reverse=True)
        final_data_01 = ['Yes', 'Sometimes/Maybe', 'No']

        # print(data_listout)
        # print("final data",final_data_01)

        # print("Total Survey Given : ", len(data_listout))
        total_data_count = len(data_listout)

        # print("Yes : ", data_listout.count('Yes'))
        # print("Sometimes/Maybe : ", data_listout.count('Sometimes/Maybe'))
        # print("No : ", data_listout.count('No'))
        

        yes_count = data_listout.count('Yes')
        somemaybe_count = data_listout.count('Sometimes/Maybe')
        no_count = data_listout.count('No')

        value_count = [yes_count, somemaybe_count, no_count]
        # print("Value Count: ", value_count)             
        

        yes_percentage = (yes_count / total_data_count) * 100
        somemaybe_percentage = (somemaybe_count / total_data_count) * 100
        no_percentage = (no_count / total_data_count) * 100
        

        yes_percentage = round(yes_percentage, 2)
        somemaybe_percentage = round(somemaybe_percentage, 2)
        no_percentage = round(no_percentage, 2)


        # print("\nPercentage of 'Yes' in {} : ".format(question), yes_percentage)
        # print("Percentage of 'Sometimes/Maybe' in {} : ".format(question), somemaybe_percentage)
        # print("Percentage of 'No' in {} : ".format(question), no_percentage)
        
        # For Graph - list_percentage_data_01
        list_percentage_data_01 = [yes_percentage , somemaybe_percentage , no_percentage]
        # print(list_percentage_data_01)

        # For Graph - list_colors_data_01
        list_colors_data_01 = ['green', 'yellow', 'red']
        # print(list_colors_data_01)


        # Plot_01
        # plt.pie(list_percentage_data_01, labels=final_data_01, colors=list_colors_data_01, autopct='%1.1f%%')
        plt.pie(value_count, labels=final_data_01, colors=list_colors_data_01, autopct='%1.1f%%')
        fig = plt.gcf()
        fig.set_size_inches(6,5.4) # or (4,4) or (5,5) or whatever
        cw = os.getcwd()
        
        # For Linux
        newcw = cw+"/static/"
        
        # For Windows
        # newcw = cw+"\static\/"

        # Create a file with timestamp
        # basename = "question01"
        # suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        # myfile = "_".join([basename, suffix]) # e.g. 'mylogfile_120508_171442'

        #print(myfile)
#        print("\nPercentage of 'Yes' in {} : ".format(question), float(yes_percentage))  

        # plt.title("Survey analysis : {}".format(question))
        # bytes_image = plt.savefig('D:\web_development - Copy\covid19_survey_new\static\question01.png')

    # for spot, group in df.set_index('spot', append=True).groupby(level='spot'):
    #     group.plot(kind = 'bar, figsize = (12,6))
    #     plt.savefig('{}.png'.format(spot))

        # plt.savefig(newcw+"question01.png")
        
        # for image in question_list:

            # for i in range(2):
            # plt.figure(i)


        if question == "question4":
            plt.title("{}".format("""4. Do you feel that being at work you tend to
    ignore yourself and your health but now
    you are having your ‘Me time’?"""))

        if question == "question6":
            plt.title("{}".format("""6. Have you adopted any new healthy habits in
    your daily routine to improve your
    health and wellness?"""))

        if question == "question7":
            plt.title("{}".format("""7. Did you meditate or perform Yoga to improve
    your mental health?
    """))


        plt.savefig(newcw+'{}.png'.format(question))
        # plt.show()
        plt.clf()
    
        # print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")     

def close_connection():
    """ Close DB Connection """
    if conn is not None and conn.is_connected():
        conn.close()
        print('Connection is closed.')

if __name__ == '__main__':
    connect()
    survey_data()
    survey_analysis_01()
    survey_analysis_02()
    close_connection()
