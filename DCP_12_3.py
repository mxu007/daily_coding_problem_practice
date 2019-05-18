# Given an array of length n, find both the minimum and maximum using less than 2*(n-2) comparison


# each increment compares two times, total (n-1) * 2 comparison
# brute force
def min_and_max(arr):
    min_element, max_element = arr[0], arr[0]
    for i in range(1,len(arr)):
        min_element = arr[i] if arr[i] < min_element else min_element
        max_element = arr[i] if arr[i] > max_element else max_element
    
    return min_element, max_element

# improved version
def compare(x,y):
    return (x, y) if x < y else (y,x)

# O(n/2) *3  comparison from the compare function call, min function call and max function call
def min_and_max_1(arr):
    min_element, max_element = arr[0], arr[0]
    # take care of even number of arr elements, artificially add the last element again to the arr
    if len(arr) %2 == 0:
        arr.append(arr[-1])

    for i in range(1, len(arr), 2):
        #print(i, arr[i],arr[i+1])
        smaller, larger = compare(arr[i],arr[i+1])
        #rint(smaller,larger)
        min_element = min(min_element, smaller)
        max_element = max(max_element, larger)
        
    return min_element, max_element

# use divide-and-conquer
# T(n) = 2 * T(n/2) + 2 
# first 2 for the left and right split, second 2 for the min, max function call during the merge of result
# apply master theorem, O(n) time complexity
# detail induction shows total 3(n)-2 times of comparison
def min_and_max_2(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    elif len(arr) == 2:
        return (arr[0],arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    
    else:
        n = len(arr) // 2
        min_left, max_left = min_and_max(arr[:n])
        min_right, max_right = min_and_max(arr[n:])
        return min(min_left, min_right), max(max_left, max_right)

if __name__ == "__main__":
    arr = [4,2,7,5,-1,3,6]
    print(min_and_max(arr))
    print(min_and_max_1(arr))
    print(min_and_max_2(arr))
