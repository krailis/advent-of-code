def is_non_decreasing(digits):
    for i in range(1, len(digits)):
        if digits[i - 1] > digits[i]:
            return False
    return True


def has_double_digit_pair(digits):
    for i in range(1, len(digits)):
        if digits[i - 1] == digits[i]:
            return True
    return False


def pwd_count(low, high):
    possible_pwd_cnt = 0
    for pwd in range(low, high + 1):
        digits = list(map(int, list(str(pwd))))
        if not is_non_decreasing(digits):
            continue
        if not has_double_digit_pair(digits):
            continue
        possible_pwd_cnt += 1
    return possible_pwd_cnt


# Get solution for input
print(pwd_count(137683, 596253))
