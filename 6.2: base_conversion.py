import string

def convert_from_base(num , base):
    if num == 0:
        return ''
    return convert_from_base(num//base , base) + string.hexdigits[num % base]


