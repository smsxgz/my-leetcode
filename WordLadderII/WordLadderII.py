from collections import defaultdict


class Solution(object):
    def build_graph(self, wordSet, wordLength):
        ascii_lowercase = set('abcdefghijklmnopqrstuvwxyz')
        graph = defaultdict(list)

        for word in wordSet:
            for t in range(wordLength):
                first, second = word[:t], word[t + 1:]
                for ch in ascii_lowercase:
                    combined_word = first + ch + second
                    if ch != word[t] and combined_word in wordSet:
                        graph[word].append(combined_word)
        return graph

    def findLadders1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

        m = len(beginWord)
        if m == 1:
            return [[beginWord, endWord]]

        lth = len(wordList) + 1
        graph = self.build_graph(set(wordList + [beginWord]), m)
        saved = {beginWord: [[beginWord]]}
        nodes = [beginWord]
        while nodes:
            word = nodes.pop(0)
            paths = saved[word]
            if len(paths[0]) + 1 > lth:
                return saved.get(endWord, [])
            for w in graph[word]:
                if w in saved:
                    if len(paths[0]) + 1 > len(saved[w][0]):
                        continue
                    else:
                        saved[w].extend([p + [w] for p in paths])
                else:
                    nodes.append(w)
                    saved[w] = [p + [w] for p in paths]

                if w == endWord:
                    lth = len(saved[w][0])
        return saved.get(endWord, [])

    def findLadders2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        ascii_lowercase = set('abcdefghijklmnopqrstuvwxyz')

        if endWord not in wordList:
            return []

        m = len(beginWord)
        if m == 1:
            return [[beginWord, endWord]]

        lth = len(wordList) + 1
        wordSet = set(wordList + [beginWord])
        saved = {beginWord: [[beginWord]]}
        nodes = [beginWord]
        while nodes:
            word = nodes.pop(0)
            paths = saved[word]
            if len(paths[0]) + 1 > lth:
                return saved.get(endWord, [])
            for t in range(m):
                first, second = word[:t], word[t + 1:]
                for ch in ascii_lowercase:
                    w = first + ch + second
                    if ch != word[t] and w in wordSet:
                        if w in saved:
                            if len(paths[0]) + 1 > len(saved[w][0]):
                                continue
                            else:
                                saved[w].extend([p + [w] for p in paths])
                        else:
                            nodes.append(w)
                            saved[w] = [p + [w] for p in paths]

                        if w == endWord:
                            lth = len(saved[w][0])
        return saved.get(endWord, [])

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        ascii_lowercase = set('abcdefghijklmnopqrstuvwxyz')
        if endWord not in wordList or not endWord or not beginWord:
            return []
        wordList = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        parents = defaultdict(set)
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                # We need to trace the direction in order to distinguish the parents
                direction *= -1

            # The new set of words which will be forward in the next iteration
            next_foward = set()

            # Because all words in forward will be modified by one character
            wordList -= forward
            for word in forward:
                for i in range(len(word)):
                    first, second = word[:i], word[i + 1:]
                    for ch in ascii_lowercase:
                        combined_word = first + ch + second
                        if combined_word in wordList:
                            next_foward.add(combined_word)
                            # Because at the last part, we find parents by indexing dictionary from endWord
                            # So when direction == 1, the combined_word is the key
                            # otherwise, the combined_word should be the value of dictionary.
                            if direction == 1:
                                parents[combined_word].add(word)
                            else:
                                parents[word].add(combined_word)

            # next_foward and backward are always in different direction,
            # so if they have common elements we find a path.
            # We check and return this function inside is because this problem finds the all shortest paths
            if next_foward & backward:
                # Starting from the endWord, we find its parent and append to results
                # And do this until we reach the beginWord
                results = [[endWord]]
                while results[0][0] != beginWord:
                    results = [[parent] + result for result in results
                               for parent in parents[result[0]]]
                return results
            forward = next_foward
        return []


if __name__ == '__main__':
    s = Solution()

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # s.findLadders(beginWord, endWord, wordList)
    #
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    # s.findLadders(beginWord, endWord, wordList)
    #
    # beginWord = "leet"
    # endWord = "code"
    # wordList = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
    # s.findLadders(beginWord, endWord, wordList)

    with open('sample.txt', 'r') as f:
        beginWord = f.readline().strip().strip('"')
        endWord = f.readline().strip().strip('"')
        wordList = f.readline().strip().replace('"', '')[1:-1].split(',')
    s.findLadders(beginWord, endWord, wordList)
