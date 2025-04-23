class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        lMax = [0] * n
        rMax = [0] * n

        lMax[0] = height[0]
        for i in range(1, n):
            lMax[i] = max(lMax[i - 1], height[i])
        
        rMax[n - 1] = height[n - 1]
        for i in range(n-2, -1,-1):
            rMax[i] = max(rMax[i + 1], height[i])

        for i in range(n):
            res += min(lMax[i], rMax[i]) - height[i]
        return res






        