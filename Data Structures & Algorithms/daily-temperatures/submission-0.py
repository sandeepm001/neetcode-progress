class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]*n
        t = temperatures
        for i in range(n):
            while stack and t[i]>stack[-1][0]:
                _,idx = stack.pop()
                res[idx] = i-idx
            stack.append([t[i],i])
        return res
                
                            