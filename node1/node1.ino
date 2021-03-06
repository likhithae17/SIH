#include <ESP8266WiFi.h>
#include <PubSubClient.h> 
#include <SoftwareSerial.h>
SoftwareSerial s(D6,D5);


//const char* ssid = "Likhitha";                   
//const char* password =  "75770003";    
const char* ssid = "sravanti";                   
const char* password =  "sravanti1";    
const char* mqttServer = "192.168.43.166";    
const int mqttPort = 1883;


//const char* initial="S";
//const char* check="Remove";
int packet;
int packet1;
int flag;
String data1 = "Node1";
String data2 ;
String data;
String s2 = "WL";
String s1 = "PH";
double d;
int Solenoid = D7;
float spdata;
String spdata2 ;


WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  s.begin(9600);
  Serial.begin(9600);
  pinMode(A0,OUTPUT);
  //pinMode(Solenoid, OUTPUT);    //D7 as output
  //digitalWrite(Solenoid, LOW);  //Deactivate Solenoid
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(50);
    Serial.println("Connecting to WiFi..");
  }
  Serial.print("Connected to  ");
  Serial.println(ssid);

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...\n");

    if (client.connect("ESP8266Client1")) {

      Serial.println("connected");
       

    } else {

      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(200);

    }
  }

  client.subscribe("test1");

}


void callback(char* topic, byte* payload, unsigned int length) {  
  String messageTemp;
  for (int i = 0; i < length; i++) { 
         //Serial.print((char)payload[i]);
         messageTemp += (char)payload[i];    
  }
    Serial.println();
    if (String(topic) == "test1") {
    if(messageTemp == "Remove"){
      Serial.println("Remove");
      //digitalWrite(Solenoid, HIGH);
    }
    else if(messageTemp == "S"){
         flag =1;
         packet=0;
         //Serial.println("Remove");
    }
   }
}

  


void loop() {
  //digitalWrite(Solenoid, LOW);
    if(flag==1 && client.connected() && packet<50){
        //d = analogRead(A0);
        //unsigned long t = DateTime.now();
        d = random(1,14);
        if (d<6.5)
        {
           data2 = "Soft water";
        }
        else if (6.5<d<8.5)
        {
           data2 = "Drinking water";
        }
        else if (d>8.5)
        {
          data2 = "Hard water";
        }

        if (s.available()>0)
        {
          spdata=s.read();
          //Serial.println(spdata);
        }
        
        data = String(s1)+','+String(data1)+','+String(__DATE__)+','+String(__TIME__)+','+d+','+String(data2);
        spdata2 = String(s2)+','+String(data1)+','+String(__DATE__)+','+String(__TIME__)+','+spdata+" L/Hr";
        client.publish("test1", String(data).c_str());
        client.publish("test1", String(spdata2).c_str());
        Serial.println("---");
        Serial.println(data);
        Serial.print("Sent Packet ");
        packet = packet+1;
        Serial.println(packet);
        Serial.println(spdata2);
        Serial.print("Sent Packet ");
        packet1 = packet1+1;
        Serial.println(packet1);
        delay(10000);  
    }


    if(packet==50 && client.connected())
    {
        //client.disconnect();
        //Serial.println("Connection closed");
        flag=0;
    }
    //client.subscribe("test1");
    //client.setCallback(callback);
    client.loop();
}
