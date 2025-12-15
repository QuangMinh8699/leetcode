from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1 

        return k
    
if __name__ == "__main__":
    s = Solution()
    nums = [3,2,2,3]
    val = 3
    expected_nums = [2,2]
    k = s.removeElement(nums, val)
    assert k == len(expected_nums)
    nums[:k] = sorted(nums[:k])
    for i in range(k):
        assert nums[i] == expected_nums[i]
    
    print("Success !")
