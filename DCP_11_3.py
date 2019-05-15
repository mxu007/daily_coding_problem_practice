# Bloom filter
# implement a data structure which carries out the following operations without re-sizing the underlying array:
# add(value): add a value to the set of values
# check(value): check whether a value is in the set

# the check method may return occasional false positive, but should always correctly identify a true element
# we cannot get around that bloom filter will occasionally return false positives. It is called a probabilitic data structure

import hashlib
class BloomFilter:
    def __init__(self, n=1000, k=3):
        self.array = [False] * n
        self.hash_algorithms = [
            hashlib.md5,
            hashlib.sha1,
            hashlib.sha256,
            hashlib.sha384,
            hashlib.sha512
        ]
        self.hashes = [self._get_hash(f) for f in self.hash_algorithms[:k]]

    def _get_hash(self,f):
        def hash_function(v):
            h = f(str(val).encode('utf-8')).hexdigest()
            return int(h,16) % len(self.array)
            return hash_function

    def add(self,value):
        for h in self.hashes:
            v = h(value)
            self.array[v] = True

    def check(self, value):
        for h in self.hashes:
            v = h(value)
            if not self.array[v]:
                return False
        return True