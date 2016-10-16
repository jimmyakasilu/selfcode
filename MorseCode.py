import time
import winsound
import numpy as np
freq = 880 #Hz, no. of waves per second 
code = {'-':'dah','.':['dit','di']}
dur={'dah': 750, 'di': 400, 'dit': 300}
morse_code = {'a':'.-','b':'-...','c':'-.-.',
              'd':'-..','e':'.','f':'..-.',
              'g':'--.','h':'....','i':'..',
              'j':'.---','k':'-.-','l':'.-..',
              'm':'--','n':'-.','o':'---',
              'p':'.--.','q':'--.-','r':'.-.',
              's':'...','t':'-','u':'..-',
              'v':'...-','w':'.--','x':'-..-',
              'y':'-.--','z':'--..','0':'-----',
              '1':'.----','2':'..---','3':'...--',
              '4':'....-','5':'.....','6':'-....',
              '7':'--...','8':'---..','9':'----.',
              '.':'.-.-.-',',':'--..--','?':'..--..'}
#...............sound generation............#
def playsound(sound):
    winsound.Beep(freq,dur[sound])
#..............text 2 morse.................#
def text2morse(string):
    morsecode = ''
    stringlist = string.split(' ')
    print stringlist
    for w in stringlist:
        for l in w.lower():
            if morsecode == '':
                morsecode= morsecode + morse_code[l]+' '
                print morsecode
            else:
                if w.index(l) == len(w)-1:
                    morsecode= morsecode + morse_code[l]
                    print morsecode
                else:
                    morsecode= morsecode + morse_code[l]+' '
                    print morsecode
        if stringlist.index(w) != len(stringlist) - 1:
            morsecode = morsecode +'/'
    return morsecode
    
#..............morse player.................#
def playmorse(string):
    morsecode = text2morse(string)
    print morsecode
    morseeachword = morsecode.split('/')
    print morseeachword
    for word in morseeachword:
        for d in word:
            if word.index(d)== len(word)-1 and d=='.':
                playsound(code[d][0])
            elif word.index(d)!= len(word)-1 and d=='.':
                playsound(code[d][1])
            elif d==' ':
                time.sleep(0.5)
            else:
                playsound(code[d])
        time.sleep(0.75)
#........................
while(1):
    input_text = raw_input('Enter text: ')
    playmorse(input_text)
    time.sleep(1)
    print ('Got more to di-dah-dit?: ')
    print
    print ('Press 1 for YES and 0 for NO:')
    option = raw_input()
    if option != '1':
        break
#.........................
