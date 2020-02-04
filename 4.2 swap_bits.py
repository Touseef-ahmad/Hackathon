x = 73

def swap_bits(x , i , j):

    if (x >> i) & 1 != (x >> j) & 1:
        bitwise_mask = (1<<i)|(1<<j)
        x ^= bitwise_mask
    return x

y = swap_bits(x,1,6)

print(y)