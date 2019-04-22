# Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome

# E.G. Input ["code","edoc","da","d"] 
# Output: [(0,1),(1,0),(2,3)]

# O(n^2*c) time complexity where n is number of words and c is the length of the longest word
def palindrome_pairs(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                if (words[i]+words[j]) == (words[i]+words[j])[::-1]:
                    result.append((i,j)) 
    return result

# improved version, store all words into dicitonary as word-key index
# O(nc^2) time complexity, improved time as we only need to iterate throught the word list once
# usually the word list is much larger than the maximum length of a word
def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs_2(words):
    palindrome_dict = {}
    result = []

    for i, word in enumerate(words):
        palindrome_dict[word] = i
    
    for i, word in enumerate(words):
        for j in range(len(word)):
            pre, post = word[:j], word[j:]
            reverse_pre, reverse_post = pre[::-1], post[::-1]

            if(is_palindrome(pre)) and reverse_post in palindrome_dict:
                if i != palindrome_dict[reverse_post]:
                    result.append((palindrome_dict[reverse_post], i))

            if(is_palindrome(post)) and reverse_pre in palindrome_dict:
                if i != palindrome_dict[reverse_pre]:
                    result.append((i, palindrome_dict[reverse_pre])) 
    
    return result
