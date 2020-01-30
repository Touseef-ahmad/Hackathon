# 4.1 Computing the parity of a word
# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.

# obvious solution 
# The brute-force algorithm iteratively tests the value 
# of each bit while tracking the number of 1s seen so far
def parity_brute_force(x):
    result = 0
    while x:
        
        result ^= x & 1
        x>>=1
        
    return result
x = 0x00100111

print(parity_brute_force(x))

# solution
def parity(x):
    result = 0
    while x:
        
        result ^= 1

        x &= x-1 # drops lowest set bit of x
    return result