# Implement an autocomplete system. That is given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix

#  Eg. Input: [dog, deer, deal] query "de"
# Output: [deer, deal]

# when text completion arises in an interview, tries should be the first tool you search for

# O(N) time ,where N is no.of words in the dictionary
def autocomplete(s, words):
    result = set()
    for word in words:
        if word.startswith(s):
            result.add(word)

    return result


ENDS_HERE = '#' 
# improve time complexity, worst-case time complexity still O(N)
# but if words are uniformly distribted across alphabet, it will be on average much faster using trie
# trie can be thought as many trees with different root nodes, where root nodes are the starting letter of the prefix
# the more words share commom prefix, they more branches from the root node (first letter of the prefix)
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
        # trie stoes the existing words
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]   
            else:
                return []
        # the the prefix is in the trie, the deepest dictionary shall return True
        # return the trie to the depth of prefix
        print("found trie:", trie)
        return self._elements(trie)

    # d is the trie dictionary passed from the return call of find
    # creating combination on the remaining depth of the trie
    # the tricky part is the recursive call at self._element() on the val
    def _elements(self,d):
        result = []
        # iterate the remaining depth of the trie
        # d.items returns the key valu
        print(d.items())
        for key, val in d.items():
            print("current key:", key)
            if key == ENDS_HERE:
                subresult = ['']
            else:
                # recursive call, key+s iterable for all possible words under current key
                subresult = [key+s for s in self._elements(val)]
                print("subresult:", subresult)
            # append adds only single element, extend addds an iterable
            result.extend(subresult)
        
        print(result)
        return result

def autocomplete_2(s):
    return [s + w for w in trie.find(s)]


if __name__ == "__main__":
    words = ["dog", "deer", "deal"]
    s = "de"
    print(autocomplete(s,words))
    print("-----------")
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    print(autocomplete_2(s))
    

