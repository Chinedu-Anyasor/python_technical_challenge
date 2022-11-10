
"""Rite  a  Python  program  that  checks  if  a  string  is  a palindrome,  Then  optionally  write  a  unit  test
to  check your program's correctness. """
"""A palindrome is a string that reads the same forwards and backwards."""


def palindrome_check(main_list, user_string):
    # reversing the list
    inverse_list = main_list[::-1]

    # comparing reversed_list to original_list to
    # determine if the original_list is a palindrome
    if main_list == inverse_list:
        print("'" + user_string.lower() + "' is a palindrome.")
    else:
        print("'" + user_string.lower() + "' is not a palindrome!")


def main():
    # promting user to input a word or phrase
    user_string = input("Enter string: Madam ")

    user_list = list(user_string.lower())

    # putting our palindrome_function() to use
    palindrome_check(user_list, user_string)


if __name__ == "__main__":
    main()
