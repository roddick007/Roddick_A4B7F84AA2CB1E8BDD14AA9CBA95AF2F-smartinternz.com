def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():  
            lowercase_letter_count += 1

    print("Count of uppercase letters:", uppercase_letter_count)
    print("Count of lowercase letters:", lowercase_letter_count)

count_upper_lower("Hello, How are you? How was your day?")
