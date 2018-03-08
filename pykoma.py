#coding=<utf-8>

import os
def runkoma(string):
    print ("koma start")
    try:
        if os.path.exists(string):                              #check if 'string' is the string or file path 
            os.system('KoMA -t -s -i '+string+' -o tmp.out.txt')#execute with koma
        else:
            f = open('tmp2.txt','wb')                             #create the temp file
            f.write(string)
            f.close()
            os.system('KoMA -t -s -i -n tmp2.txt -o tmp.out.txt')   #execute with coma
            os.remove('tmp2.txt')                                #remove the temp file
        print ("koma start")
    except:
        f = open('tmp2.txt','wb')                             #create the temp file
        f.write(string)
        f.close()
        os.system('KoMA -t -s -i tmp2.txt -o tmp.out.txt')   #execute with coma
        os.remove('tmp2.txt')
            
    outf= open('tmp.out.txt','r')                           #get the result from output file
    tmpLine = outf.readline()
    
    dict={}                                                 #create the dictionary to save the result
    sentlist = []                                           #the list of original sentence segmented
    taglist=[]                                              #the tagged result list, the list 1:1 maps with the 'sentlist'.
    while tmpLine:
        if -( tmpLine.find(':')) >0:
            pass
        else:
            tmplist=tmpLine.split(':')
            sentlist.append(tmplist[0])
            taglist.append(tmplist[1].replace('\n',''))
            dict[tmplist[0].replace(' ','')]=tmplist[1].replace('\n','')
        tmpLine = outf.readline()
    outf.close()
    return taglist

