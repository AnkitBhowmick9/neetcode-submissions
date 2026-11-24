class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^A-Za-z0-9]', '', s)
        for i in range(len(cleaned)//2):
            if cleaned[i].upper() != cleaned[-i-1].upper():
                return False
        return True
        