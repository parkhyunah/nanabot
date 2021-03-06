#*- coding:euc-kr -*-
import codecs
import os,re
import operator

#파일을 리스트 형태로 불러옴
def get_abs_fpaths(dpath): 

    fpaths = os.listdir(dpath)
    return [os.path.join(dpath,fpath) for fpath in fpaths]




def write_files(nfname,fpath):
    conts = codecs.open(fpath,'r','utf8').read().replace('\r','')

    lines=conts.split('\n')     #리스트를 '\n'으로 쪼개서 가져옴
    copy_lines=[]
    dic_line = {}


    #첫번째 분류작업 - 숫자만 있는경우, 아무것도 없는 경우 빼고 저장
    for i in range(len(lines)):
        if lines[i] == '' :
            pass
        elif lines[i].isdigit()==True:
            pass
        else :
            copy_lines.append(lines[i])


    patt='[0-9][0-9][0-9][0-9][0-9][0-9]?[0-9]?'

    #숫자+문자 조합인 문장을 분리해서 dictionary로 저장
    for i in range(len(copy_lines)) :
        string = re.sub(patt,'',copy_lines[i])
        try:
            num = int(copy_lines[i].replace(string,''))
        except:
            print (i,copy_lines[i])
        dic_line[num]=string+'\n'

    #dictionary를 list형태로 sort
    sorted_x=list(sorted(dic_line.items(), key=operator.itemgetter(0)))


    
    clear_list=[]        #새로운 list
    tmp_list =[]         #list 안의 list


    #비교된 숫자 차가 10000이하인 문장들을 하나의 리스트로 만들어 저장
    for i in range(len(sorted_x)-1) :
        key1 = sorted_x[i][0]
        key2 = sorted_x[i+1][0]

        
        if key2-key1 < 10000 :
           
            tmp_list+=[sorted_x[i][1]]

        #10000이상인 경우 리스트가  홀수 개이면 마지막 문장 제외하고 저장 
        else :
            if len(tmp_list)%2 == 1 :
                tmp_list = tmp_list[:-1]
            clear_list.append(tmp_list)
            tmp_list=[]

    #print ('clear',clear_list)
    

       
 
    # keys =dic_line.keys()
    # for key in keys:
    #     print (key,dic_line[key])

    line_x =[]

    #이중 list를 하나씩 불러와서 list로 만듬
    for x in clear_list :
        for y in x :
            line_x.append(y)
            

    #리스트 텍스트로 저장
    nf = codecs.open(nfname,'w','utf8')
    nf.writelines(line_x)
    nf.close()





if __name__ =="__main__":
    dpath = 'D:/zamak2/'
    fpaths = get_abs_fpaths(dpath)
    
    for fpath in fpaths:
        
        write_files(fpath.replace('zamak2','new_zamak2'),fpath)
        #try:
        #    write_files(fpath.replace('temp','new_zamak'),fpath)
        #except:
        #print (fpath)
        

    print ("finish")
