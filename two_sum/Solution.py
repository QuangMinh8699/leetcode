import time
from typing import List

class Solution:
    #Solution 1
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    #Solution 2
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in hash_map:
                return[hash_map[rem],i]
            hash_map[nums[i]]=i
            
if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    start_time_1 = time.perf_counter()
    res1 = s.twoSum1(nums, target)
    print(f"res1: {res1}, executed in: {time.perf_counter() - start_time_1}")

    start_time_2 = time.perf_counter()
    res2 = s.twoSum2(nums, target)
    print(f"res2: {res2}, executed in: {time.perf_counter() - start_time_2}")

