# Dutch flag problem
# given an array of strictly the character R, G, and B, segregate the values of the array so that all the Rs come first, the Gs come second and the Bs come last. You can only swap elements of the array

# E.g. input ['G', 'B', 'R', 'R', 'B', 'G', 'G']
# Output: ['R', 'R', 'R', 'G', 'G', 'B', 'B']

# Do this in linear time and in-place

# The problem was posed with three colours, here `0′, `1′ and `2′. The array is divided into four sections:

# a[1..Lo-1] R
# a[Lo..Mid-1] G
# a[Mid..Hi] unknown
# a[Hi+1..N] B

# O(N) time complexity as it is single pass
# in-place update
class DNF:
    def __init__(self, arr):
        self.arr = arr
        print(self.arr)

    def partition(self):
        low, mid, high = 0, 0, len(self.arr) - 1
        while mid <= high:
            #print("begin of an iteration", low,mid,high)
            #  arr[mid] shall be 'G', hence swap 'B' to the front
            if self.arr[mid] == 'R':
                self.arr[low], self.arr[mid] = self.arr[mid], self.arr[low]
                low += 1
                mid += 1
            # case arr[mid] == 'B'
            # arr[mid] shall be 'G', hence swap 'B' to the back
            elif self.arr[mid] == 'B':
                self.arr[mid], self.arr[high] = self.arr[high], self.arr[mid]
                high -= 1

            else:
                mid += 1
            #print(self.arr)
            #print("after an iteration",low,mid,high)
                

if __name__ == "__main__":
    dnf = DNF(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
    dnf.partition()
    print(dnf.arr)
