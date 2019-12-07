def rotateleft(array_one,size,difference):
    for i in range(difference):
        temp_array = array_one[0]
        for j in range(size - 1):
            array_one[j] = array_one[j + 1]
        array_one[size - 1] = temp_array
        print(array_one[size-1])

def printArray(array_one, size):
    for i in range(size):
        print("% d"% array_one[i], end =" ")


def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x


def search(arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

    if arr[l] <= arr[mid]:

        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)

    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)



if __name__ == "__main__":
    array_one=[1,2,3,4,5,6]
    size=len(array_one)
    difference= 2

    rotateleft(array_one,size,difference)
    # printArray(array_one,size)

    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print("Given array is")
    for i in range(0, n):
        print(arr[i], end=' ')

    rotate(arr, n)

    print("\nRotated array is")
    for i in range(0, n):
        print(arr[i], end=' ')

    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    i = search(arr,0,len(arr)-1,key)
    if i != -1:
        print("\nthe index is %d"%i)
    else:
        print("No key found")

    minimumArray=[2,4,6]
    min = min(minimumArray)
    print(min)




