# 1.1 Get product of all other elements
# Given an array of integers, return a new array such taht each element at index i of the new array is the product of all the numbers in the original array excpet the one at i

# E.g. Input: [1,2,3,4,5]
# Output: [120 60, 60, 40, 30, 24]

# Input: [3,2,1]
# Output: [2,3,6]

# 1) calculate the product of all elements, then use division: total_product/current_value and append to the list
# O(N) time complexity, O(N) space
def product_of_other_elements_1(x):
    product = 1
    for item in x:
        product *= item
    
    result = []
    for item in x:
        result.append(int(product/item))
    
    return result


# 2) if division is not allowed to use, outer for loop to iterate each element in the list
# inner loop to compute others product for each element 
# O(N^2) time complexity, O(N) space, brute-force
def product_of_other_elements_2(x):
    result = []
    for i in range(len(x)):
        others_product = 1
        for j in range(len(x)):
            if j != i:
                others_product *= x[j]
        result.append(others_product)
    
    return result


# 3) optimized solution, trying to reduce time complexity from O(N^2) to O(N)
# requires two array, one stroes products from left to right, another stores from right to left
# the for a specif item, its product of other elements is simply multiplying prefix product and postfix product
# three-pass appraoch
def product_of_other_elements_3(x):
    
    prefix_list = [1]
    product_prefix = 1
    
    for i in range(1,len(x)):
        product_prefix = product_prefix * x[i-1]
        prefix_list.append(product_prefix)
    
    postfix_list = [1]*len(x)
    product_postfix = 1
    
    for i in range(len(x)-2,-1,-1):
        product_postfix = product_postfix * x[i+1]
        postfix_list[i] = product_postfix
    
    result = []
    # print(prefix_list)
    # print(postfix_list)

    for i in range(len(x)):
        result.append(prefix_list[i] * postfix_list[i])
    
    return result


# 4) solution by the book
def product_of_other_elements_4(nums):
    
    # construct prefix_products list
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1]*num)
        else:
            prefix_products.append(num)
    
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    
    suffix_products = list(reversed(suffix_products))

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    
    return result

