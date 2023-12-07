def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitivity
    return s == s[::-1]
# Example
input_str = "radar"
result = is_palindrome(input_str)
print(f"Is '{input_str}' a palindrome? {result}")