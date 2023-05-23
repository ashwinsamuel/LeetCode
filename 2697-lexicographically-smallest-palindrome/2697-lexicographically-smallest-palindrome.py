class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)  # Convert the string to a list of characters
        left, right = 0, len(s) - 1  # Initialize the two pointers

        while left <= right:
            if s[left] != s[right]:
                s[left] = min(s[left], s[right])  # Replace with the lexicographically smaller character
                s[right] = s[left]  # Make both characters equal

            left += 1
            right -= 1

        return ''.join(s)  # Return the resulting string