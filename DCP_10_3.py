# Create stepword chain
# given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence rom start to end such taht only one letter is changed at each step of teh sequence, and each transformed word exists in the dictionary
# if there is no possible transformation, return null. Each word in the dictionary has the same length as start and end and is lowercase

# E.g. start = "dog" end = "cat", and dictionary = {"dot", "dop","dat","cat"}
# return ["dog", "dot", "dat", "cat"]

# model this problem as graph. the node will be the words in the dictionary, and we can form an edge between two nodes if and only if one character can be modified in one word to get to the other

# BFS search starting from start and finishing once we encounter the end
# why bfs? because we want the shortest transformation, the deeper we traverse the tree, the longer the transformation

from collections import deque
from string import ascii_lowercase

# O(N^2) time where N is no.of words
# O(N) for pop and append to the queue
# another O(N) for the inner loop to check if next_word is in words
# O(N) space for the queue
def word_ladder(start, end, words):
    # pop the tuple(node, path)
    queue = deque([(start, [start])])

    # bfs using deque
    while queue:
        word, path = queue.popleft()
        # if matching the end
        if word == end:
            return path
        
        for i in range(len(word)):
            # ascii_lowercase = abcdefghijklmnopqrstuvwxyz
            for char in ascii_lowercase:
                next_word = word[:i] + char + word[i+1:]
                # add possible mutation into the queue and remove from words
                # the iteration is controlled by the queue, so it is fine of removing element from words, where words is the input list
                # O(N) time for *in* operation here
                if next_word in words:
                    words.remove(next_word)
                    queue.append([next_word, path + [next_word]])
    return None

if __name__ == "__main__":
    words = ["dot", "dop","dat","cat"]
    print(word_ladder("dog", "cat",words))