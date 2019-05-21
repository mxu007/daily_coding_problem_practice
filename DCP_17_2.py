# Implement Division without / or * operators

# decimal division: we subtract the product from the dividend to get the remainder. The remainder is initially the value x. We can abstract this process into subtracting the largest multiple of y*(10^d) from the remainder where d is the place of the digit
# consider the left-most digit that can be divided by the divisor, at each step, the quotient becomes the first digit of the result
# similiary using shift, finding the largest value of y * (2^d), then test  y * (2^(d-1))... until the remainder is less than y

# O(n) time where n is no.bits to represent x/y as x/y determines how many bits the quotient result has
def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Divided by Zero")

    # quotient is the result
    quotient = 0
    # y power starts at y^32
    power = 32
    y_power = y << power 
    
    # init remainder to be x
    remainder = x

    # compare remainder with y to determine stoping point
    while remainder >= y:
        # find the y_power that just become smaller than remainder
        while y_power > remainder:
            # right shift y power
            y_power = y_power >> 1
            power -= 1
        
        # once find the right power in binary, set the bit in quotient
        quotient  = quotient + (1 << power)
        # decrement from remainder on product of quotient and power (which is actually y_power)
        remainder -= y_power

    return quotient


if __name__ == "__main__":
    x, y = 31, 3
    print(divide(x,y))