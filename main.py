from get_vector import make_vect_line
import clearFeatureList
import pickle
import os
from os import path
import re, math
import pymysql
import sys
import  numpy
import speech_recognition as sr
from gtts import gTTS
from pyglet.gl import *
from pyglet import window, app
from pyglet import event
import sys
import tempfile


fname = tempfile.mktemp()       #recognition 임시 저장

#cos 유사도 함수
def cos(v1,v2):

    return numpy.dot(v1,v2)/((numpy.sqrt(numpy.dot(v1,v1))*numpy.sqrt(numpy.dot(v2,v2)))+0.000000001)


if __name__ == '__main__' :

    conn = pymysql.connect(host='localhost', user='root', passwd='12091209', db='db_vector', charset='utf8')
    cur = conn.cursor()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # write audio to a WAV file
    with open(fname, "wb") as f:
        f.write(audio.get_wav_data())

    WAV_FILE = path.join(path.dirname(path.realpath(__file__)), fname)

    # Recognize
    r = sr.Recognizer()
    with sr.WavFile(WAV_FILE) as source:
        audio = r.record(source)  # read the entire WAV file

    try:
        from pprint import pprint

        obj = r.recognize_google(audio, language='ko-KR', show_all=True)

        # pprint(obj) # pretty-print the recognition result
        # 'transcrips' of first list value of 'altinative' of obj(dic)
        print("나 :"+obj['alternative'][0]['transcript'])
        ouptupline=obj['alternative'][0]['transcript']

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



    fpf = open('feature_list.p', 'rb')               # feature_list.p에서 읽어옴.
    feature_list = pickle.load(fpf)                  #저장해 둔 feature_list 불러옴

    qpf = open('Qvector_list.p', 'rb')               # feature_list.p에서 읽어옴.
    Qvector_list = pickle.load(qpf)                  # 저장해 둔 feature_list 불러옴


    tmpline=make_vect_line(feature_list,ouptupline)        #string을 벡터로 된 리스트에 저장한 부분을 tmpline에 저장

    cosin_calculate_list=[]                          #cosin 유사도 계산을 넣을 리스트
    for qvec in Qvector_list:
        cosin_calculate_list.append(cos(tmpline, qvec))


    maxind=cosin_calculate_list.index(max(cosin_calculate_list))    #코사인 유사도 최대값의 index값

    cur.execute("SELECT answer FROM save where num=%s;", (maxind))  #db내에서 index위치

    toutput=cur.fetchall()[0]
    output=''.join(toutput)
    print ('chat_bot : '+output)

    win = window.Window()
    event_loop = app.EventLoop()

    tts = gTTS(text=output, lang='ko')
    tts.save("output.mp3")


    music = pyglet.media.load('output.mp3')
    music.play()

    app.run()
    event_loop.exit()


    print('finish')


