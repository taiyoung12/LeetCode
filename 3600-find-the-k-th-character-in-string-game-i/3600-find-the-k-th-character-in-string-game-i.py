class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_chars = ''.join(
                chr(((ord(c) - 96) % 26) + 97) if c != 'z' else 'a'
                for c in word
            )
            word += next_chars
        return word[k - 1]