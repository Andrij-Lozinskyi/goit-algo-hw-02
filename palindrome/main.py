from collections import deque

def is_palindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    char_deque = deque(normalized_str)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True