// https://leetcode.com/problems/array-reduce-transformation/description/

type Fn6 = (accum: number, curr: number) => number;

function reduce(nums: number[], fn: Fn6, init: number): number {
  let rslt: number = init;
  for (const num of nums) {
    rslt = fn(rslt, num);
  }

  return rslt;
}
