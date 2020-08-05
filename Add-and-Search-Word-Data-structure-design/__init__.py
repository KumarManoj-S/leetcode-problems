class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        def _add(w, trie):
            if len(w) == 0:
                return {}
            try:
                trie[w[0]][1].update(_add(w[1:], trie[w[0]][1]))
            except KeyError:
                trie[w[0]] = [False]
                trie[w[0]].append(_add(w[1:], {}))
            if not w[1:]:
                trie[w[0]][0] = True
            return trie
        self.trie = _add(word, self.trie)

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return False

        def _search(w, trie):
            if w[0] == '.':
                if not w[1:]:
                    res = []
                    for k, v in trie.items():
                        res.append(v[0])
                    return any(res)
                res = []
                for k, v in trie.items():
                    res.append(_search(w[1:], v[1]))

                return any(res)

            if w[0] not in trie:
                return False

            if not w[1:]:
                return trie[w[0]][0]

            return _search(w[1:], trie[w[0]][1])
        return _search(word, self.trie)


t = WordDictionary()

t.addWord("a")
t.addWord("ab")
assert t.search("a") is True
assert t.search("ab") is True
assert t.search(".a") is False
assert t.search(".b") is True
assert t.search("ab.") is False
assert t.search(".") is True
assert t.search("..") is True
