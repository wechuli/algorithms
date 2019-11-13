def is_palindrome(words):
    array = list(words)
    array.reverse()
    return ''.join(array) == words


print(is_palindrome('awesome'))
print(is_palindrome('foobar'))
print(is_palindrome('tacocat'))
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('amanaplanacanalpandemonium'))
