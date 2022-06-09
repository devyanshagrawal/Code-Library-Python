''' Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. '''



def isIncMono(arr):
    flag = 0
    ##increasing
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            flag = 1
            break

    if flag == 0:
        print("It's monotonic")       
    else:
        print("It's not monotonic")    


def isDecMono(arr):
    flag = 0
    ##increasing
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            flag = 1
            break

    if flag == 0:
        print("It's monotonic")       
    else:
        print("It's not monotonic")     



arr = [1,2,3,4,56,6]
isIncMono(arr)        