class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))