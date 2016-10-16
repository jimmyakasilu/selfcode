def number(i,maxlenbin):
    num=str(i)
    return num.rjust(maxlenbin)
def octal(i,maxlenbin):
    octlist=[]
    num = i
    while num != 0:
        lenoct = len(octlist)
        octlist.insert(-1-lenoct,str(num%8))
        num = num/8
    octal = ''.join(octlist)
    return octal.rjust(maxlenbin)
def hexadecimal(i,maxlenbin):
    hexlist=[]
    num = i
    hexdict = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
    while num != 0:
        lenhex = len(hexlist)
        rem = num%16
        hexlist.insert(-1-lenhex,hexdict[str(rem)])
        num = num/16
    hexadecimal = ''.join(hexlist)
    return hexadecimal.rjust(maxlenbin)
def binary(i,maxlenbin=0):
    binlist=[]
    num = i
    while num != 0:
        lenbin = len(binlist)
        binlist.insert(-1-lenbin,str(num%2))
        num = num/2
    binary = ''.join(binlist)
    return binary.rjust(maxlenbin)
N= int(raw_input('N: '))
maxlenbin = len(binary(N))
for i in range(1,N+1):
    print number(i,maxlenbin), octal(i,maxlenbin), hexadecimal(i,maxlenbin), binary(i,maxlenbin)

                    
    
