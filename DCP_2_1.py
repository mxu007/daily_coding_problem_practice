# Find anagram
# Given a word w and a string s, find all indices in s which are the starting locations of anagrams of w

# Eg. Input w = ab, s = abxaba
# Output [0,3,4]

# use default dictionary, time complexity of O(ws), space complexity of O(s)
# stores the letter and count in dictionary, then compare the dictionary
import collections
def find_anagram (w, s):
    len_anagram = len(w)
    w_dict = collections.defaultdict(int)
    result = []

    for letter in w:
        w_dict[letter] += 1

    for i in range(0,len(s)-len_anagram+1):
        s_dict = collections.defaultdict(int)
        for letter in s[i:i+len_anagram]:
            s_dict[letter] += 1
        if w_dict == s_dict:
            result.append(i)
    return result


# >>> from collections import Counter
# >>> Counter("ab")
# Counter({'a': 1, 'b': 1})

# similar appraoch but use Counter, passing string to python Counter returns a dictionary of character occurence
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def find_anagram_2(w, s):
    result = []
    for i in range(len(s)-len(w)+1):
        window = s[i:i+len(w)]
        if is_anagram(window,w):
            result.append(i)

    return result


# single pass, O(s), still not ideal because of comparing two dictionary
import collections
def find_anagram_3 (w, s):
    len_anagram = len(w)
    w_dict, s_dict = collections.defaultdict(int), collections.defaultdict(int)
    result = []

    for letter in w:
        w_dict[letter] += 1
    
    for letter in s[0:len(w)]:
        s_dict[letter] += 1

    if w_dict == s_dict:
        result.append(0)

    for i in range(len(w),len(s)):
        s_dict[s[i-len(w)]] -= 1
        if s_dict[s[i-len(w)]] <= 0:
            del s_dict[s[i-len(w)]]

        s_dict[s[i]] += 1
        if w_dict == s_dict:
            result.append(i)
    return result

# single dictionary for update, adding/removing with the sliding winwod, O(s) time and space complexity
# assume the begining of s is a anagram, freq becomes empty, so sliding window adding start_char and removing end_char, if these 2 cancel out each other, the sliding window has an anagram, if not just update the dictionary freq.. As long as there are cancel out and eventually make the freq empty again, we find another anagram
def del_if_zero(dict, char):
    if dict[char] == 0:
        # delete the key
        del dict[char]

def find_anagram_4(w,s):
    result = []
    freq = collections.defaultdict(int)

    for char in w:
        freq[char] += 1
    
    for char in s[:len(w)]:
        freq[char] -= 1
        del_if_zero(freq,char)
    
    # freq is empty, means a match anagram
    if not freq:
        result.append(0)

    for i in range(len(w),len(s)):
        start_char, end_char = s[i-len(w)], s[i]
        freq[start_char] += 1
        del_if_zero(freq,start_char)

        freq[end_char] -= 1
        del_if_zero(freq, end_char)

        if not freq:
            beginning_index = i - len(w) + 1
            result.append(beginning_index)

    return result
 
        
        
