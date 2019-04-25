# You are given a string of length n and an integer k. The string can be manipulated by taking one of the first k letters and moving it to the end of string. 

# write program to determine the lexicographically smallest string that can be created after an unlimited number of moves

# E.g. input: string = 'daily' and k = 1
# output = 'ailyd'

# possible manipulation 
# 'ailyd', 'ilyda', 'lydai', 'ydail', 'daily'

# if k >= 2, remeber we can only take ONE of the first k letters and moving it to the end
# e.g. k == 2, for pattern 'xxbaxx', we want 'a' ahead of 'b'
# 'xxbaxx'
# 'xbaxxx'
# 'baxxxx' takng one ('a') and move it to the end
# 'bxxxxa' 
# 'xxxxab'
# ...
# 'abxxxx' 'ba' has been sorted
# so the above example shows that when k>=2, the problem simply becomes finding the sorted string as we are allowed to manipulate for unlimited number of moves


# O(NlogN) time complexity from the python sorted function (K >= 2)
# O(N^2) time complexity for n iterations the length of list, each time the lexicograhically comparison compares all the letters in the string, O(N) for each comparison (K == 1)
# O(N) space complexit to store smallest

def smallest_roated_str(string, k):
    string_list = list(string)
    smallest = string_list
    if k == 1:
        for i in range(len(string_list)):
            if string_list[i:] + string_list[:i] < smallest:
                smallest = string_list[i:] + string_list[:i] 
    else:
        smallest = sorted(string_list)
    
    return ('').join(smallest)
