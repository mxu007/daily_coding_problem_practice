# Given a string a number of lines k, print the string in zigzagform. In zigzag, characters are printed out diagonally from top left to bottom right until readching the kth line, the back up to top right and so on.

# Eg. Input "thisisazigzag" and k = 4
# Output
# t       a       g
#  h     s z     a
#    i  i   i   z
#      s      g


# create dictionary to map the (row_id, col_id) as key to the letter as value
# mod is the number we perform modulation on, e.g. k=4, mod=6
# handle the case of column_id % mod smaller/equal to half of mod or otherwise, this decides the movement is downward or upward to derive the row index
# O(mk) time complexity, where m is length of sentence string and k is number of rows
# O(m) space complexity as we init empty string for each row

def print_zigzag(sentence, k):
    letter_dic = {}
    mod = k * 2 -2

    for column_id, letter in enumerate(sentence):
        if column_id % mod <= (mod/2):
            row_id = column_id % mod
        else:
            row_id = mod - (column_id % mod)
        letter_dic[(row_id,column_id)] = letter
    
    for i in range(k):
        result = ""
        for j in range(len(sentence)):
            if (i,j) in letter_dic:
                result += (letter_dic[(i,j)])
            else: 
                result += " "
        print(result)

    return


# determine space between two letters in the same row, constant time
def get_spaces(row, desc, k):
    max_spaces = (k-1) * 2 -1
    if desc:
        spaces = max_spaces - row * 2
    else:
        spaces = max_spaces - (k - 1 -row) * 2
    return spaces

# decide whether the part is ascending or descending, constant time
def is_descending(index, k):
    return index % (2 * (k-1)) < k-1

# O(kn) time, where n is the length of sentence string
# calculate the space between two consecutive letters in each line
# space is the offset index in the original sentence string
def print_zigzag_2(sentence, k):
    n = len(sentence)

    for row in range(k):
        i = row
        line = [" " for _ in range(n)]

        while i < n:
            line[i] = sentence[i]
            desc = is_descending(i,k)
            spaces = get_spaces(row, desc, k)
            i += spaces + 1
    
        print("".join(line))


