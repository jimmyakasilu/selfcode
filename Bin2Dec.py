def bin2dec():
    binary = raw_input('Binary: ')
    n = len(binary)
    print binary 
    print n
    dec = 0
    for b in binary:
        expo = 2**(n-1)
        dec = dec + expo*int(b)
        n=n-1
    print dec
bin2dec()
