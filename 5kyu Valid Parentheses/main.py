def valid_parentheses(string):
    left = 0
    right = 0
    for i in string:
        if left - right < 0:
            return False
        if i == "(":
            left += 1
        if i == ")":
            right += 1
    if left - right == 0:
        return True
    else:
        return False
