class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Solution(object):
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def _search(self, s):
        if len(s) == 0:
            return [[]]

        if s in self.cache:
            return self.cache[s]

        i = 0
        pCrawl = self.root
        res = []
        while i < len(s):
            index = self._charToIndex(s[i])
            if not pCrawl.children[index]:
                self.cache[s] = res
                return res
            pCrawl = pCrawl.children[index]
            if pCrawl.isEndOfWord:
                for lst in self._search(s[i + 1:]):
                    res.append([s[:i + 1]] + lst)

            i += 1

        self.cache[s] = res
        return res

    def wordBreak(self, s, wordDict):
        for word in wordDict:
            self.insert(word)

        self.cache = dict()

        return [' '.join(lst) for lst in self._search(s)]


if __name__ == '__main__':
    so = Solution()

    s = "leetcode"
    wordDict = ["leet", "code"]
    so.wordBreak(s, wordDict)

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    so.wordBreak(s, wordDict)

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    so.wordBreak(s, wordDict)
