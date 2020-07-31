class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = {}

        def find_words(string, word_dict):
            if string in dp:
                return dp[string]

            res = []
            for word in word_dict:
                if word == string[0:len(word)]:
                    new_string = string[len(word):]
                    if not new_string:
                        res += [word]
                    else:
                        res += [word + " " + w for w in find_words(new_string, word_dict)]

            dp[string] = res
            return res

        return find_words(s, wordDict)


s = Solution()

assert s.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]) == ['cats and dog', 'cat sand dog']
assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
assert s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]) == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
assert s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == []