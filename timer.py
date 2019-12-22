import time

def timer(h,m,s):
  sec = h*3600 + m * 60 + s
  for i in range(sec):
    if i%10==0 and i != 0:
      print("{}秒経過".format(i))
    time.sleep(1)
  print("時間が来たニャ！")
  # serialしたい
