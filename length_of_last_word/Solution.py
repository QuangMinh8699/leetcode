import time

class Solution:
    def lengthOfLastWord1(self, s: str) -> int:
        return len(s.split()[-1])
    
    def lengthOfLastWord2(self, s: str) -> int:
        fl = 0
        n = s.split(" ")
        for i in reversed(n):
            if i != "":
                ans = i
                fl = 1
                break
        if fl == 1:
            return len(ans)
        
    
if __name__ == "__main__":
    s = Solution()
    start_time_1 = time.perf_counter()
    res1 = s.lengthOfLastWord1(" Hello World ")
    print(f"res1: {res1}, executed in: {time.perf_counter() - start_time_1}")

    start_time_2 = time.perf_counter()
    res2 = s.lengthOfLastWord2(" Hello World ")
    print(f"res2: {res2}, executed in: {time.perf_counter() - start_time_2}")