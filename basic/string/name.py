# string represent by single or double quotes ('', "")
first_name = "ada"
last_name = 'lovelace'

# the some methods you can use strings
print(first_name.title()) # title() convert every each words begins with a capital letter
print(first_name.upper()) # upper() convert strings to uppercase
print(first_name.lower()) # upper() convert strings to lowercase

# formated string with f-strings
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

# stripping whitespaces on string
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip()) # rstrip() remove extra whitespace at the end of string

favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip()) # lstrip() remove extra whitespace at the beginning of string

favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip()) # strip() remove extra whitespace at the both sides