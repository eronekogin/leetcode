"""
https://leetcode.com/problems/encrypt-and-decrypt-strings/description/
"""


from collections import Counter


class Encrypter:
    """
    Encrypter
    """

    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        encrypt_memo: dict[str, str] = {}

        for k, v in zip(keys, values):
            encrypt_memo[k] = v

        self.encrypt_memo = encrypt_memo

        allowed_encrypted_words = Counter(
            self._encrypt_with_fill(w, ' ')
            for w in dictionary
        )

        self.allowed_encrypted_words = allowed_encrypted_words

    def _encrypt_with_fill(self, w: str, fill='') -> str:
        """
        encrypt with fill char
        """
        return ''.join(
            self.encrypt_memo.get(c, fill)
            for c in w
        )

    def encrypt(self, word1: str) -> str:
        """
        encrypt
        """
        return self._encrypt_with_fill(word1)

    def decrypt(self, word2: str) -> int:
        """
        decrypt
        """
        return self.allowed_encrypted_words[word2]


e = Encrypter(["a", "b", "c", "d"], ["ei", "zf", "ei", "am"], [
              "abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
print(e.decrypt('eizfeiam'))
