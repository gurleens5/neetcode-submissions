class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if index == len(candidates) or total > target:
                return
            
            #cannot reuse the same index
            #can use another occurrence of the same value
            curr.append(candidates[index])
            dfs(index + 1, curr, total + candidates[index])
            curr.pop()

            while index+1 < len(candidates) and candidates[index+1] == candidates[index]:
                index += 1
            
            dfs(index + 1, curr, total)
        
            
            

        dfs(0, [], 0)
        return res