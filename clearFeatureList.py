def clearfeature(line):
    words = line.replace(' ','').split(':')[1].split('+')
    word_list=[]
    for word in words:
        if ((word.count('(K')>0) or (word.count('(C')>0) or (word.count('(S')>0) or (word.count('(U')>0) or (word.count('(Y')>0)) is True:
            word_list.append(word)
    return word_list

