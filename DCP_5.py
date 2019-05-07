# Givenn a list of numbers and a number k, return whether any two numbers from the list add up to k.

# E.g. Input: [10, 15, 3, 7] and k=17
# Output: True


def two_sum(lst, k):
    lst_dict = {}

    for item in lst:
        if (k - item) in lst:
            return True
        else:
            lst_dict[item] = True
    
    return False


if __name__ == "__main__":
    lst = [10, 15, 3, 7] 
    k = 15
    print(two_sum(lst,k))