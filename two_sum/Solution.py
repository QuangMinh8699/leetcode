"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
import time

class Solution(object):
    #Solution 1
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    #Solution 2
    def twoSum2(self, nums, target):
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

