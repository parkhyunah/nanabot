import pickle
from make_featurelist import get_abs_fpaths
import codecs,os
import pymysql
import sys


#형태소 분석
def koma(string):
    string = string.encode('cp949')
    f = open('tmp2.txt','wb')                             #create the temp file
    f.write(string)
    f.close()
    os.system('KoMA -t -s -i tmp2.txt -o tmp-input.out.txt')   #execute with coma
    os.remove('tmp2.txt')

    outf= open('tmp-input.out.txt','r')                           #get the result from output file
    tmpLine = outf.readline()

    taglist=[]                                              #the tagged result list, the list 1:1 maps with the 'sentlist'.

    #morphList
    while tmpLine:
        if -( tmpLine.find(':')) >0:
            pass
        else:
            tmplist=tmpLine.split(':')
            taglist.append(tmplist[1].replace('\n','').replace(' ',''))
        tmpLine = outf.readline()

    outf.close()
    
    return taglist


#(DB)sqlite3에 저장
def DBconnect(dic_vector):
    conn = pymysql.connect(host='localhost', user='root', passwd='12091209', db='db_vector', charset='utf8')
    cur = conn.cursor()
    cur.execute("delete from save;")

    Qvector_list =[]
    Avector_list =[]

    for item in dic_vector.items():
        Qvector_list.append(item[0])
        Avector_list.append(item[1])

    pf = open('Qvector_list.p', 'wb')  # Qvector_list.p를 만듬
    pickle.dump(Qvector_list,pf)      #Qvector_list dump하기

    for i in range(len(dic_vector)):
        #dic_vectors.append(dic_vectors_name)
        try:
            cur.execute("INSERT INTO save VALUES (%s,%s)", (i,Avector_list[i]) )
            conn.commit()
        except:
            conn.rollback()

    cur.close()
    conn.close()
    print("DBconnect finish")
    print ("Qvector_list.p 만듬!!!")


#하나의 line을 vector만듬
def make_vect_line(feature_list,line):
    
    vector_list=[]
    input_list =[]
    taglist=koma(line)
    for tag in taglist:
        input_list +=tag.split('+')
    
    # print (input_list)

    for fword in feature_list :
        if input_list.count(fword)>0 :
            vector_list.append(1)
        else :
            vector_list.append(0)
    # print ('vector list in get vector')
    # print (vector_list)
    return vector_list

if __name__ =='__main__':
    print ('start')
    pf = open('feature_list.p','rb')    #feature_list.p에서 읽어옴.
    feature_list = pickle.load(pf)

    dic_vector={}
    
    dpath = 'D:\conversation'
    fpath_list = get_abs_fpaths(dpath)

    for fpath in fpath_list :
        conts = codecs.open(fpath,'r','utf8').read().replace('\r','').replace('\ufeff','')   #String,파일오픈
        lines=conts.split('\n') #List
        
        i=1
        vector = []

        for line in lines :
            #print (i)
            if i%2 == 1 :
                vector=make_vect_line(feature_list,line)
            else :
                dic_vector[tuple(vector)]=line
                #print (i,line)
                vector = []

            i+=1

    DBconnect(dic_vector)
    
    print ("get_vector finish")
