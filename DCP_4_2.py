# Given a string of round, curly and square opening and closing brackets, return whether the brackets are ballanced (well-formed)

# For example, Input: "([])[]({})"
# Output: True

# Input: "([)]" or "((()"
# Output: False

# O(N) time and O(N) space where N is no.of characters in the input string
def check_balance(input_string):
    stack = []
    for char in input_string:
        if char in ["(","{","["]:
            stack.append(char)
            print(stack)
        
        else:
            if len(stack) == 0:
                return False
            else:
                if (char == "]" and stack[-1] != "[") or (char == "}" and stack[-1] != "{") or (char == ")" and stack[-1] != "("):
                    return False
                stack.pop()
                print(stack)

    return len(stack) == 0


if __name__ == '__main__':
    input_string = "([)]"
    print("Input:",input_string)
    print(check_balance(input_string))

