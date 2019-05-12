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
    def __init__(self):
        self.map = {}

    def insert(self, key:str, value:int):
        self.map[key] = value
    
    def sum_prefix(self, prefix):
        #print(self.map.items())
        return sum([val for key,val in self.map.items() if key.startswith(prefix)])
    

# less frequent of inserting new words and make sum operation to be more efficient
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
    
    def sum_prefix(self,prefix):
        return self.map[prefix]


# whenever a problem involves prefixes, a trie hould be one of your go-to options
# O(k) time complexity for both insert and sum_prefix as it just need to iterate through all letters of input key
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.letters = {}
        self.total = 0

class PrefixMapSum_2:
    def __init__(self):
        self._trie = TrieNode()
        self.map = {}

    def insert(self, key:str, value: int):
        # the reason of only adding the delta of the value
        # is due to previously the sum of prefix of key has been already comprehended in the self.total
        # hence we only update the delta respect to the original key
        value -= self.map.get(key,0)
        self.map[key] = value

        trie = self._trie
        for char in key:
            # create new trie node
            # each trie node comes with letters and total
            if char not in trie.letters:
                trie.letters[char] = TrieNode()
            # go to a detter trie
            trie = trie.letters[char]
            trie.total += value

    def sum_prefix(self,prefix):
        d = self._trie
        for char in prefix:
            if char in d.letters:
                d = d.letters[char]
            else:
                return 0
        return d.total


if __name__ == "__main__":
    pfm = PrefixMapSum()
    pfm.insert("happy",2)
    pfm.insert("halo", 3)
    pfm.insert("hapiness",5)
    print(pfm.sum_prefix("ha"))

    pfm_1 = PrefixMapSum_1()
    pfm_1.insert("happy",2)
    pfm_1.insert("halo", 3)
    pfm_1.insert("hapiness",5)
    print(pfm_1.sum_prefix("ha"))

    pfm_2 = PrefixMapSum_2()
    pfm_2.insert("happy",2)
    pfm_2.insert("happy",100)
    pfm_2.insert("halo", 3)
    pfm_2.insert("hapiness",5)
    print(pfm_2.sum_prefix("ha"))