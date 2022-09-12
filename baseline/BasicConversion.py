# 여기서 코드짜고 cmd 창에서 가상환경 켜고 런돌려야 하나
# speechrecognition 라이브러리 pip에서 미리 install
# with-as 구문 : 개발자가 close()를 하지 않아도 자동으로 열린 파일을 close하게 해줌


import speech_recognition as sr
from gtts import gTTS # Google Text to speech (TTS)

# Import gtts could not be resolved
# 내부함수 : recognizer() / Microphone() / listen() / recognize_google()

import os
import time
import playsound

# replying using pre-saved mp3 files(이거 저장해둬야 됨) 
# 현재 문장 인식 가능(영어), 응답단계에서 오류남 -> 파일이 없어서
def reply(text, a):
    tts = gTTS(text=text, lang = 'en') # 언어설정 -> 한국어로 학습된 모델이 있다면 그걸 써도 됨
    fileName = 'C:\\'+ text + str(a) + '.mp3' # 파일 저장형식
    tts.save(fileName) # 이런 파일이 존재해야함!->파일을 열어서 틀어주는 방식임!!
    playsound.playsound(fileName)


# vr using microphone
def voiceRecognition(fileNum): 
    r = sr.Recognizer()
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


# 녹음 파일 저장용
def fileSave(audio, fileNum):
    with open("microphone-savefile"+".wav","wb") as f:
        f.write(audio.get_wav_data())

# main
def start():
    i = 0
    voiceList = []
    answer1 =""

    print("\n\n::Voice Recognization starts ::\n")
    while True: # 원하는 만큼 말하기 위함
        text = voiceRecognition(i) # return said
        
        if "hello" in text: # 첫번째 인식 -> 인사부터 시작 ->hi는 잘 못알아듣는거같다????
            answer1 = 'hilongtimenoseehowareyou'
            # reply(answer1, i)
            i+=1

        elif "how are you?" in text: #여기는 그냥 예시~
            answer1 = "I'mFine"
            # reply(answer1, i)
            i+=1

        elif "bye" in text: # 마지막 인식 -> bye가 입력된 경우
            reply("GoodBye", i)
            # print("\n::Voice Recognization Ends::")
            break
    
        voiceList.append(answer1 + str(i)+'.mp3') # 원래 예제에서는 i-1이었는데 마지막 bye에서 그냥 카운트 안해줘서 이걸로 둠
    
    for item in voiceList:
        print(item)
        os.remove('D:/'+item) # 이건 뭐지

if __name__ == '__main__':
    start()

