#*- coding:euc-kr -*-
import codecs
import os,re

#stops = ['<SYNC Start=','>','C0C0C0','#D9EFB9','<P Class=KRCC>','ffccff','P Class=ENCC','red','♪','white','#FFD700','FF8C00','D4C2F3','lightgreen','aqua','#','yellow','<br>','&nbsp','-','!','orange',"'",'</BODY>','</SAMI>','<','=','font color=','♬','color=cornflowerblue','font face=','palegreen','/i','lightblue','/font','eedd44','"#D4C2F3"','"violet"',';','"','ccff99','i','b','silver','eeffaa',]
stops = ['<SYNC Start=','>','<Sync Start=','<SYNC START=','><P CLASS=KRCC>','<font color=lightgreen>','(',')','<font color=eedd44>','<font color=lightblue>','<font color=yellowgreen>','<font color=ccffcc>','<font color=gold>','<font color=gold>','<font color=aqua>','<P Class=SUBTTL>','<font color=yellow>','C0C0C0','<P Class=KRCC>','ffccff','P Class=ENCC','red','♪','white','<br>','&nbsp','!',"'",'</BODY>','</SAMI>','<font color=#D9EFB9>','<','=','♬','/i','/font',';','i','b','<I>','</I>']
stops = list(sorted(stops, reverse=True, key=len))


#폴더 안에 파일에 절대경로 리스트로 리턴
def get_abs_fpaths(dpath): 

    fpaths = os.listdir(dpath)
    return [os.path.join(dpath,fpath) for fpath in fpaths]



def write_files(nfname,fpath):
    conts = codecs.open(fpath,'r','utf8').read().split('<BODY>')[1]#[:2000]


    for stop in stops:
        if stop == '<br>' :
            #print (conts)
            conts = conts.replace(stop,' ')
        else :
            conts = conts.replace(stop,'')
    conts = re.sub(r'font.+"','',conts)
    conts = re.sub(r'Font.+"','',conts)
    conts = conts.replace('"','')

    lines = conts.split('\n')
    nlines = []
    i=0
    
    while i<len(lines):
        if lines[i][:3].count('-')>0:
            nlines.append(lines[i].replace('-','')+'\n')
            nlines.append(lines[i+2].replace('-','')+'\n')
            nlines.append(lines[i+1].replace('-','')+'\n')
            i=i+2
        else:
            nlines.append(lines[i]+'\n')
        i+=1
        
    nf = codecs.open(nfname,'w','utf8')
    nf.writelines(nlines)
    nf.close()

if __name__ =="__main__":
    dpath = 'D:\zamakzamak'
    fpaths = get_abs_fpaths(dpath)
    for fpath in fpaths:
        try:
            write_files(fpath.replace('zamakzamak','zamak'),fpath)
        except:
            print (fpath)

    print ("finish")


