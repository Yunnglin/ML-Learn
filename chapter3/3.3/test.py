from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n = len(points),len(points[0])
        dp = points
        for i in range(1,m):
            for j in range(n):
                update = 0
                for col in range(n):
                    update = max(update,dp[i-1][col]-abs(col-j))
                dp[i][j] = dp[i][j] + update
        return max(dp[-1])
points = [[1,2,3],[1,5,1],[3,1,1]]
s = Solution()
print(s.maxPoints(points))