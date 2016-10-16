String = raw_input("Enter string: ").split(' ')
print (String)
String2=[]
for word in  String:
    string = word
    string2=''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for l in string:
        if l in lower:
            string2+=l.upper()
        elif l in upper:
            string2+=l.lower()
        else:
            string2+=l
    print (string2)
    String2.append(string2)
print ' '.join(String2)
