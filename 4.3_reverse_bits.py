#!/usr/bin/python

PRECOMPUTED_REVERSE = {
	0b00:0b00,
	0b01:0b10,
	0b10:0b01,
	0b11:0b11,
}

def reverse_bits(x):
	"""this function reverses bits of given 8 bit integer"""
	BIT_MASK = 0b11
	return (PRECOMPUTED_REVERSE[x & BIT_MASK] << 6 | 
	PRECOMPUTED_REVERSE[(x >> 2) & BIT_MASK] << 4 | 
	PRECOMPUTED_REVERSE[(x >> 4) & BIT_MASK] << 2 | 
	PRECOMPUTED_REVERSE[(x >> 6) & BIT_MASK])

def main():
	x = 1
	print(reverse_bits(x))

if __name__ == "__main__":
	main()
