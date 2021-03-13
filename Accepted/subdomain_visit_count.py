"""
https://leetcode.com/problems/subdomain-visit-count/
"""

from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        memo = Counter()
        for cpdomain in cpdomains:
            cnt, s = cpdomain.split()
            cnt = int(cnt)
            domains = s.split('.')
            memo[s] += cnt
            for i in range(1, len(domains)):
                memo['.'.join(domains[i:])] += cnt

        return ['{0} {1}'.format(cnt, s) for s, cnt in memo.items()]
