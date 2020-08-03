class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return s == s[::-1]


s = Solution()

assert s.isPalindrome("A man, a plan, a canal: Panama") is True
assert s.isPalindrome("race a car") is False
assert s.isPalindrome(" ") is True
