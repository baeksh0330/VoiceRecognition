# 여기서 코드짜고 cmd 창에서 가상환경 켜고 런돌려야 하나 -> 여기서 런 돌아감
# pip install : speechrecognition / gtts / sounddevice / wheel / pyaudio / playsound / librosa / audioread / soundfile
# with-as 구문 : 개발자가 close()를 하지 않아도 자동으로 열린 파일을 close하게 해줌

__author__ ="baeksh0330@naver.com"

import speech_recognition as sr
from gtts import gTTS # Google Text to speech (TTS)
# 내부함수 : recognizer() / Microphone() / listen() / recognize_google()

import os
from time import time
from time import localtime
import playsound # pygame이나 playsound 둘 중 하나 이용할 예정
import pygame

# synthesis voice + play voicefile
def reply(text, a):
    tts = gTTS(text=text, lang = 'en') # 언어설정 -> 한국어로 학습된 모델 : lang = 'ko'
    fileName = text + str(a) + '.mp3' # 파일 저장형식
    tts.save(fileName) # filename으로 mp3파일 합성 -> 지금 pyaudio가 mp3파일을 지원하지 않아 reply에서 오류가 발생하는것으로 보임
    playsound.playsound(fileName) # 읽어주기


# vr using microphone
def voiceRecognition(fileNum): 
    r = sr.Recognizer() # 인식 시작 
    with sr.Microphone() as source :
        audio = r.listen(source) # 받기
        YouSaid=" "

        try:
            YouSaid = r.recognize_google(audio) # 오류가 없을경우 말한 문장 tts후 출력
            print("YOU :",YouSaid)
        
        except Exception as e:
            print("Exception :"+str(e)) # 오류 발생한 경우 오류 출력

    fileSave(YouSaid, fileNum) # 문장 저장
    return YouSaid # 말한 문장 반환


# save recording file 
def fileSave(audio, fileNum):
    with open(fileNum+"microphone-savefile"+".wav","wb") as f:
        f.write(audio.get_wav_data())


# chat here!
def chat():
    voiceList = []
    print("Welcome.")
       
    while True:
        text = voiceRecognition(cnt) # return said
        
        if "hi" or "hello" in text: 
            answer = 'hilongtimenoseehowareyou'
            # reply(answer1, cnt)
            cnt+=1

        elif "how are you?" in text: # 그냥 예시
            answer = "I'mFine"
            # reply(answer1, cnt)
            cnt+=1

        elif "time" in text: # ex : 시간 알려줘 / 지금 몇 시야 / ...
            now = localtime(time())
            date = str(now.tm_year + "-" + now.tm_mon + "-" + now.tm_mday)
            time = str(now.tm_hour + "-" + now.tm_min + "-" + now.tm_sec)
            
            # 날짜 물어보는지 시간 물어보는지 확인하고 return
            answer = "dateortime?"
            if voiceRecognition(cnt) == "date":
                answer = date
            elif voiceRecognition(cnt) == "time":
                answer = time
            else:
                answer = "say again."
                
            # reply(answer, cnt)

            cnt+=1

        elif "bye" in text: # 마지막 인식 -> bye가 입력된 경우
            # reply("GoodBye", cnt)
            print("\n::Voice Recognization Ends::")
            break
        
        voiceList.append(answer + str(cnt)+'.mp3') # 원래 예제에서는 i-1이었는데 마지막 bye에서 그냥 카운트 안해줘서 이걸로 둠
    
    for item in voiceList:
        print(item)
        os.remove('D:/'+item) # 이건 뭐지

# main
def start():
    cnt = 0 # conversation count
    answer = ""
    text = ""

    print("\n\n::Voice Recognization starts ::\n")
    text = voiceRecognition(cnt)

    if "heybuddy" in text: # 헤이버디 듣고있으니까 일단은 헤이버디
       chat()
    else:
        print("no voice verified")
        print("\n:: Voice Recognition ends. ::")
        exit(1)



if __name__ == '__main__':
    start()

