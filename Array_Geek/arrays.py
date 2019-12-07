# def alternate(arr,n):
#     newarray = sum(zip(reversed(arr), arr), ())[:len(arr)]
#     print(newarray)


def merge(ar1, ar2, m, n):
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n - 1, -1, -1):

        # Find the smallest element
        # greater than ar2[i]. Move all
        # elements one position ahead
        # till the smallest greater
        # element is not found
        last = ar1[m - 1]
        j = m - 2
        while (j >= 0 and ar1[j] > ar2[i]):
            ar1[j + 1] = ar1[j]
            j -= 1
        # If there was a greater element
        if (j != m - 2 or last > ar2[i]):
            ar1[j + 1] = ar2[i]
            ar2[i] = last

def constructArr(arr,pair,n):
    arr [0] = (pair[0]+pair[1]-pair[n-1])//2
    print(arr[0])
    for i in range(1,n):
        print(pair[i-1])
        arr[i] = pair[i-1]-arr[0]


def printDistinct(arr,n):

    for i in range(0,n):
        d=0
        for j in range(0,i):
            if arr[i]==arr[j]:
                d=1
                break
        if(d == 0):
                print(arr[i])
def subarray(a,n):
    for i in range(0,n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(a[k], end=" ")
            print ("\n",end=" ")


def relativeComplement(arr11, arr22,m,n):

    for i in range(n):
        for j in range(m):
            if (arr11[i] == arr22[j]):
                break

        if (j == m-1):
             print(arr11[i], end=" ")

def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x

def leftRotate(aer, n, k) :
    for i in range(0,k):
        x = aer[0]
        for j in range(0,n-1):
            aer[j] = aer[j+1]
        aer[n-1]=x
if __name__ == "__main__":
    # arr = {7, 1, 2, 3, 4, 5, 6}
    # n=len(arr)
    # alternate(arr,n)


    # ar1 = [1, 5, 9, 10, 15, 20]
    # ar2 = [2, 3, 8, 13]
    # m = len(ar1)
    # n = len(ar2)
    #
    # merge(ar1, ar2, m, n)
    #
    # print("After Merging \nFirst Array:", end="")
    # for i in range(m):
    #     print(ar1[i], " ", end="")
    #
    # print("\nSecond Array: ", end="")
    # for i in range(n):
    #     print(ar2[i], " ", end="")


    pair = [15, 13, 11, 10, 12, 10, 9, 8, 7, 5]
    n = 5
    arr = [0] * n
    # constructArr(arr, pair, n)
    for i in range(n):
        print(arr[i], end=" ")

    arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
    n = len(arr)
    printDistinct(arr,n)


    a= [1,2,3,4]
    n = len(a)
    subarray(a,n)

    arr11 = [3, 6, 10, 12, 15]
    arr22 = [1, 3, 5, 10, 16]
    n= len(arr11)
    m= len(arr22)
    relativeComplement(arr11, arr22,m,n)

    arr = [12, 10, 5, 6, 52, 36]
    n = len(arr)
    k = 2

    splitArr(arr, n, k)

    for i in range(0, n):
        print(arr[i], end=' ')

    aer = [1, 3, 5, 7, 9]
    n = len(arr)
    k = 2
    leftRotate(aer, n, k)
