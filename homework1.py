def palindrome(s: str):
    if s == s[::-1]:
        return True
    else:
        return False
    
print(palindrome("лепсспел"))
