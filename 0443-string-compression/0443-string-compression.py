class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        while j < len(chars):
            count = 1
            while j < len(chars) - 1 and chars[j] == chars[j+1]:
                count += 1
                j += 1
            chars[i] = chars[j]
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    i += 1
                    chars[i] = digit
            i += 1
            j += 1
        return i