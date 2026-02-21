"""
https://leetcode.com/problems/count-complete-substrings/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_complete_substrings(self, word: str, k: int) -> int:
        """
        count complete substrings
        """
        def check(s: str) -> int:
            rslt = 0
            max_len = len(s)

            for i in range(1, 27):
                curr_len = i * k
                if curr_len > max_len:
                    break

                char_cnt = Counter(s[: curr_len])
                freq_cnt = Counter(char_cnt.values())

                rslt += freq_cnt[k] == i

                for j in range(max_len - curr_len):
                    c = s[j]
                    freq_cnt[char_cnt[c]] -= 1
                    char_cnt[c] -= 1
                    freq_cnt[char_cnt[c]] += 1

                    c = s[j + curr_len]
                    freq_cnt[char_cnt[c]] -= 1
                    char_cnt[c] += 1
                    freq_cnt[char_cnt[c]] += 1

                    rslt += freq_cnt[k] == i

            return rslt

        start = 0
        rslt = 0
        n = len(word)
        for end in range(1, n):
            if abs(ord(word[end]) - ord(word[end - 1])) > 2:
                rslt += check(word[start: end])
                start = end

        rslt += check(word[start:])
        return rslt


print(Solution().count_complete_substrings('igigee', 2))
