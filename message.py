import re

def get_time_from_message(received_message):
  units_ja = ["時間", "分", "秒"]
  times = [0,0,0]

  for i,unit in enumerate(units_ja):
    pattern = "[0-9]+"+unit
    #print("p:{} m:{}".format(pattern,received_message))
    time_strings = re.findall(pattern, received_message)
    #print("time_strings:{}".format(time_strings))
    if len(time_strings) > 1:
      times = [0,0,0]
      break
    if time_strings:
      time_string = time_strings[0]
      times[i] = int(time_string.replace(unit,""))

  return times

def get_time_string(times):
  units_ja = ["時間", "分", "秒"]
  time_string = ""

  for time,unit in zip(times,units_ja):
    if time:
      time_string += str(time)+unit
  return time_string


def create_reply_and_times(received_message):
  times =  get_time_from_message(received_message)
  message = get_time_string(times)
  if message:
    message += "後におしらせするニャ！"
  else:
    message = "にゃーん"
    times = None
  return (message,times)

