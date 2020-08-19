class Solution:
    def toGoatLatin(self, S: str) -> str:
        result = ''
        for idx, word in enumerate(S.split(' ')):
            result += word if word[0].lower() in 'aeiou' else word[1:] + word[0]
            result += 'ma' + ('a' * (idx + 1)) + ' '
        return result.strip()


s = Solution()

assert s.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert s.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
assert s.toGoatLatin("Each word consists of lowercase and uppercase letters only") == "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"
