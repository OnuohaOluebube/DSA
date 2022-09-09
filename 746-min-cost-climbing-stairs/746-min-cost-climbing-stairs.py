class Solution:
    # recursion method
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         self.res = float(inf)
        
#         def dfs(i, currCost):
            
#             if i >= len(cost):
#                 return currCost
            
#             return min(dfs(i+1, currCost+cost[i]), dfs(i+2, currCost+cost[i]))
            
#         return min(dfs(0,0), dfs(1,0))

    # dynamic programming method
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) 
        
        return dp[-1]
            
        
            

            
        