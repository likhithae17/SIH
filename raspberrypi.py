import paho.mqtt.client as mqtt
import time
import mysql.connector

nx = mysql.connector.connect( user='root',
                              password='password',
                              host='localhost',
                              auth_plugin='mysql_native_password',
                              database='mydatabase')

mycursor = nx.cursor()

#mycursor.execute("CREATE TABLE Waterquantity(id INT AUTO_INCREMENT PRIMARY KEY,sensorname VARCHAR(255),username VARCHAR(255),date VARCHAR(255), time VARCHAR(255), quantity VARCHAR(255))")
#mycursor.execute("CREATE TABLE ph(id INT AUTO_INCREMENT PRIMARY KEY,sensorname VARCHAR(255),username VARCHAR(255),date VARCHAR(255), time VARCHAR(255), ph VARCHAR(255), classification VARCHAR(255))")

def on_connect(client, userdata, flags, rc):
        print ("Connected with Code : " + str(rc))
        client.subscribe("test1")

def on_message(client, userdata, msg):
        print(msg.payload)
        global nx
        global mycursor
        array=msg.payload
        array=array.decode("utf-8")
        array1=array.split(',')
        print(array1)
        if(array1[0]=='PH'):
            sql = "INSERT INTO ph(sensorname, username, date, time, ph, classification) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (array1[0],array1[1],array1[2],array1[3],array1[4],array1[5])
        elif (array1[0] == 'WL'):
            sql = "INSERT INTO Waterquantity(sensorname, username, date, time, quantity) VALUES (%s, %s, %s, %s, %s)"
            val = (array1[0],array1[1],array1[2],array1[3],array1[4])
    
        mycursor.execute(sql, val)
        nx.commit()
        print(mycursor.rowcount, "record inserted.")
        print(msg.payload)
                
                
                

client = mqtt.Client("node6")
client.on_connect = on_connect
client.on_message = on_message

broker_address="192.168.43.166"              #"m16.cloudmqtt.com"
port = 1883                #16755
user =""                  #"ryqrjgdp"
password ="" 


import paho.mqtt.client as mqtt
import time
import mysql.connector

nx = mysql.connector.connect( user='root',
                              password='password',
                              host='localhost',
                              auth_plugin='mysql_native_password',
                              database='mydatabase')

mycursor = nx.cursor()

#mycursor.execute("CREATE TABLE Waterquantity(id INT AUTO_INCREMENT PRIMARY KEY,sensorname VARCHAR(255),username VARCHAR(255),date VARCHAR(255), time VARCHAR(255), quantity VARCHAR(255))")
#mycursor.execute("CREATE TABLE ph(id INT AUTO_INCREMENT PRIMARY KEY,sensorname VARCHAR(255),username VARCHAR(255),date VARCHAR(255), time VARCHAR(255), ph VARCHAR(255), classification VARCHAR(255))")

def on_connect(client, userdata, flags, rc):
        print ("Connected with Code : " + str(rc))
        client.subscribe("test1")

def on_message(client, userdata, msg):
        print(msg.payload)
        global nx
        global mycursor
        array=msg.payload
        array=array.decode("utf-8")
        array1=array.split(',')
        print(array1)
        if(array1[0]=='PH'):
            sql = "INSERT INTO ph(sensorname, username, date, time, ph, classification) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (array1[0],array1[1],array1[2],array1[3],array1[4],array1[5])
        elif (array1[0] == 'WL'):
            sql = "INSERT INTO Waterquantity(sensorname, username, date, time, quantity) VALUES (%s, %s, %s, %s, %s)"
            val = (array1[0],array1[1],array1[2],array1[3],array1[4])
    
        mycursor.execute(sql, val)
        nx.commit()
        print(mycursor.rowcount, "record inserted.")
        print(msg.payload)
                
                
                

client = mqtt.Client("node6")
client.on_connect = on_connect
client.on_message = on_message

broker_address="192.168.43.166"              #"m16.cloudmqtt.com"
port = 1883                #16755
user =""                  #"ryqrjgdp"
password ="" 
 

client.connect(broker_address,port, 60)
client.username_pw_set(user,password)


client.loop_forever()  









 
