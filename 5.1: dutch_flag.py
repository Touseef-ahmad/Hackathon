# The Dutch national flag problem

A = [0,1,2,0,2,1,3,4,5,6,7,7,8,9]
pivot = 8
temp = 0
def dutch_partitioner(list,pivot):
    low = 0
    high = len(list) - 1
    i = 0
    while i < len(list) and high >= low and i < high:

        if list[i] > pivot:
            temp = list[i]
            list[i] = list[high]
            list[high] = temp
            high-=1
        elif list[i] < pivot:
            temp = list[i]
            list[i] = list[low]
            list[low] = temp
            low+=1
            i+=1
        else:
            i+=1


dutch_partitioner(A,pivot)
print(A)