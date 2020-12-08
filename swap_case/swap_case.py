def swap_case(s):
    if 0 < len(s) <= 1000:
        return s.swapcase()


if __name__ == '__main__':
    user_input = input()
    result = swap_case(user_input)
    print(result)
