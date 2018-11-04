def _feasible_move(strings):
    idx = strings.index('0')
    if idx == 0:
        yield strings[1] + '0' + strings[2:]
        yield strings[3] + strings[1:3] + '0' + strings[4:]

    elif idx == 1:
        yield '0' + strings[0] + strings[2:]
        yield strings[0] + strings[2] + '0' + strings[3:]
        yield strings[0] + strings[4] + strings[2:4] + '0' + strings[5]

    elif idx == 2:
        yield strings[0] + '0' + strings[1] + strings[3:]
        yield strings[:2] + strings[5] + strings[3:5] + '0'

    elif idx == 3:
        yield '0' + strings[1:3] + strings[0] + strings[4:]
        yield strings[:3] + strings[4] + '0' + strings[5]

    elif idx == 4:
        yield strings[0] + '0' + strings[2:4] + strings[1] + strings[5]
        yield strings[:3] + '0' + strings[3] + strings[5]
        yield strings[:4] + strings[5] + '0'

    else:
        yield strings[:2] + '0' + strings[3:5] + strings[2]
        yield strings[:4] + '0' + strings[4]


class Solution(object):
    def __init__(self):
        self.saved = {'123450': 0}
        nodes = ['123450']
        while nodes:
            strings = nodes.pop(0)
            for s in _feasible_move(strings):
                if s in self.saved:
                    continue
                self.saved[s] = self.saved[strings] + 1
                nodes.append(s)

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        strings = ''.join(str(i) for i in board[0] + board[1])
        return self.saved.get(strings, -1)

    def slidingPuzzle2(self, board):
        target = [1, 2, 3, 4, 5, 0]
        state = [x for y in board for x in y]
        if state == target:
            return 0

        d = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        arrived = {tuple(state)}
        front = [[state.index(0), None, state]]
        distance = 0

        while front:
            distance += 1
            newfront = []
            while front:
                idx, last, curstate = front.pop()
                for nex in d[idx]:
                    if nex != last:
                        new = curstate[:]
                        new[idx], new[nex] = new[nex], new[idx]
                        if new == target:
                            return distance
                        t_new = tuple(new)
                        if t_new not in arrived:
                            newfront.append([nex, idx, new])
                            arrived.add(t_new)
            front = newfront
        return -1


if __name__ == '__main__':
    s = Solution()
    s.slidingPuzzle([[1, 2, 3], [4, 0, 5]])
    s.slidingPuzzle([[4, 1, 2], [5, 0, 3]])
    s.slidingPuzzle([[3, 2, 4], [1, 5, 0]])
