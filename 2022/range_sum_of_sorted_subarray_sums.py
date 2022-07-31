"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
"""


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        prefixSums = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)

        sumOfSubArrays: list[int] = []
        for start in range(n):
            for end in range(start, n):
                sumOfSubArrays.append(prefixSums[end + 1] - prefixSums[start])

        sumOfSubArrays.sort()
        return sum(sumOfSubArrays[left - 1: right]) % (10 ** 9 + 7)

    def rangeSum2(self, nums: list[int], n: int, left: int, right: int) -> int:
        def count_sum_no_less_than(target: int) -> int:
            # Using sliding window to count the total number of sums of sub
            # arrays that is no less than the input target.
            cnt, start = 0, 0
            for end in range(n + 1):
                while prefixSumsOfNums[end] - prefixSumsOfNums[start] > target:
                    start += 1

                cnt += end - start  # = end - 1 - start + 1

            return cnt

        def get_sum_no_less_than(targetIndex: int) -> int:
            # Use binary search to get the highest sum at targetIndex of the
            # final sorted subarray sum array.
            l, r = 0, prefixSumsOfNums[n]
            while l < r:
                m = l + ((r - l) >> 1)
                if count_sum_no_less_than(m) < targetIndex:
                    l = m + 1
                else:
                    r = m

            return l

        def calc_sum_at(targetIndex: int) -> int:
            limit = get_sum_no_less_than(targetIndex)
            cnt, start = 0, 0
            for end in range(n + 1):
                while prefixSumsOfNums[end] - prefixSumsOfNums[start] > limit:
                    start += 1

                # Equals to for i in range(start, end + 1), cnt +=
                # prefixSumofNums[end] - prefixSumOfNums[i]
                cnt += (
                    prefixSumsOfNums[end] * (end - start + 1) -
                    (
                        prefixSumsOfPrefixSums[end] -
                        (
                            prefixSumsOfPrefixSums[start - 1]
                            if start else 0
                        )
                    )
                )

            # Subtract multiple instances that having the same sum as limit.
            return cnt - (count_sum_no_less_than(limit) - targetIndex) * limit

        prefixSumsOfNums = [0] * (n + 1)
        prefixSumsOfPrefixSums = [0] * (n + 1)

        # Calculate prefix sums.
        for i in range(n):
            prefixSumsOfNums[i + 1] = prefixSumsOfNums[i] + nums[i]
            prefixSumsOfPrefixSums[i + 1] = (
                prefixSumsOfPrefixSums[i] + prefixSumsOfNums[i + 1]
            )

        return (calc_sum_at(right) - calc_sum_at(left - 1)) % (10 ** 9 + 7)


print(Solution().rangeSum([1, 2, 3, 4], 4, 1, 5))
