# Create Prefix MapSum class
# Implement a PrefixMapSum class with the following methods
# insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite that value
# sum(prefix: str): Return the sum of all values of keys that begin with a given prefix

# E.g. 
# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3

# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5

# use python dictionary
# sum takes O(n*k) time complexity where n is no.of words, and k is the length of the prefix
# O(1) for insertion
# save the words in dictionary and compute the sum on demand
class PrefixMapSum:
    def __int__(self):
        self.map = {}

    def insert(self, key:str, value:int):
        self.map[key] = value
    
    def sum_prefix(self, prefix):
        returm sum([val for key,val in self.map.items() if key.startswith(prefix)])
    

# inserting new words and make sum operation to be more efficient
# save the words in the set and sum(prefix as key) in the dictionary
# O(1) sum computation
# O(k^2) time for insertion, 
from collections import defaultdict
class PrefixMapSum_1:
    def __init__(self):
        self.map = defaultdict(int)
        # words are now in a set
        self.words = set()

    def insert(self, key:str, value:int):
        if key in self.words:
            value -= self.map[key]
        self.words.add(key)

        # equivalent to the key.startswith operation
        # updatet the sum of all possible prefix derieved from this newly inserted key
        # O(k) for the for loop
        # O(k) for the slicing
        # slicking is O(k), https://wiki.python.org/moin/TimeComplexity
        for i in range(1, len(key)+1):
            self.map[key[:i]] += value
    
    def sum(self,prefix):
        return self.map[prefix]

if __name__ == "__main__":
     pfm = PrefixMapSum()
     pfm.add("happy",2)
     pfm.add("halo", 3)
     pfm.add("hapiness",5)

     print(pfm.sum_prefix("ha"))