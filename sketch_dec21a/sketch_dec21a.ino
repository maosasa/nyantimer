#include <Servo.h>

Servo myservo;
int pos = 0;

const int LED = 13;
int incomingByte;  // 受信データ用
void setup(){
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  myservo.attach(9);
}

void loop(){
  if (Serial.available() > 0) { // 受信したデータが存在する
    incomingByte = Serial.read(); // 受信データを読み込む
    Serial.print("I received: "); // 受信データを送りかえす
    Serial.println(incomingByte);
  for (pos = 80; pos <= 260; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 260; pos >= 80; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  myservo.write(90);
  }
  delay(1);
}

