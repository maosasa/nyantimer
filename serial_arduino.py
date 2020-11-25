import serial
import time

#シリアル通信(PC⇔Arduino)
def send_serial(ser):
  print("Start sending serial")
  line=""
  ser.write(b't')       #送りたい内容をバイト列で送信
  print("Sent message")
  line = ser.readline()
  print(line)
  print("Closing serial")
  ser.close()           #COMポートを閉じる

def init_serial():
  ser = serial.Serial()
  ser.port = "/dev/cu.usbserial-14JP0199"     #デバイスマネージャでArduinoのポート確認
  #ser.port = "/dev/cu.usbmodem14111"
  ser.baudrate = 115200 #Arduinoと合わせる
  ser.setDTR(False)     #DTRを常にLOWにしReset阻止
  ser.open()            #COMポートを開く
  print("Opening serial")
  return ser

if __name__ == "__main__":
  ser = init_serial()
  time.sleep(3)
  send_serial(ser)
