class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.capitalize() or word == word.upper() or word == word.lower():
            return True
        return False


s = Solution()
assert s.detectCapitalUse("USA") is True
assert s.detectCapitalUse("FlaG") is False