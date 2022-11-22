import os

filename = 'enwiktionary-latest-pages-meta-current.xml'

file1 = open(filename, 'r', encoding='utf-8')
Lines = file1.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

'''def normalizeLetter(letter):
    letter = letter.lower()
    al = 'áâãà'
    au = 'ÁÂÃÀ'
    el = 'éê'
    eu = 'ÉÊ'
    il = 'í'
    iu = 'Í'
    ol = 'óôõ'
    ou = 'ÓÔÕ'
    ul = 'ú'
    uu = 'Ú'

    if letter in al:
        return 'a'
    if letter in au:
        return 'A'
    if letter in el:
        return 'e'
    if letter in eu:
        return 'E'
    if letter in il:
        return 'i'
    if letter in iu:
        return 'I'
    if letter in ol:
        return 'o'
    if letter in ou:
        return 'O'
    if letter in ul:
        return 'u'
    if letter in uu:
        return 'U'
    if letter == 'ç':
        return 'c'
    if letter == 'Ç':
        return 'C'
        
    return letter'''

def englishWord(word):
    word = word.lower()
    for letter in word:
        if letter not in alphabet:
            return False
    return True

def fileName(folder,word):
    filepath = os.path.join(folder,word + '.xml')
    counter = 0
    while os.path.exists(filepath):
        counter += 1
        filepath = os.path.join(folder,word + '_' + str(counter) + '.xml')
    return filepath

content = ''
collecting = False
portWord = False
counter = 0

for line in Lines:
    line = line.lstrip()
    if not collecting and line.startswith('<page>'):
        collecting = True

    if collecting:
        if line.startswith('<title>'):
            word = line[7:-9]
            portWord = englishWord(word)

        if line.startswith('</page>'):
            if portWord:
                content += line
                counter += 1
                if counter % 1000 == 0:
                    print(str(counter) + ' ' + word)
               # letter = normalizeLetter(word[0])
                folder = os.path.join('words');
                isExist = os.path.exists(folder)
                if not isExist:
                    os.makedirs(folder)
                filepath = fileName(folder,word)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                f.close()
            collecting = False
            content = ''
            title = ''
            portWord = False
        else:
            content += line