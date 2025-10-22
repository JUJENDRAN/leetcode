class Solution(object):
    def findLexSmallestString(self, s, a, b):
        from collections import deque

        visited = set([s])
        queue = deque([s])
        ans = s

        while queue:
            cur = queue.popleft()
            if cur < ans:
                ans = cur

            arr = list(cur)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            add_a = "".join(arr)

            rotate_b = cur[-b:] + cur[:-b]

            for nxt in [add_a, rotate_b]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return ans