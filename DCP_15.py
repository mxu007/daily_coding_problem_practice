# binary search on sorted array
# implementing binary search can frequently be tricky, due to subtle off-by-off index errors
# use python bisect module

# log(n) time complexity
def binary_search(arr, x):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        if x == arr[mid]:
            return True, mid

        elif x < arr[mid]:
            high = mid - 1
        
        else: 
            low = mid + 1

    return False

if __name__  == "__main__":
    arr = [4,5,6,15, 29, 65, 88, 99, 190]
    print(binary_search(arr, 90))