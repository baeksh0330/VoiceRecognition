from codecs import utf_16_be_decode
import queue, os, threading
import sounddevice as sd # could not be resolved / Pylance
import soundfile as sf
import time
from scipy.io.wavfile import write

q = queue.Queue()
recorder = False
recording = False

def complicated_record(): # 마이크에서 데이터를 가져오는 부분
    # 파일 이 위치에 저장할 예정
    with sf.SoundFile("C:/Users/user/sttproject/env/temp.wav", mode='w',samplerate=16000, subtype='POM_16', channels=
    1) as file:
        with sd.InputStream(samplerate = 16000, dtype='int16', channels=1, callback=complicated_save):
            while recording:
                file.write(q.get())

def complicated_save(indata, frames, time, status): # 데이터 저장 -> callback= complicated_save
    q.put(indata.copy())

def start(): # thread를 돌릴지 말지 -> 돌리는 경우
    global recorder # 전역변수 선언
    global recording
    
    recording = True
    recorder = threading.Thread(target=complicated_record)
    print('Recording start')
    recorder.start()

def stop(): # thread를 돌릴지 말지 -> 돌리지 않는 경우
    global recorder
    global recording

    recording = True
    recorder.join()
    print('stop recording')


# def main():
#     start()
#     time.sleep(3)
#     stop()

# if __name__ == '__main__':
#     main()

start()
time.sleep(5)
stop()
#syntax error : unicode error -> unicadeescape codec can't decode bytes in position