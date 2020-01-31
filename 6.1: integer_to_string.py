def str(x):
    is_negative = False
    if x<0:
        is_negative = True
        x = -x
    s = []
    while x:
        
        s.append(chr(ord('0') + x % 10))
        x//=10
    
    return ('-' if is_negative else '')+''.join(reversed(s))


print(str(-1000))