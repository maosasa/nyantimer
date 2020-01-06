import serial
import time

#シリアル通信(PC⇔Arduino)
def send_serial():
  ser = serial.Serial()
  ser.port = "/dev/tty.usbmodem14311"     #デバイスマネージャでArduinoのポート確認
  ser.baudrate = 9600 #Arduinoと合わせる
  ser.setDTR(False)     #DTRを常にLOWにしReset阻止
  ser.open()            #COMポートを開く
  print("start sending serial")
  for i in range(3):
    ser.write(b'l')       #送りたい内容をバイト列で送信
    time.sleep(1)
    ser.write(b'0')
    time.sleep(1)
  ser.close()           #COMポートを閉じる


if __name__ == "__main__":
  send_serial()
