# Bloom filter
# implement a data structure which carries out the following operations without re-sizing the underlying array:
# add(value): add a value to the set of values
# check(value): check whether a value is in the set

# the check method may return occasional false positive, but should always correctly identify a true element
# we cannot get around that bloom filter will occasionally return false positives. It is called a probabilitic data structure

# hash function takes O(1) time, so overall O(N) time where N is the size of the array
import hashlib
class BloomFilter:
    def __init__(self, n=1000, k=3):
        self.array = [False] * n
        # hashing each item in multiple ways, so that several values in the array will be set to True for any given input
        # return true if all of the locations have been set
        # reduce likelihood of collision by using more optimal hash functions
        # bloom filter will ocassionaly return false positive
        self.hash_algorithms = [
            hashlib.md5,
            hashlib.sha1,
            hashlib.sha256,
            hashlib.sha384,
            hashlib.sha512
        ]
        #print([f for f in self.hash_algorithms[:k]])
        self.hashes = [self._get_hash(f) for f in self.hash_algorithms[:k]]
        #print(self.hashes)


    def _get_hash(self,f):
        def hash_function(val):
            # hexdigest() : Returns the encoded data in hexadecimal format.
            h = f(str(val).encode('utf-8')).hexdigest()
            # convert hex to int
            return int(h,16) % len(self.array)
        return hash_function

    # set the hash location to be true
    def add(self,value):
        #print(self.hashes)
        for h in self.hashes:
            v = h(value)
            self.array[v] = True

    def check(self, value):
        for h in self.hashes:
            v = h(value)
            # check if hashed location is set to True
            if not self.array[v]:
                return False
        return True


if __name__ == "__main__":

    BF = BloomFilter(1000, 5)
    BF.add(10)
    BF.add(1)
    BF.add(8)
    BF.add(2)
    BF.add(3)

    print(BF.check(1))
    print(BF.check(10))
    print(BF.check(100))
