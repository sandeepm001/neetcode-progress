class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = []
        for ch in s:
            if ch.isalnum():
                temp.append(ch.lower())
        temp = ''.join(temp)
        return temp[::-1]==temp