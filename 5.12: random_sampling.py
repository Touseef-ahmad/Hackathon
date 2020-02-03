import random
A = [1,2,3,4,5,6]

def random_sampling(k , A):

    for i in range(k):
        r = random.randint(i , len(A) - 1)

        A[r] , A[i] = A[i] , A[r]

random_sampling(3, A)
print(A)