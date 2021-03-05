# def multiply(x,y):
#     result = x * y
#     return result


# answer  = multiply(10.5,4)
# print(answer)
test = "Was it a car, or a cat, I saw?"
def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return string

attempt = palindrome_sentence(test)

if is_palindrome(attempt):
    print("'{}' is a palindrome".format(attempt))
else:
    print("'{}' is not a palindrome".format(attempt))