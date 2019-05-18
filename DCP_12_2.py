# Implement regular expression
# implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterik) which matches zero or more of the preceding element, remeber it's the character before * (preceeding)

# input: "ray", regex: "ra."
# output: True
# input: "raymond", regex: "ra."
# output: False

# match string s and regex r
# base case: r is empty, return True if s is also empty, and False otherwise
# first character in regex r is not succeeded by a * --> compare first character of both s and r
# if there is a match on the first character, we recursively continue to analyze match(r[1:], s[1:]). Otherwise we can return False
# the first character in r is in fact succeded by a *, we can try every suffix substring of s on r[2:] and return any of them provide a working solution


# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# this is basically matching the first character only, will be called by outer function matches
def matches_first_char(s,r):
    #print(s, r, len(s))
    if len(s) > 0:
        return s[0] == r[0] or (r[0] == "." and len(s) > 0)
    else:
        return False

# O(len(s)*len(r)) time and space complexity. potentially need to iterate over each suffix substring again for each character

def matches(s,r):
    # base case
    if r == "":
        return s == ""

    # case where the first character in r is NOT succeded by a *
    if len(r) == 1 or r[1] != "*":
        if matches_first_char(s,r):
            return matches(s[1:], r[1:])
        # no match
        else:
            return False
    # handle case where first character in r is followed by a *

    # recall that * matches ZERO or MORE of the preceding element
    else:
        # try zero length for preceeding elements e.g. r = x*abc, x can be repeated for 0 times
        if matches(s, r[2:]):
            return True

        # if that doesn't match staight away, try globbing more prefixes until the first character of the string doesn't match any more
        i = 0
        # i starts with 0, match first char with r
        # the while loop ensures earlier match of s[0] with r[0] starting with i =1, as this is the condition of the while loops
        while matches_first_char(s[i:], r):
            if matches(s[i+1:], r[2:]):
                return True
            # perform offset by 1 on i 
            i += 1
            #print(i, s[i:], s[i+1:])
        
        return False

if __name__ == "__main__":
    print(matches("ab", ".*"))
    print(matches("aab", "c*a*b"))
    print(matches("mississippi", "mis*is*p*"))
    print(matches("aa", "a"))
    print(matches("aa", "a*"))
    print(matches("ab", ".*c"))




        
    
