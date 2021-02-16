# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

def first_unique_letter(string):
    # Remove spaces
    string = string.replace(" ", "")
    # Create a list that only has unique values
    string = [c for c in string if string.lower().count(c.lower()) == 1]
    # Return the first unique character if there is, if not return ""
    return string[0] if string else ""

def assert_function(actual, expected):
    assert actual == expected, f"Expected {expected}, but got {actual}"

assert_function(first_unique_letter("Google"), "l")
assert_function(first_unique_letter("Amazon"), "m")
assert_function(first_unique_letter("xoxoxo"), "")
assert_function(first_unique_letter("Hello World"), "H")
assert_function(first_unique_letter("   Spaces        will   be   removed"), "p")
