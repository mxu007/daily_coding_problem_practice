# You have a large array, most of whole elements are zero. Create a more space-efficient data strcture, SparseArray, that implements the following interface:
# init(arr,size): initialize with the original large array and size
# set(i,val): update index at i to be val
# get(i): get the value at index i


# save only non-zero values and their index into the dictionary
class SparseArray:
    def __init__(self,arr,n):
        self.n = n
        self._dict = {}
        for i, e in enumerate(arr):
            if e != 0:
                self._dict[i] = e
    
    def _check_bounds(self,i):
        if i <0 or i >= self.n:
            raise IndexError('out of bounds')

    def set(self,i,val):
        self._check_bounds(i)
        if val != 0:
            self._dict[i] = val
            return
        # zero value, direct delete it from the dictioanry
        elif i in self._dict:
            del self._dict[i]

    def get(self,i):
        self._check_bounds(i)
        return self._dict.get(i,0)

if __name__ == "__main__":
    lst = SparseArray([1,2,3,0,0,0,0,0,0,4,3,2,1,1,2],15)
    print(lst.get(0))
    print(lst._dict)
    lst.set(0,1000)
    print(lst._dict)
    lst.set(20,1)
    print(lst.get(1000))
