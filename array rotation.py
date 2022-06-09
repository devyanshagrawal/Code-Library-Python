''' array rotation '''

arr = [1,2,3,4,5,6,7,8]
rotate_by = int(input())
for i in range(rotate_by):
    arr1 = []
    arr1.append(arr[-1])
    arr1 = arr1+arr[:-1]
    arr = arr1

print("Rotation of array = ",arr1)