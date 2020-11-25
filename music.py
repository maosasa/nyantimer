import pyaudio
import wave

def play_music():
  # wavファイルを読み込み
  wavfile = wave.open('cat.wav', 'rb')

  # PyAudioのインスタンスを生成
  p = pyaudio.PyAudio()

  # Streamを生成
  stream = p.open(format=p.get_format_from_width(wavfile.getsampwidth()),
                  channels=wavfile.getnchannels(),
                  rate=wavfile.getframerate(),
                  output=True)
  # チャンク単位でストリームに出力し音声を再生
  chunk = 1024

  data = wavfile.readframes(chunk) # wavfileからdataに1つ目のチャンク1024フレームを取ってくる
  #num = 1
  while len(data) > 0: # wavfileをすべて読み込み終わったら終わり
    stream.write(data) # dataをバッファに送る（1024フレーム×1チャンネル×2byte=2048byte
    data = wavfile.readframes(chunk) # wavfileから次のチャンクを取ってくる
    #print(num, ": len(data)=", len(data))
    #num+=1

  stream.stop_stream()
  stream.close()
  p.terminate()

if __name__ == "__main__":
  play_music()
