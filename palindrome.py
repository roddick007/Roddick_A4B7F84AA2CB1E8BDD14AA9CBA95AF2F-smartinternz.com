def palindrome(string):
    if string == string[::-1]:  
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."

string = input("Enter a string: ")
print(palindrome(string))
