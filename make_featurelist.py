#coding=<utf-8>

import re, math
import os
from collections import Counter
import codecs
import operator
import clearFeatureList as cfl
from tmpkoma import runkoma
import pickle

WORD = re.compile(r'\w+')

#파일을 리스트 형태로 불러옴
def get_abs_fpaths(dpath): 
    fpaths = os.listdir(dpath)
    return [os.path.join(dpath,fpath) for fpath in fpaths]

#모든 문장을 String으로 저장하는 임시 txt 생성
def create_outputfile(dpath):
    file_list=[]
    file_list=get_abs_fpaths(dpath)
    conts = ''

    for file in file_list :
        conts += codecs.open(file,'r','utf8').read().replace('\r','').replace('\ufeff','')  #const:string

    tmp_f = 'tmpmorph.txt'
    f = open(tmp_f,'w')      #모든 형태소 분석 결과를 저장할 임시 파일
    f.write(conts)
    f.close()
    runkoma(tmp_f)
    print ('tmp.out.txt CREATED!!!')

#featurelist 만듬
def make_featureList(output_file):
    f = open(output_file,'r') 
    lines = f.read().split('\n')
    feature_list=[]

    for line in lines :
        if line.count(':')==0:
            pass
        else:
            feature_list+=cfl.clearfeature(line)
    feature_list=list(set(feature_list))    #중복 제거

    return feature_list


#VectorList만들기
def make_vectorList(feature_list,line):
    
    vector_list=[]
    Input_list=line.split()

    for fword in feature_list :
        if Input_list.count(fword)>0 :
            vector_list.append(1)
        else :
            vector_list.append(0)

    return vector_list
    

if __name__ =="__main__":
    dpath = 'D:\conversation'
    fpath_list = get_abs_fpaths(dpath)
    
    #create_outputfile(dpath)

    output_file = 'tmp.out.txt'
    
    feature_list = make_featureList(output_file)

    pickle.dump(feature_list,open('feature_list.p','wb'))#feature_list.p 에 저장
    pf = open('feature_list.p','rb')#feature_list.p에서 읽어옴.
    feature_list = pickle.load(pf)
  
    print ('feature_list 만들고,feature_list.p 에 저장')
    print ('finish')

 
