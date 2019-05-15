# You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following

# update(hour, value): increment the element at index hour by value
# query(start, end): Retrieve the number of subscribers that have signed up between start and end (inclusive)

# The data strcutre required efficiently supports finding the sum of a subarray, and updating individual values in the array
# Fenwick tree, every numbers can be represented as sum of powers of 2

# in worst case we are querying binary representation of all ones (2^n -1), which translate to log(n) operations
# O(log(n)) time complexity for update and query where n is the number of elements due to the 2-powe sum in self.tree

# cannot add/remove the original array num
# the position of the least significant bit (LSB) determines the range of responsibility that cell has to the cells below itself

# https://www.youtube.com/watch?v=RgITNht_f4Q
# https://www.youtube.com/watch?v=BHPez138yX8
class BIT:
    def __init__(self, nums):
        self.tree = [0 for _ in range(len(nums)+1)]
        for i, num in enumerate(nums):
            # offset for 1-indexed
            self.update(i+1, num)
        print(self.tree)
    
    # actual tree is a list/array which alternatively stores the sum
    # if the index is even, simply store the value of subscribers[i]
    # if the index is odd, store the sum of range of values up to i whose length is a power of two
    # for update to increment index
    def update(self, index, value):
        # update start from the index, he value at index impacts all tree value with index above this input index
        while index < len(self.tree):
            # trick to get the lowest (first from the right) set bit 
            # only update on index that has dependence on current index
            self.tree[index] += value
            # then remove that bit from index, essentially reduce power of 2 from index
            index += index & -index
    
    # for query to decrement inde
    def query(self, index):
        total = 0 
        while index > 0:
            total += self.tree[index]
            # flip the right-most set bit
            index -= index & -index
        return total

class Subscribers:
    def __init__(self, nums):
        self.bit = BIT(nums)
        self.nums = nums

    # nums represented both in bit and regular list
    def update(self, hour, value):
        self.bit.update(hour, value - self.nums[hour])
        self.nums[hour] = val

    def query(self, start, end):
        # shift start and end indeices forward as our array is 1-based
        return self.bit.query(end + 1) - self.bit.query(start)

if __name__ == "__main__":
    nums = [4,8,1,9,3,5,5,3]
    print("nums:", nums)
    subs = Subscribers(nums)
    print("subs.query(0,6):", subs.query(0,6))
    print("subs.query(1,2):", subs.query(1,2))
    print("subs.query(0,0):", subs.query(0,0))
    print("subs.query(3,7):", subs.query(3,7))


