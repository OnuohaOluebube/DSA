class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures )
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([t, i])
            
        return result
            
           
        
        
        