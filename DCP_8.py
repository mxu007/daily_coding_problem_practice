# Trie 
# Two main methods in tries:
# insert(word): add a word to the trie
# find(word): check if a word or prefix exist in the tires

ENDS_HERE = '#' 

class Trie:
    def __init__(self):
        self._trie = {}

    # O(k) time complexity for find and insert, where k is the length of the word
    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            # recursive re-assignment of trie
            trie = trie[char]
        
        trie[ENDS_HERE] = True


    def find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            
            else:
                return None
        # the the prefix is in the trie, the deepest dictionary shall return True
        return trie

if __name__ == "__main__":
    trie = Trie()
    trie.insert("happy")
    
    print(trie._trie)
    print(trie.find("happy"))
    print(trie.find("happyy"))