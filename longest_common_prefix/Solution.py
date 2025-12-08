import time
from typing import List

class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        
        j = 0
        i = 0
        first_element = strs[0]
        while j < len(first_element):
            if j == len(strs[i]):
                break
            
            if strs[i][j] != first_element[j]:
                break

            if i == len(strs) - 1:
                prefix += first_element[j]
                i = 0
                j += 1
                continue

            i += 1
        
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Compare prefix with each string
        for s in strs[1:]:
            # Reduce prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]   # Remove last character
                if prefix == "":
                    return ""

        return prefix

if __name__ == "__main__":
    s = Solution()
    x = ["flower","flow","flight"]
    start_time_1 = time.perf_counter()
    res1 = s.longestCommonPrefix1(x)
    print(f"res1: {res1}, executed in: {time.perf_counter() - start_time_1}")

    start_time_2 = time.perf_counter()
    res2 = s.longestCommonPrefix2(x)
    print(f"res2: {res2}, executed in: {time.perf_counter() - start_time_2}")