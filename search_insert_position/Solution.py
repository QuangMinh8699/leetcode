from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f = 0 #first
        l = len(nums) - 1 #last 
        m = 0 #mid

        while f <= l:    
            m = (f + l) // 2
            print(f"first - mid - last: {f} - {m} - {l}")
            if nums[m] > target:
                l = m - 1
            elif nums[m] < target:
                f = m + 1
            else:
                return m
        
        return f
    
if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,4], 2))