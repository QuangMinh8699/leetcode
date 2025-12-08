class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        idx = 0
        while idx < len(s):
            if idx + 1 < len(s) and m[s[idx]] < m[s[idx + 1]]:
                result = result + m[s[idx + 1]] - m[s[idx]]
                idx += 2
            else:
                result = result + m[s[idx]]
                idx += 1
            
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))