def is_reverse(original):
    reverse=''
    length = len(original)

    for j in range(length -2, -1, -1):
        reverse = reverse + original[j]
    return reverse


def is_palindrome():
    original=''

    i = 0
    j = 0

    original = input('Enter a string to check if it is a name ')
    length = len(original)

    print('length is ', length, ', string is ', original)

    reverse = is_reverse(original)

    if original == reverse:
        print('Entered string is a palindrome')
    else:
        print('Entered string is not a palindrome')

is_palindrome()


