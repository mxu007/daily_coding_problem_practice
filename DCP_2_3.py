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


