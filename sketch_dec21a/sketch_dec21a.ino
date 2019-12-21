
const int LED = 13;
int incomingByte;  // 受信データ用
void setup(){
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
}

void loop(){
  if (Serial.available() > 0) { // 受信したデータが存在する
    incomingByte = Serial.read(); // 受信データを読み込む
    Serial.print("I received: "); // 受信データを送りかえす
    Serial.println(incomingByte);

    switch (incomingByte){
      case 1:
        digitalWrite(LED_BUILTIN, HIGH);
      break;
      case 0:
        digitalWrite(LED_BUILTIN, LOW);
      break;
      default:
      break;
    }
  }
  delay(1);
}

