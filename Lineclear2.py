#*- coding:euc-kr -*-
import codecs
import os,re
import operator

#������ ����Ʈ ���·� �ҷ���
def get_abs_fpaths(dpath): 

    fpaths = os.listdir(dpath)
    return [os.path.join(dpath,fpath) for fpath in fpaths]




def write_files(nfname,fpath):
    conts = codecs.open(fpath,'r','utf8').read().replace('\r','')

    lines=conts.split('\n')     #����Ʈ�� '\n'���� �ɰ��� ������
    copy_lines=[]
    dic_line = {}


    #ù��° �з��۾� - ���ڸ� �ִ°��, �ƹ��͵� ���� ��� ���� ����
    for i in range(len(lines)):
        if lines[i] == '' :
            pass
        elif lines[i].isdigit()==True:
            pass
        else :
            copy_lines.append(lines[i])


    patt='[0-9][0-9][0-9][0-9][0-9][0-9]?[0-9]?'

    #����+���� ������ ������ �и��ؼ� dictionary�� ����
    for i in range(len(copy_lines)) :
        string = re.sub(patt,'',copy_lines[i])
        try:
            num = int(copy_lines[i].replace(string,''))
        except:
            print (i,copy_lines[i])
        dic_line[num]=string+'\n'

    #dictionary�� list���·� sort
    sorted_x=list(sorted(dic_line.items(), key=operator.itemgetter(0)))


    
    clear_list=[]        #���ο� list
    tmp_list =[]         #list ���� list


    #�񱳵� ���� ���� 10000������ ������� �ϳ��� ����Ʈ�� ����� ����
    for i in range(len(sorted_x)-1) :
        key1 = sorted_x[i][0]
        key2 = sorted_x[i+1][0]

        
        if key2-key1 < 10000 :
           
            tmp_list+=[sorted_x[i][1]]

        #10000�̻��� ��� ����Ʈ��  Ȧ�� ���̸� ������ ���� �����ϰ� ���� 
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

    #���� list�� �ϳ��� �ҷ��ͼ� list�� ����
    for x in clear_list :
        for y in x :
            line_x.append(y)
            

    #����Ʈ �ؽ�Ʈ�� ����
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
