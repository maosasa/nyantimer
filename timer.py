import time

def timer(h,m,s):
  sec = h*3600 + m * 60 + s
  for i in range(sec):
    time.sleep(1)
    if i%10==0:
      print("{}秒経過".format(i))
  print("終了です")
  return True