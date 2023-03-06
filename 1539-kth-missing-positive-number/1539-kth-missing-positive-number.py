class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = []
        end = arr[-1]
        for i in range(1,end+1+k):
            if i in arr:
                continue
            else:
                ans.append(i)
                k-=1
                if k == 0:
                    break
        
        return ans[-1]
                    