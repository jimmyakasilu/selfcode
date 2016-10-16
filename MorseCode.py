import time
import pygame
import winsound
import numpy as np
pygame.mixer.init()
freq = 880 #Hz, no. of waves per second 
#br = 44100 #no. of frames per second
code = {'-':'dah','.':['dit','di']}
dur={'dah': 750, 'di': 400, 'dit': 300}
'''samp = {}
#wavevalues=0
for k in length.keys():
    #print k
    samp[k]=length[k]*br
print samp'''
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
    '''filename = sound+'.wav'
    print filename'''
    #endval = int(samp[sound])
    '''#print endval
    timeinst = np.arange(0,endval,1)
    #print timeinst
    wavevalues = 10*np.ones(endval,dtype=int)
    print wavevalues'''
    #plt.plot(wavevalues)
    #plt.show()
    '''f=wave.open(filename,'w')
    f.setparams((1,2,br,endval,"NONE","Uncompressed"))
    f.writeframes(wavevalues)
    f.close()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()'''
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
#text2morse('.')
#playsound('dah')
