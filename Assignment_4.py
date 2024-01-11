def is_palindrome(input_str):

    cleaned_str = input_str.lower().replace(" ", "")
    return cleaned_str == cleaned_str[::-1]


user_input = input("Enter a number " )

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")