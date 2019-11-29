

def diff(a, b):
    return a != b


def distancewords(word1, word2):
    D = [[0] * (len(word1)+1) for i in range(len(word2)+1)]

    for i in range(1, len(word2)+1):
        D[i][0] = i
    for j in range(1, len(word1)+1):
        D[0][j] = j

    for i in range(1, len(word2)+1):
        for j in range(1, len(word1)+1):
            c = diff(word1[j-1], word2[i-1])
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + c)


    return D[len(word2)][len(word1)]















with open("brain065.txt", "r") as inputfile:
    file = inputfile.read()
    file = file.lower()
    words = file.split()
    #---------------First - pretreament ------------------------------#
    for i in range(len(words)):
        if(words[i] in { "!", "?", ",", ";", ".", ":", "«", "(", ")", "»", "-"} ):
            words.pop(i)
        while(words[i][len(words[i])-1] in {'.',',',')',':','?','»'}):
            words[i] = words[i][:len(words[i])-1]
        while(words[i][0] in {'«'}):
            words[i] = words[i][1:]
    #---------------Second - first calculations ------------------------#
    set_words = set()
    count_wordforms = dict()
    count_all_words = 0
    count_different_words = 0
    for x in words:
        count_all_words += 1
        if x not in set_words:
            set_words.add(x)
            count_different_words += 1
    dict_words = []
    dict_words
    dict_words_count = dict()
    with open("dict1.txt", "r") as dictionary:
        line = dictionary.readline()
        while(line != ''):
            dict_words.append(line.split()[0])
            dict_words_count[line.split()[0]] = int(line.split()[1])
            line = dictionary.readline()
    count_wordforms_from_dictionary = 0
    for x in set_words:
        if(x in dict_words):
            count_wordforms_from_dictionary +=1
    print(count_all_words)
    print(count_different_words)
    print(count_wordforms_from_dictionary)
    #----------------------Third - find and fix mistakes --------------------------#
    with open("dict1.txt", "r") as dictionary:
        line = dictionary.readline()
        while(line != ''):
            dict_words.append(line.split()[0])
            line = dictionary.readline()
    count_wordforms_nfrom_dictionary = 0
    set_nwords = set()
    for x in set_words:
        if(x not in dict_words):
            count_wordforms_nfrom_dictionary +=1
            set_nwords.add(x)
    print(count_wordforms_nfrom_dictionary)
    replased_words = dict()
    for x in set_nwords:
        maxl = len(x)
        tmpw = x
        for wordfdict in dict_words:
            dist = distancewords(x, wordfdict)
            mincount = 0
            if( dist <= maxl and dist <= 2 and mincount <= dict_words_count[wordfdict]):
                maxl = dist
                tmpw = wordfdict
                mincount = dict_words_count[wordfdict]
        replased_words[x] = [tmpw, maxl]
    normal_words =[]
    normal_words.extend(replased_words)
    for key, value in replased_words.items():
        if (key == value[0]):
            for i in range(len(key)):
                if (key[:i] in dict_words and key[i:] in dict_words):
                    line = key[:i] + " " + key[i:]
                    replased_words[key][0] = line
                    replased_words[key][1] = 1

    print(count_wordforms_nfrom_dictionary)
    for key, value in replased_words.items():
        print(key, " -> ", value[0])
    #----------------- Fourth - Replace and calculate -------------------------------#
    for key, value in replased_words.items():
        file = file.replace(key, value[0])
    words = file.split()
    for i in range(len(words)):
        if(words[i] in { "!", "?", ",", ";", ".", ":", "«", "(", ")", "»", "-"} ):
            words.pop(i)
        while(words[i][len(words[i])-1] in {'.',',',')',':','?','»'}):
            words[i] = words[i][:len(words[i])-1]
        while(words[i][0] in {'«'}):
            words[i] = words[i][1:]
    #print(file)
    set_words = set()
    count_forms = 0
    count_words = 0
    for x in words:
        if (x in set_words):
            count_words += 1
        else:
            set_words.add(x)
            count_forms +=1
            count_words += 1
    dict_words = []
    dict_words_count = dict()
    with open("dict1.txt", "r") as dictionary:
        line = dictionary.readline()
        while (line != ''):
            dict_words.append(line.split()[0])
            dict_words_count[line.split()[0]] = int(line.split()[1])
            line = dictionary.readline()
    count_wordforms_from_dictionary = 0
    for x in set_words:
        if (x in dict_words):
            count_wordforms_from_dictionary += 1
    print(count_forms)
    print(count_words)
    print(count_wordforms_from_dictionary)
    #---------------------Fifth - Output mistakes --------------------------------------------#
    for key, value in replased_words.items():
        if(key == value[0]):
            print(key, " - не найдено - >2")
        else:
            print(key, " - ", value[0], " - ", value[1])


    #print(replased_words)