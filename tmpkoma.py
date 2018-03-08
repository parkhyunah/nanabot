#coding=<utf-8>
#

import os
def runkoma(string):
    #print ("koma start")
    try:
        if os.path.exists(string):                              #check if 'string' is the string or file path 
            os.system('KoMA -t -s -i '+string+' -o tmp.out.txt')#execute with koma
        else:
            f = open('tmp2.txt','wb')                             #create the temp file
            f.write(string)
            f.close()
            os.system('KoMA -t -s -i tmp2.txt -o tmp.out.txt')   #execute with coma
            os.remove('tmp2.txt')                                #remove the temp file
        #print ("koma start")
    except:
        f = open('tmp2.txt','wb')                             #create the temp file
        f.write(string)
        f.close()
        os.system('KoMA -t -s -i tmp2.txt -o tmp.out.txt')   #execute with coma
        os.remove('tmp2.txt')
    print("tmpkoma finish,check #tmp.out.txt#!!!")
