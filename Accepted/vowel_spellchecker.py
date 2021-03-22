"""
https://leetcode.com/problems/vowel-spellchecker/
"""


class Solution:
    def spellchecker(
            self, wordlist: list[str], queries: list[str]) -> list[str]:
        def remove_vowels(w: str) -> str:
            return ''.join(c if c not in VOWELS else ' ' for c in w)

        VOWELS = set('aeiou')
        sameCheck = set(wordlist)
        caseCheck = {}  # {lowercase word: first matching word}
        vowelCheck = {}  # {word without vowels: first matching word}

        for w in wordlist:
            lw = w.lower()
            vw = remove_vowels(lw)
            if lw not in caseCheck:
                caseCheck[lw] = w

            if vw not in vowelCheck:
                vowelCheck[vw] = w

        rslt = []
        for q in queries:
            if q in sameCheck:
                rslt.append(q)
            else:
                lq = q.lower()
                if lq in caseCheck:
                    rslt.append(caseCheck[lq])
                else:
                    vq = remove_vowels(lq)
                    if vq in vowelCheck:
                        rslt.append(vowelCheck[vq])
                    else:
                        rslt.append('')

        return rslt
