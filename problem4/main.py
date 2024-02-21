def palindrome(input_string):
    reverse_str=input_string[::-1]
    if reverse_str==input_string: return True
    else: return False


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False