import mysql.connector
from mysql.connector import Error
from transformers import pipeline
def create_server_connection(host_name,user_name,user_password):
    connection=None
    try:
        connection=mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            auth_plugin="mysql_native_password"
        )
        print("My SQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection
connection=create_server_connection("localhost","root","chaitali12345")
mycursor = connection.cursor()
count=0
mycursor.execute("SHOW DATABASES")

for x in mycursor:
        x = ''.join(x)
        if x=="sentiment_analysis":
            count+=1

if count==0:
    mycursor.execute("CREATE DATABASE Sentiment_Analysis")
    mycursor.execute("USE Sentiment_Analysis")
    mycursor.execute("CREATE TABLE sentiments (text varchar(100), result varchar(20))")



# Using a transformer's pipeline
pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
while(True):
    n=input("enter 'n' for discontinue and 'y' for continue: ")
    if(n=='y'):
            text=""
            text=input("enter a text: ")
            result=pipe(text)
            result=result[0]
            result=result["label"]

            value=[]
            value.append(text)
            value.append(result)
            query = f"INSERT INTO sentiments (text,result) VALUES ('{value[0]}', '{value[1]}')"
            mycursor.execute(query)
            connection.commit()

            print("record inserted.")
    else:
        
        break
mycursor.execute(" SELECT DISTINCT(text),result FROM SENTIMENTS ")
# fetch all of the rows from the query
data = mycursor.fetchall ()

# print the rows
for row in data :
    print (row)