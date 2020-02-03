def power_function(x,y):
    power , result = y , 1.0
    if y < 0:
        power , x = -power , 1.0/x
    while power:
        if power & 1:
            result *= x
        x , power = x*x , power>>1
    return result

print(power_function(2,2))