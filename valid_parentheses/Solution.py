class Solution:
    def isValid(self, s: str) -> bool:
        # Đảo map lại để check trực tiếp ký tự đóng, đỡ phải index và lookup nhiều lần
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
    
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("[[]}"))