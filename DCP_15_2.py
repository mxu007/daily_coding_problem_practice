# pancake sort
# given a list ,sort it using the helper method reverse(lst, i, j)

# This method takes a sublist as indicted by the left and right bounds i and j and reverse all its elements. 
# E.g. reverse([10,20,30,40,50], 1, 3) would result in [10, 40, 30, 20, 50]

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

# the idea is iteratively place the maximum remaining element at the END OF THE LIST

# The outer loops take O(n) time to decrement from n to 1, shrink the window from right to left
# the inner  max_pos and reverse takes O(n) time
# overall O(n^2) time and O(1) space for the max_ind
def pancake_sort(lst):
    # reduce the sorting window
    for size in reversed(range(len(lst))):
        #print(size)
        # find the index of largest element given the current window, assumping largest item has been thrown to the last of lst
        max_ind = max_pos(lst[:size+1])
        print("before first reverse", lst, size, max_ind)
        # reverse first time between 0 to index of max element, this put the maximum item to the front
        reverse(lst, 0, max_ind)
        print("after first reverse", lst, size, max_ind)
        # reverse second time between 0 to current window size, this put the maximum item to the last before the largest element in the previous iteration
        reverse(lst, 0, size)
        print("after second reverse", lst, size, max_ind)
        print("")
    
    return lst

def max_pos(lst):
    #print(lst, lst.index(max(lst)))
    return lst.index(max(lst))
    
def reverse(lst, i, j):
        #print(lst, i, j)
        lst[i:j+1] = lst[i:j+1][::-1]
        #print(lst, i, j)
        return lst

if __name__ == "__main__":
    lst = [10, 40, 30, 20, 50]
    print(pancake_sort(lst))
