class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        reverse = 0
        x_copy = x
        while x > 0:
            reverse = (reverse * 10) + x % 10
            x //= 10

        return reverse == x_copy
    
if __name__ == "__main__":
    s = Solution()
    x = 1221
    print(s.isPalindrome(x))
        