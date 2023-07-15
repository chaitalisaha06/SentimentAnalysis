import mysql.connector
from mysql.connector import Error
import pandas as pd
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

# mycursor.execute("CREATE DATABASE Sentiment_Analysis")
# mycursor.execute("USE Sentiment_Analysis")
# mycursor.execute("CREATE TABLE sentiments (text varchar(100), result varchar(20))")
while(True):
    n=input("enter 'n' for discontinue and 'y' for continue: ")
    if(n=='y'):
            openai.api_key = "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"
            text=""
            text=input("enter a text: ")
            
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=(f"Sentiment analysis of the following text: '{text}'\n\nSentiment score: "),
                temperature=0,
                max_tokens=1
            )

            #get the sentiment from the response
            sentiment = response.choices[0].text.strip()
            print(sentiment)
            value=[]
            value.append(text)
            value.append(sentiment)
            query = f"INSERT INTO sentiments (text,result) VALUES ('{value[0]}', '{value[1]}')"
            mycursor.execute(query)
            connection.commit()

            print("record inserted.")
    else:
        break
 